from flask import Blueprint, session, render_template, redirect
from qa327.library.authenticate import authenticate
import qa327.library.tickets as tckts

"""
This file defines the user's homepage through Blueprints, and implements any needed background logic.
"""

home_page = Blueprint('home_page', __name__, template_folder='templates')

@home_page.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    """
    profile renders the user's profile page at the "/" route.
    """

    if 'logged_in' not in session:
            return redirect('/login', code=303)

    

    
    tickets = tckts.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets, balance=user.balance/100)
