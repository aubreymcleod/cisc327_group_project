from flask import Blueprint, session, render_template, redirect, request, make_response
from qa327.library.authenticate import authenticate
import qa327.library.tickets as tckts

"""
This file defines the user's homepage through Blueprints, and implements any needed background logic.
"""

home_page = Blueprint('home_page', __name__, template_folder='templates')

@home_page.route('/', methods=['GET', 'POST'])
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
	
	
	sell_msg = request.cookies.get('sell_msg') if 'sell_msg' in request.cookies else ""
	buy_msg = request.cookies.get('buy_msg') if 'buy_msg' in request.cookies else ""
	update_msg = request.cookies.get('update_msg') if 'update_msg' in request.cookies else ""
	tickets = tckts.get_all_tickets()
	tickets = tckts.prune_expired_tickets(tickets)
	
	print("DEBUG:", sell_msg)
	
	resp = make_response(render_template('index.html', user=user, tickets=tickets, balance=user.balance/100, sell_msg=sell_msg, buy_msg=buy_msg, update_msg=update_msg))
	resp.set_cookie('buy_msg', '',expires=0)
	resp.set_cookie('sell_msg', '', expires=0)
	resp.set_cookie('update_msg', '', expires=0)
	return resp
