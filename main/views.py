from . import main
from flask import render_template,request,redirect,url_for,abort 

@main.route('/')
def index():
    title =  'PITCH IT UP ! '
    return render_template( title = title)

