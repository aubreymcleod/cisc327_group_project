from flask import Blueprint, render_template, request, session, redirect
import qa327.library.users as usr
import qa327.library.validation as valid

"""
This file defines the login page through blueprint, and implements the necessary front
end input processing to log a user in.
"""

login_page = Blueprint('login_page', __name__, template_folder='templates')

@login_page.route('/', methods=['GET'])
def login_get():
    """
    Displays the login page at the "/login" route
    """
    if 'logged_in' in session:
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='Please login')


@login_page.route('/', methods=['POST'])
def login_post():
    """
    Collects field data from the login screen and calls the requisite backend login functions
    to validate the user or reject their credentials.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not valid.validate_email_address(email) or not valid.validate_password(password):
        return render_template('login.html', message='email/password format is incorrect.')

    user = usr.login_user(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.
        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='email/password combination incorrect')
