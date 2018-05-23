from flask import  render_template,redirect,url_for,flash
from flask_login import login_user,login_required,logout_user
from . import auth
from app.models import User
from .form import RegistrationForm,LoginForm
from ..import db
from sqlalchemy import exc
from ..import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')
    return render_template('auth/login.html',login_form = login_form,title=title)


@auth.route('/register',methods['GET','POST'])
def register():
    register_form = RegisterForm()
    if form.validate_on_submit():
        User = User(username=form.username.data,email=form.email.data,password_hash=harshed_password)
        db.session.add(user)
        db.session.commit()
        flash('invalid')

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

