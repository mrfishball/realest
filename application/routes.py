from flask import render_template
from application.utils import auth
from application import app

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/<path:path>")
def any_path(path):
    return render_template("index.html")
