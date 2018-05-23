from flask import render_template, request, redirect, url_for, abort 
from . import main
from flask_login import login_required





@main.route('/')
def index():

    title = 'PITCH-IT-UP'
    

    return render_template('index.html', title = title)

# @login_required
# def user(id):

