import re
from datetime import datetime
from app import app
from flask import render_template

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template('admin/dashboard.html')


@app.route("/admin/profile/<name>")
def admin_profile(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello Admin, " + clean_name + "! It's " + formatted_now
    return content
