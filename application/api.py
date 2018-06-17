from flask import request, jsonify, render_template
from application import app, mongo, bcrypt

@app.route("/index", methods=["GET"])
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/<path:path>", methods=["GET"])
def any_path(path):
    return render_template("index.html")

@app.route("/api/create_user", methods=["GET","POST"])
def create_user():
    if (request.data):
        incoming = request.get_json()
        email = incoming["email"]
        existing_email = mongo.db.users.find_one({ "email": email })
        if existing_email:
            result = jsonify(error="Looks like there's already an account associated with the email '{}'.".format(email))
        else:
            name = "{} {}".format(incoming["firstName"], incoming["lastName"])
            password_hash = bcrypt.generate_password_hash(incoming["password"]).decode("utf-8")
            user = mongo.db.users.insert({"email": email, "email": email, "password": password_hash})
            result = jsonify(success=user)
    else:
        result = jsonify(error="Insufficient data to create a new user.")
    return (result)
