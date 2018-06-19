from application import mongo, bcrypt

def get_user_with_email(email):
    user = mongo.db.users.find_one({ "email": email })
    return user

def verify_user(email, password, confirm_password):
    user = get_user_with_email(email)
    if user:
        if password == confirm_password:
            if bcrypt.check_password_hash(user["password"], password):
                return user
    return None
