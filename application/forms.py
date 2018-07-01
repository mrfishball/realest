from flask_inputs import Inputs
from wtforms.validators import InputRequired, Length, EqualTo

class RegistrationForm(Inputs):
    rule = {
        "firstName": [InputRequired(), Length(min=2)],
        "lastNight": [InputRequired(), Length(min=2)],
        "email": [InputRequired()],
        "password": [InputRequired(), Length(min=8)],
        "confirm_password": [InputRequired(), EqualTo("password")]
    }
