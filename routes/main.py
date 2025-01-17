# routes/main.py
from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_required, current_user
from config import CALCULATOR_CONFIG

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return redirect(url_for("auth.login"))


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@main.route("/calulator", methods=["GET", "POST"])
@login_required
def calc():
    if request.method == "POST":
        results = request.form
        return jsonify(results)
    return render_template("calculator.html", config=CALCULATOR_CONFIG)
