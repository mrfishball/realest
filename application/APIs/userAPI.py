from flask_restful import Resource, reqparse
from application import mongo, bcrypt, models
from application.utils.token import TWO_WEEKS, generate_token

class UserAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("email", required=True, type=str, help="Email field required", location="json")
        self.reqparse.add_argument("password", required=True, type=str, help="Password field required", location="json")
        self.reqparse.add_argument("confirm_password", required=True, help="Password confirm field required", location="json")
        super(UserAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        email = args["email"]
        password = args["password"]
        confirm_pass = args["confirm_password"]
        user = models.verify_user(email, password, confirm_pass)
        if user:
            return { "status": "success", "message": user, "token": generate_token(user, TWO_WEEKS) }, 202

        return { "status": "error", "message": "Email or password does not match." }, 403
