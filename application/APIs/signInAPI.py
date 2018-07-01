from flask_restful import Resource, reqparse
from application import mongo, bcrypt, models
from application.utils.token import TWO_WEEKS, generate_token, confirm_token

class SignInAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("email", location="json")
        self.reqparse.add_argument("password", location="json")
        super(SignInAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        email = args["email"]
        password = args["password"]
        user = models.verify_user_and_password(email, password)
        if user:
            token = generate_token(str(user["_id"]), TWO_WEEKS)
            payload = confirm_token(token)
            if payload:
                return { "status": "success", "token": token, "confirmed": user["confirmed"] }, 201

            return { "status": "error", "message": "Invalid token." }, 403

        return { "status": "error", "message": "Email or password does not match." }, 403
