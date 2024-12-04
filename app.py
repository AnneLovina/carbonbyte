# app.py
from flask import Flask, render_template, redirect, url_for, session
from forms import ServerInfrastructureForm, StorageForm, NetworkingForm
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)

TOTAL_SECTIONS = 3


def calculate_carbon_footprint(server_data, storage_data, networking_data):
    # This is a simplified calculation - you should replace with your actual logic
    monthly_emissions = 0

    # Server emissions based on location and usage
    location_factors = {"europe": 0.23, "north_america": 0.38, "asia": 0.54}

    server_factor = location_factors.get(server_data.get("location", "europe"), 0.38)
    cpu_usage = float(server_data.get("cpu_usage", 0)) / 100
    server_emissions = server_factor * cpu_usage * 720  # 720 hours in a month

    # Storage emissions
    storage_amount = float(storage_data.get("amount", 0))
    storage_type_factor = {"ssd": 0.000875, "hdd": 0.000400, "hybrid": 0.000600}
    storage_factor = storage_type_factor.get(storage_data.get("type", "ssd"), 0.000875)
    storage_emissions = storage_amount * storage_factor * 720

    # Network emissions
    bandwidth = float(networking_data.get("bandwidth", 0))
    cdn_factor = {"none": 1, "partial": 0.7, "full": 0.5}
    network_factor = cdn_factor.get(networking_data.get("cdn", "none"), 1)
    network_emissions = bandwidth * 0.000001 * network_factor * 720

    monthly_emissions = server_emissions + storage_emissions + network_emissions

    return {"monthly": monthly_emissions, "yearly": monthly_emissions * 12}


@app.route("/")
def index():
    # Reset session if starting fresh
    if "visited_sections" not in session:
        session["visited_sections"] = []
    return redirect(url_for("step", step_number=1))


@app.route("/step/<int:step_number>", methods=["GET", "POST"])
def step(step_number):
    if step_number not in range(1, TOTAL_SECTIONS + 1):
        return redirect(url_for("step", step_number=1))

    session["current_section"] = step_number
    if "visited_sections" not in session:
        session["visited_sections"] = []
    if step_number not in session["visited_sections"]:
        session["visited_sections"] = list(
            set(session["visited_sections"] + [step_number])
        )

    # Initialize all forms with session data if available
    server_form = ServerInfrastructureForm()
    storage_form = StorageForm()
    networking_form = NetworkingForm()

    # Pre-populate forms with session data
    if "server_data" in session and step_number == 1:
        # First process select fields
        server_form.server_location.default = session["server_data"].get("location")
        server_form.server_type.default = session["server_data"].get("type")
        server_form.process()
        # Then set regular field data
        server_form.cpu_usage.data = session["server_data"].get("cpu_usage")

    if "storage_data" in session and step_number == 2:
        # First process select fields
        storage_form.storage_type.default = session["storage_data"].get("type")
        storage_form.process()
        # Then set regular field data
        storage_form.storage_amount.data = session["storage_data"].get("amount")

    if "networking_data" in session and step_number == 3:
        # First process select fields
        networking_form.cdn_usage.default = session["networking_data"].get("cdn")
        networking_form.process()
        # Then set regular field data
        networking_form.monthly_bandwidth.data = session["networking_data"].get(
            "bandwidth"
        )

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
        return redirect(url_for("results"))

    return render_template(
        "index.html",
        current_section=step_number,
        total_sections=TOTAL_SECTIONS,
        visited_sections=session.get("visited_sections", []),
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
    if 4 not in session.get("visited_sections", []):
        session["visited_sections"] = list(
            set(session.get("visited_sections", []) + [4])
        )

    # Get all data from session
    server_data = session.get("server_data", {})
    storage_data = session.get("storage_data", {})
    networking_data = session.get("networking_data", {})

    # Calculate carbon footprint
    carbon_footprint = calculate_carbon_footprint(
        server_data, storage_data, networking_data
    )

    return render_template(
        "results.html",
        total_sections=TOTAL_SECTIONS,
        visited_sections=session.get("visited_sections", []),
        server_data=server_data,
        storage_data=storage_data,
        networking_data=networking_data,
        carbon_footprint=carbon_footprint,
    )


if __name__ == "__main__":
    app.run(debug=True)
