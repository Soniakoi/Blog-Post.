from . import auth
from .. import db
from flask import render_template

@auth.route('/login')
def login():
  return render_template('auth/login.html')
 