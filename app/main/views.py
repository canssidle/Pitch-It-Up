from flask import render_template, request, redirect, url_for, abort 
from . import main

@main.route('/')
def index():

    title = 'PITCH-IT-UP'
    

    return render_template('index.html', title = title)


