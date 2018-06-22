from flask_restful import Resource, reqparse
from application import mongo, bcrypt, models


class RegisterAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("firstName", type=str, required=True, help="First name field required", location="json")
        self.reqparse.add_argument("lastName", type=str, required=True, help="Last name field required", location="json")
        self.reqparse.add_argument("email", type=str, required=True, help="Email field required", location="json")
        self.reqparse.add_argument("password", type=str, required=True, help="Password field required", location="json")
        self.reqparse.add_argument("confirm_password", type=str, required=True, help="Password confirm field required", location="json")

        super(RegisterAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        email = args["email"]
        firstName = args["firstName"]
        lastName = args["lastName"]
        password = args["password"]
        confirm_password = args["confirm_password"]
        if password == confirm_password:
            user = models.register_user(firstName, lastName, email, password)
            if user:
                return { "status": "success", "message": "New user registered successfully." }, 201

            return { "status": "error", "message": "Account already exist."}, 403

        return { "status": "error", "message": "Passwords don't match." }, 403
