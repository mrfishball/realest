from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    firstName = StringField("First Name", validators=[InputRequired(), Length(min=2)])
    lastName = StringField("Last Name", validators=[InputRequired(), Length(min=2)])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), EqualTo("password")])
