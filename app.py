from flask import Flask, render_template, redirect, url_for, session
from config import FORM_CONFIG
from carbon_calculation import calculate_carbon_footprint
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)


def initialize_session():
    if "visited_sections" not in session:
        session["visited_sections"] = []
    return redirect(url_for("step", step_number=1))


def get_form_instance(step_number):
    if step_number not in FORM_CONFIG:
        return None

    config = FORM_CONFIG[step_number]
    form = config["form_class"]()

    # Pre-populate form with session data if available
    session_data = session.get(config["session_key"])
    if session_data:
        # Process select fields first
        for form_field, session_field in config["data_mapping"].items():
            if hasattr(form, form_field) and hasattr(
                getattr(form, form_field), "default"
            ):
                setattr(
                    getattr(form, form_field),
                    "default",
                    session_data.get(session_field),
                )
        form.process()

        # Then set regular field data
        for form_field, session_field in config["data_mapping"].items():
            if hasattr(form, form_field) and not hasattr(
                getattr(form, form_field), "default"
            ):
                field = getattr(form, form_field)
                field.data = session_data.get(session_field)

    return form


def handle_form_submission(step_number, form):
    if not form.validate_on_submit():
        return None

    config = FORM_CONFIG[step_number]
    session_data = {}
    for form_field, session_field in config["data_mapping"].items():
        session_data[session_field] = getattr(form, form_field).data

    session[config["session_key"]] = session_data
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
        forms={f"form_{i}": get_form_instance(i) for i in FORM_CONFIG.keys()},
        title=FORM_CONFIG[step_number]["title"],
        description=FORM_CONFIG[step_number]["description"],
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
    )


if __name__ == "__main__":
    app.run(debug=True)
