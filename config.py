import os

class BaseConfig():
    BASEDIR = os.path.dirname(os.path.realpath(__file__))
    TEMPLATE_DIR = os.path.join("%s/static" % BASEDIR, "build")
    STATIC_DIR = os.path.join("%s/" % TEMPLATE_DIR, "static")
    SECRET_KEY = "uglymojo"

class DevelopmentConfig(BaseConfig):
    # Development configuration.
    MONGO_DBNAME = "realest_dev"
    MONGO_URI = "mongodb://127.0.0.1"
    MONGO_PORT = 27017

    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
