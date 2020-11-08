from flask import Blueprint, redirect, request, session
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

    ticket = tic.add_ticket(ticket_name, quantity, price, expiration, email)
    if ticket:
        #debug
        print('debug: failed to post ticket')

    return redirect('/', code=303)
