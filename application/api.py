from flask import request, jsonify, render_template
from application import app, mongo

@app.route("/index", methods=["GET"])
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
