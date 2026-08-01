from flask import Blueprint, render_template, session, redirect, url_for

mentor_bp = Blueprint("mentor", __name__)


@mentor_bp.route("/mentor")
def mentor():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("mentor.html")