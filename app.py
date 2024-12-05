from flask import Flask, render_template, redirect, url_for, request, session
from config import FORM_CONFIG
from carbon_calculation import calculate_carbon_footprint
import secrets
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)


def initialize_session():
    if "visited_sections" not in session:
        session["visited_sections"] = []
    return redirect(url_for("step", step_number=1))


def get_form_instance(step_number):
    """
    Get a form instance for the given step number, pre-populated with session data if available.
    """
    if step_number not in FORM_CONFIG:
        return None

    config = FORM_CONFIG[step_number]
    form = config["form_class"]()

    # Pre-populate form with session data if available
    session_data = session.get(config["session_key"])
    if session_data:
        # Process select fields first to handle choices properly
        for field_name, field in form._fields.items():
            if hasattr(field, "default") and field_name in session_data:
                # Handle date fields
                if hasattr(field, "format") and isinstance(
                    session_data[field_name], str
                ):
                    try:
                        # Convert string to datetime object using the field's format
                        date_value = datetime.strptime(
                            session_data[field_name], field.format
                        )
                        setattr(field, "default", date_value)
                    except (ValueError, TypeError):
                        # If date parsing fails, skip setting the default
                        continue
                else:
                    setattr(field, "default", session_data[field_name])
        form.process()

        # Then set regular field data
        for field_name, field in form._fields.items():
            if not hasattr(field, "default") and field_name in session_data:
                # Handle date fields for non-default fields
                if hasattr(field, "format") and isinstance(
                    session_data[field_name], str
                ):
                    try:
                        date_value = datetime.strptime(
                            session_data[field_name], field.format
                        )
                        field.data = date_value
                    except (ValueError, TypeError):
                        continue
                else:
                    field.data = session_data[field_name]

    return form


def handle_form_submission(step_number, form):
    """
    Handle form submission for the given step number.
    Returns the next step number or 'results' if all steps are complete.
    Returns None if the form is invalid or not submitted via POST.
    """
    # Only process if it's a POST request
    if request.method != "POST":
        return None

    # Check form validation
    if not form.validate_on_submit():
        return None

    config = FORM_CONFIG[step_number]

    # Store all form field data directly in session
    session_data = {}
    for field_name, field in form._fields.items():
        if field_name != "submit":  # Exclude the submit button
            if field.data and hasattr(field, "format"):
                # Convert datetime objects to strings for session storage
                try:
                    if isinstance(field.data, datetime):
                        session_data[field_name] = field.data.strftime(field.format)
                    else:
                        session_data[field_name] = field.data
                except (ValueError, AttributeError):
                    # If conversion fails, store the raw data
                    session_data[field_name] = field.data
            else:
                session_data[field_name] = field.data

    session[config["session_key"]] = session_data

    # Determine next step
    next_step = step_number + 1
    return next_step if next_step in FORM_CONFIG else "results"


@app.route("/")
def index():
    return initialize_session()


@app.route("/step/<int:step_number>", methods=["GET", "POST"])
def step(step_number):
    if step_number not in FORM_CONFIG:
        return redirect(url_for("step", step_number=1))

    session["current_section"] = step_number
    if step_number not in session.get("visited_sections", []):
        session["visited_sections"] = list(
            set(session.get("visited_sections", []) + [step_number])
        )

    # Get the appropriate form instance
    current_form = get_form_instance(step_number)

    # Handle form submission
    if current_form:
        next_step = handle_form_submission(step_number, current_form)
        if next_step:
            return redirect(
                url_for(
                    "step" if next_step != "results" else next_step,
                    step_number=next_step if next_step != "results" else None,
                )
            )

    return render_template(
        "index.html",
        current_section=step_number,
        total_sections=len(FORM_CONFIG),
        visited_sections=session.get("visited_sections", []),
        forms={f"form_{step_number}": current_form},  # Only pass the current form
        title=FORM_CONFIG[step_number]["title"],
        description=FORM_CONFIG[step_number]["description"],
        config=FORM_CONFIG,
    )


@app.route("/prev-step")
def prev_step():
    current_step = session.get("current_section", 1)
    if current_step > 1:
        session["current_section"] = current_step - 1
    return redirect(url_for("step", step_number=session["current_section"]))


@app.route("/results")
def results():
    results_step = len(FORM_CONFIG) + 1
    if results_step not in session.get("visited_sections", []):
        session["visited_sections"] = list(
            set(session.get("visited_sections", []) + [results_step])
        )

    # Collect all data from session
    collected_data = {
        config["session_key"]: session.get(config["session_key"], {})
        for config in FORM_CONFIG.values()
    }

    carbon_footprint = calculate_carbon_footprint(**collected_data)

    return render_template(
        "results.html",
        total_sections=len(FORM_CONFIG),
        visited_sections=session.get("visited_sections", []),
        collected_data=collected_data,
        carbon_footprint=carbon_footprint,
        config=FORM_CONFIG,
    )


if __name__ == "__main__":
    app.run(debug=True)
