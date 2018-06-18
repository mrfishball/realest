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

api.add_resource(RegisterAPI, "/realest/api/v1.0/register")
