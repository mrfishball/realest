from flask_restful import Resource, reqparse
from application import mongo, bcrypt, models
from application.utils.token import TWO_WEEKS, generate_token

class SignInAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("email", required=True, type=str, help="Email field required", location="json")
        self.reqparse.add_argument("password", required=True, type=str, help="Password field required", location="json")
        super(SignInAPI, self).__init__()

    def post(self):
        print(TWO_WEEKS)
        args = self.reqparse.parse_args()
        email = args["email"]
        password = args["password"]
        user = models.verify_user_and_password(email, password)
        if user:
            return { "status": "success", "message": "Logged in as {}".format(str(user["name"])), "token": generate_token(str(user["_id"]), TWO_WEEKS) }, 202

        return { "status": "error", "message": "Email or password does not match." }, 403
