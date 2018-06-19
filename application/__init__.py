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
from application.APIs.emailConfirmAPI import ConfirmAPI
from application.APIs.userAPI import UserAPI

api.add_resource(RegisterAPI, "/realest/api/v1.0/register", endpoint="register")
api.add_resource(ConfirmAPI, "/realest/api/v1.0/confirm_email/<token>", endpoint="email_confirm")
api.add_resource(UserAPI, "/realest/api/v1.0/sign_in_with_token/<token>", endpoint="signin")
