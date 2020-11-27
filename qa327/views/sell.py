from flask import Blueprint, redirect, session, request, make_response
import qa327.library.validation as valid
import qa327.library.tickets as tic

'''
The following functions allow the user to fill out ticket name, quantity,
price and expiration date for the ticket they want to post to sell. If
the ticket fails to post, users are given an error message and redirected
to the homepage
'''

sell_page = Blueprint('sell_page', __name__)

@sell_page.route('/', methods=['GET'])
def sell_get():
    return redirect('/', code=303)

@sell_page.route('/', methods=['POST'])
def sell_post():
	email = session['logged_in']
	ticket_name = request.form.get('ticket_name')
	quantity = request.form.get('quantity')
	price = request.form.get('price')
	expiration = request.form.get('expiration')
	errors = []
	sell_msg='failed to list the ticket(s): '

	if not valid.validate_name(ticket_name):
		errors.append("The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end)")
	if not valid.validate_quantity(quantity):
		errors.append("You may only sell between 1 and 100 tickets at a time with SeetGeek")
	if not valid.validate_price(price):
		errors.append("Prices must be between $10 and $100 (whole numbers only)")
	if not valid.validate_date(expiration):
		errors.append("You cannot sell expired tickets")
	if len(errors) == 0:
		ticket = tic.add_ticket(ticket_name, quantity, price, expiration, email)
		if ticket is None:
			sell_msg='Successfully listed the ticket(s)'
		else:
			errors.append(ticket)

	if len(errors) > 0:
		sell_msg += ", ".join(errors)+"."
	
	resp = make_response(redirect('/', code=303))
	resp.set_cookie('sell_msg', sell_msg)
	
	return resp
