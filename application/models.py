from application import mongo, bcrypt
from application.utils.email import send_email_confirmation

def get_user_with_email(email):
    user = mongo.db.users.find_one({ "email": email })
    return user

def verify_user_and_password(email, password):
    user = get_user_with_email(email)
    if user:
        if bcrypt.check_password_hash(user["password"], password):
            return user
    return None

def register_user(firstName, lastName, email, password):
    existing_user = get_user_with_email(email)
    if existing_user:
        return None
    password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = mongo.db.users.insert({ "firstName": firstName, "lastName": lastName, "email": email, "password": password_hash, "confirmed": False })
    send_email_confirmation(email)
    return new_user
