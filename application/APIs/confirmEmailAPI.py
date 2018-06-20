from flask_restful import Resource
from application import mongo, models
from application.utils.token import confirm_token

class ConfirmEmailAPI(Resource):

    def __init__(self):
        super(ConfirmEmailAPI, self).__init__()

    def get(self, token):
        payload = confirm_token(token)
        existing_email = models.get_user_with_email(payload)
        if existing_email:
            update = mongo.db.users.update({ "email": payload }, { "$set": { "confirmed": True } })
            return { "status": "success", "message": "Email confirmed.", "payload": update }, 201

        return { "status": "error", "message": "Invalid or expired token. Please try again." }, 403
