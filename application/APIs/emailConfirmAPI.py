from flask_restful import Resource, reqparse
from application import mongo
from application.utils.token import confirm_email

class ConfirmAPI(Resource):

    def __init__(self):
        super(ConfirmAPI, self).__init__()

    def get(self, token):
        email = confirm_email(token)
        print(email)
        existing_email = mongo.db.users.find_one({ "email": email })
        if existing_email:
            return { "status": "success", "message": "Email confirmed." }, 201
        else:
            return { "status": "error", "message": "Token expired." }, 403
