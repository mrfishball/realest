from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from config import DevelopmentConfig

app = Flask(__name__, static_folder=DevelopmentConfig.STATIC_DIR, template_folder=DevelopmentConfig.TEMPLATE_DIR)

app.config.from_object(DevelopmentConfig)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)

from application import api
