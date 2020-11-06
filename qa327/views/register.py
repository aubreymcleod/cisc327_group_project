from flask import Blueprint, render_template, request, session, redirect
import qa327.library.users as usr
import qa327.library.validation as valid

"""
This file defines the registration routes, displays a registration page, and performs all of the front end
data collection logic to call the backend registration functions.
"""

register_page = Blueprint('register_page', __name__, template_folder='templates')

@register_page.route('/', methods=['GET'])
def register_get():
    """
    If a user is logged in redirect to the home page.
    Otherwise displays a registration page.
    """
    if 'logged_in' in session:
        return redirect('/', code=303)
    else:
        # templates are stored in the templates folder
        return render_template('register.html', message='Please Register')


@register_page.route('/', methods=['POST'])
def register_post():
    """
    This function collects all of the necessary field data,
    validates the entered data to some standard, then uses
    the backend registration calls to save the new user to
    our database or requests valid data.
    """
    # All of the inforamtion used to register a user gotten from the form
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    # The users name with out spaces, to be used for validation
    nameNoSpace = name.replace(" ", "")

    '''
    A series of conditionals checking if the user's registration input is
    valid or not.
    If it is not an accurate error message will be displayed.
    If it is valid the user will be registered and redirected to the login page.
    '''

    # Check if passwords match
    if password != password2:
        error_message = "The passwords format is incorrect"
    # Check for valid email
    elif not valid.validate_email_address(email):
        error_message = "Email format is incorrect"
    # Check for valid password
    elif not valid.validate_password(password):
        error_message = "Password format is incorrect"
    # Check that the length of the name is proper length
    elif len(name) > 19 or len(name)<3:
        error_message = "Username format is incorrect"
    # Check that there are no non alphanumeric characters other then space
    elif not nameNoSpace.isalnum():
        error_message = "Username format is incorrect"
    # Check that there is no space at begining or end
    elif name[0] == ' ' or name[len(name) - 1] == ' ':
        error_message = "Username format is incorrect"
    else:
        user = usr.get_user(email)
        # Check if email has already been used
        if user:
            error_message = "This email has ALREADY been used"
        # Register User
        elif usr.register_user(email, name, password, password2, 500000):
            error_message = "Failed to store user info."

    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')
