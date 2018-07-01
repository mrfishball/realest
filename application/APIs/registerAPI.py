from flask_restful import Resource, reqparse, request
from application import mongo, bcrypt, models
from application.forms import RegistrationForm


class RegisterAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("firstName", location="json")
        self.reqparse.add_argument("lastName", location="json")
        self.reqparse.add_argument("email", location="json")
        self.reqparse.add_argument("password", location="json")
        self.reqparse.add_argument("confirm_password", location="json")

        super(RegisterAPI, self).__init__()

    def post(self):
        inputs = RegistrationForm(request)
        if not inputs.validate():
            return { "status": "error", "message": "Invalid data."}, 403
        args = self.reqparse.parse_args()
        email = args["email"]
        firstName = args["firstName"]
        lastName = args["lastName"]
        password = args["password"]
        confirm_password = args["confirm_password"]
        user = models.register_user(firstName, lastName, email, password)
        if user:
            return { "status": "success", "message": "New user registered successfully." }, 201

        return { "status": "error", "message": "Account already exist."}, 403
