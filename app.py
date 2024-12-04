# app.py
from flask import Flask, render_template, redirect, url_for, session
from forms import ServerInfrastructureForm, StorageForm, NetworkingForm
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)

TOTAL_SECTIONS = 3


@app.route("/")
def index():
    # Reset session if starting fresh
    if "current_section" not in session:
        session["current_section"] = 1
    return redirect(url_for("step", step_number=session["current_section"]))


@app.route("/step/<int:step_number>", methods=["GET", "POST"])
def step(step_number):
    if step_number not in range(1, TOTAL_SECTIONS + 1):
        return redirect(url_for("step", current_section=1))

    session["current_section"] = step_number

    # Initialize all forms
    server_form = ServerInfrastructureForm()
    storage_form = StorageForm()
    networking_form = NetworkingForm()

    # Handle form submissions based on current section
    if step_number == 1 and server_form.validate_on_submit():
        session["server_data"] = {
            "location": server_form.server_location.data,
            "type": server_form.server_type.data,
            "cpu_usage": server_form.cpu_usage.data,
        }
        return redirect(url_for("step", step_number=2))

    elif step_number == 2 and storage_form.validate_on_submit():
        session["storage_data"] = {
            "type": storage_form.storage_type.data,
            "amount": storage_form.storage_amount.data,
        }
        return redirect(url_for("step", step_number=3))

    elif step_number == 3 and networking_form.validate_on_submit():
        session["networking_data"] = {
            "bandwidth": networking_form.monthly_bandwidth.data,
            "cdn": networking_form.cdn_usage.data,
        }
        # Process final calculations here
        return redirect(url_for("results"))

    return render_template(
        "index.html",
        current_section=step_number,
        total_sections=TOTAL_SECTIONS,
        server_form=server_form,
        storage_form=storage_form,
        networking_form=networking_form,
    )


@app.route("/prev-step")
def prev_step():
    current_step = session.get("current_section", 1)
    if current_step > 1:
        session["current_section"] = current_step - 1
    return redirect(url_for("step", step_number=session["current_section"]))


@app.route("/results")
def results():
    # Calculate final carbon footprint using session data
    server_data = session.get("server_data", {})
    storage_data = session.get("storage_data", {})
    networking_data = session.get("networking_data", {})

    # Add your carbon footprint calculation logic here

    return render_template(
        "results.html",
        server_data=server_data,
        storage_data=storage_data,
        networking_data=networking_data,
    )


if __name__ == "__main__":
    app.run(debug=True)
