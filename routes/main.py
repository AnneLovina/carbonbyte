# routes/main.py
from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from config import CALCULATOR_CONFIG
from calculations import calculate

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return redirect(url_for("auth.login"))


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
