from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField
from wtforms.validators import Required


class RegisterForm(FlaskForm):

    username = StringField('Enter Username',validators=[Required()])
    email = StringField('Enter your email', validators=[Required()])
    Passwor = PasswordField('P')