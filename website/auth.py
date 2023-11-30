from flask import Blueprint

#Setting up the BluePrint
auth = Blueprint('auth', __name__)

#Setting Routes
@auth.route('/login')
def login():
    return "<p>Login<p>"

@auth.route('/logout')
def logout():
    return "<p>Logout<p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up<p>"
