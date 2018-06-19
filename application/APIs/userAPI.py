from flask_restful import Resource, reqparse
from application import mongo, bcrypt, models

class UserAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("email", required=True, type=str, help="Email field required", location="json")
        self.reqparse.add_argument("password", required=True, type=str, help="Password field required", location="json")
        self.reqparse.add_argument("confirm_password", required=True, help="Password confirm field required", location="json")
        super(UserAPI, self).__init__()

    def post(self, token):
        args = self.reqparse.parse_args()
        email = args["email"]
        user = models.get_user_with_email(email)
