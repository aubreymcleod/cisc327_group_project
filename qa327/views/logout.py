from flask import Blueprint, session, redirect

"""
This file defines the logout route through blueprint, and implements the necessary session cancellation functionality.
"""

logout_page = Blueprint('logout_page', __name__)

@logout_page.route('/')
def logout():
    """
    This function cancels a users session and redirects them to the homepage and therefore to the login page.
    """
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')