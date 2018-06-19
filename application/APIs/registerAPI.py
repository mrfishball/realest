from flask_restful import Resource, reqparse
from application import mongo, bcrypt, models
from application.utils.email import send_email_confirmation

class RegisterAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("firstName", type=str, required=True, help="First name field required", location="json")
        self.reqparse.add_argument("lastName", type=str, required=True, help="Last name field required", location="json")
        self.reqparse.add_argument("email", type=str, required=True, help="Email field required", location="json")
        self.reqparse.add_argument("password", type=str, required=True, help="Password field required", location="json")

        super(RegisterAPI, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        email = args["email"]
        existing_email = models.get_user_with_email(email)
        if existing_email:
            return { "status": "error", "message": "Account already exist." }, 403
        else:
            first_name = args["firstName"]
            last_name = args["lastName"]
            password_hash = bcrypt.generate_password_hash(args["password"]).decode("utf-8")
            new_user = mongo.db.users.insert({ "firstName": first_name, "lastName": last_name, "email": email, "password": password_hash, "confirmed": False })
            send_email_confirmation(email)
            return { "status": "success", "message": "New user registered successfully." }, 201
