from flask import Flask
from flask_restful import Api
from flask_mail import Mail
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from config import DevelopmentConfig

app = Flask(__name__, static_folder=DevelopmentConfig.STATIC_DIR, template_folder=DevelopmentConfig.TEMPLATE_DIR)

app.config.from_object(DevelopmentConfig)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
api = Api(app)
mail = Mail(app)

from application import routes
from application.APIs.registerAPI import RegisterAPI
from application.APIs.confirmEmailAPI import ConfirmEmailAPI
from application.APIs.confirmTokenAPI import ConfirmTokenAPI
from application.APIs.signInAPI import SignInAPI

api.add_resource(RegisterAPI, "/realest/api/v1.0/register", endpoint="register")
api.add_resource(ConfirmEmailAPI, "/realest/api/v1.0/confirm_email/<token>", endpoint="email_confirm")
api.add_resource(ConfirmTokenAPI, "/realest/api/v1.0/confirm_token/<token>", endpoint="token_confirm")
api.add_resource(SignInAPI, "/realest/api/v1.0/sign_in", endpoint="signin")
