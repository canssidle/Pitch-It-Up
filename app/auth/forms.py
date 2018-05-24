from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField
from wtforms.validators import Required


class RegisterForm(FlaskForm):

    username = StringField('Enter Username',validators=[Required()])
    email = StringField('Enter your email', validators=[Required()])
    Password = PasswordField('Password',validators = [Required()])
    EqualTo('password_confirm',message = 'Confirm your password')])
    password_confirm = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Enter Your Email Here ', validators=[Required(),Email()])
	password = PasswordField('Password', validators=[Required()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login In')


    