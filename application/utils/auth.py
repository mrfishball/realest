from functools import wraps
from flask import request, g
from application.utils.token import confirm_token

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization", None)
        if token:
            string_token = token.encode("ascii", "ignore")
            user = confirm_token(string_token)
            if user:
                g.current_user = user
                return f(*args, **kwargs)

        return { "status": "error", "message": "Authentication is required to access this resource" }, 401
    return decorated
