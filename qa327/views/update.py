from flask import Blueprint, redirect
import qa327.library.tickets as tic

update_page = Blueprint('update_page', __name__)

@update_page.route('/', methods=['GET'])
def update_get():
    return redirect('/', code=303)

@update_page.route('/', methods=['POST'])
def update_post():
    ticket_name = request.form.get('ticket_name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')
    expiration = request.form.get('expiration')

    ticket = tic.update_ticket(ticket_name, quantity, price, expiration)
    #If ticket exists return None, else print error message
    if ticket:
        #debug
        print('debug: failed to update ticket')

    return redirect('/', code=303)
