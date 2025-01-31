# routes/main.py
from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from config import CALCULATOR_CONFIG
from config import LANDING_PAGE_CONFIG
from calculations import calculate

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("landing.html", config=LANDING_PAGE_CONFIG)


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@main.route("/calculator", methods=["GET", "POST"])
# @login_required
def calc():
    if request.method == "POST":
        results = calculate(request.form)
        import json

        raw_string = json.dumps(results, indent=4)
        return render_template("results.html", raw=raw_string, **results)
    return render_template("calculator.html", config=CALCULATOR_CONFIG)


@main.route("/imprint")
def imprint():
    return render_template("imprint.html", config=LANDING_PAGE_CONFIG)


@main.route("/privacy")
def privacy():
    return render_template("privacy.html", config=LANDING_PAGE_CONFIG)
