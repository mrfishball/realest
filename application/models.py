from application import mongo

def get_user_with_email(email):
    user = mongo.db.users.find_one({ "email": email })
    return user
