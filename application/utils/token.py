from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from application import app

def generate_confirmation_token(email, expires_sec=3600):
    s = Serializer(app.config["SECRET_KEY"], expires_sec)
    return s.dumps(email).decode("utf-8")

def confirm_email(token):
    s = Serializer(app.config["SECRET_KEY"])
    try:
        email = s.loads(token)
    except:
        return None
    return email
