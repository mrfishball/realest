import os

class BaseConfig():
    BASEDIR = os.path.dirname(os.path.realpath(__file__))
    TEMPLATE_DIR = os.path.join("%s/static" % BASEDIR, "build")
    STATIC_DIR = os.path.join("%s/" % TEMPLATE_DIR, "static")
    SECRET_KEY = "e6e3b96c6b9c6c2436da30ef122cfe74"

class DevelopmentConfig(BaseConfig):
    # Development configuration.
    MONGO_URI = "mongodb://127.0.0.1/realest_dev"
    MONGO_PORT = 27017

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USER")
    MAIL_PASSWORD = os.environ.get("MAIL_PASS")

    # TESTING = True
    DEBUG = True
