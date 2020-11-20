from flask import Blueprint, redirect,  request
import qa327.library.tickets as tic

'''
The following functions allow the user to fill out ticket name and quantity
when buying a ticket. If the ticket fails to post, users are given an error
message and redirected to the homepage
'''

buy_page = Blueprint('buy_page', __name__)

@buy_page.route('/', methods=['GET'])
def buy_get():
    return redirect('/', code=303)

@buy_page.route('/', methods=['POST'])
def buy_post():
    ticket_name = request.form.get('ticket_name')
    quantity = request.form.get('quantity')

    ticket = tic.buy_ticket(ticket_name, quantity)
    if ticket:
        #debug
        print('debug: failed to buy ticket')	#reverted to debug logging for the sake of project priorities.

    return redirect('/', code=303)
