from flask_restful import Resource
from application import mongo, models
from application.utils.token import confirm_token

class ConfirmTokenAPI(Resource):

    def __init__(self):
        super(ConfirmTokenAPI, self).__init__()

    def get(self, token):
        payload = confirm_token(token)
        if payload:
            return { "status": "success", "message": "Token verified." }, 201

        return { "status": "error", "message": "Invalid or expired token. Please try again." }, 403
