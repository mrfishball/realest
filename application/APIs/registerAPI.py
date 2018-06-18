from flask import request, jsonify
from flask_restful import Resource, reqparse, fields, marshal
from application import mongo, bcrypt, api

class RegisterAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_arguement("firstName", type=str, required=True, help="First name field required", location="json")
        self.reqparse.add_arguement("lastName", type=str, required=True, help="Last name field required", location="json")
        self.reqparse.add_arguement("email", type=str, required=True, help="Email field required", location="json")
        self.reqparse.add_arguement("password", type=str, required=True, help="Password field required", location="json")

        super(RegisterAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        email = args["email"]
        existing_email = mongo.db.users.find_one({ "email": email })
        if existing_email:
            return { "status": "error" }, 403
        else:
            name = "{} {}".format(args["firstName"], args["lastName"])
            password_hash = bcrypt.generate_password_hash(args["password"]).decode("utf-8")
            new_user = mongo.db.users.insert({ "email": email, "name": name, "password": password_hash })
            return { "status": "success" }, 201
