from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from application import app

FIVE_HOURS = 18000
TWO_WEEKS = 1209600

def generate_token(email, expiration=FIVE_HOURS):
    # Token expires after 5 hours
    s = Serializer(app.config["SECRET_KEY"], expires_in=expiration)
    return s.dumps(email).decode("utf-8")

def confirm_token(token):
    s = Serializer(app.config["SECRET_KEY"])
    try:
        target = s.loads(token)
    except SignatureExpired:
        return { "status": "error", "message": "Token expired." }  # valid token, but expired
    except BadSignature:
        return { "status": "error", "message": "Invalid token." }  # invalid token
    return target
