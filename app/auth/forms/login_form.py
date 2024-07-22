from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password= StringField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


