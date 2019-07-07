from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from flask_login import login_required
from ..models import 

@main.route('/about')
def about():
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/')
def index():

    name = "Boss Babe!"
    title = "Welcome to My Blog!"

    return render_template('index.html',name = name)

    # return '<h1> Hello World </h1>'



@main.route('/new_blog', methods = ['GET','POST'])
@login_required

def new_blog():    
   blogform = BlogForm()

