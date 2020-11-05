from flask import Blueprint, render_template, request, redirect
import qa327.library.users as usr

"""
This file defines the registration routes, displays a registration page, and performs all of the front end
data collection logic to call the backend registration functions.
"""

register_page = Blueprint('register_page', __name__, template_folder='templates')

@register_page.route('/', methods=['GET'])
def register_get():
    """
    displays a registration page.
    """
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@register_page.route('/', methods=['POST'])
def register_post():
    """
    This function collects all of the necessary field data,
    validates the entered data to some standard, then uses
    the backend registration calls to save the new user to
    our database or requests valid data.
    """
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None


    if password != password2:
        error_message = "The passwords do not match"

    elif len(email) < 1:
        error_message = "Email format error"

    elif len(password) < 1:
        error_message = "Password not strong enough"

    else:
        user = usr.get_user(email)
        if user:
            error_message = "User exists"

        elif usr.register_user(email, name, password, password2):
            error_message = "Failed to store user info."

    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')
