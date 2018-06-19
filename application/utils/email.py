from flask import url_for
from flask_mail import Message
from application import mail
from application.utils.token import generate_token

def send_email_confirmation(email):
    token = generate_token(email)
    msg = Message("Email Verification Required", sender="Real-Est Dev", recipients=[email])
    msg.body = '''
    You’re almost there, just one last step to make sure we have all your information.
    You entered {} as the email address for your RealEst account during the sign-up process.
    If this is you, just click on the link below and you're ready to go.

    {}

    Thanks,
    Team RealEst
    '''.format(email, url_for("email_confirm", token=token, _external=True))

    print(msg)
    mail.send(msg)
