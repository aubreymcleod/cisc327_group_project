from flask import Blueprint, redirect
import qa327.library.tickets as tic

buy_page = Blueprint('buy_page', __name__)

@buy_page.route('/', methods=['GET'])
def buy_get():
    return redirect('/', code=303)

@buy_page.route('/', methods=['POST'])
def buy_post():
    ticket_name = request.form.get('ticket_name')
    quantity = request.form.get('quantity')

    ticket = tic.add_ticket(ticket_name, quantity)
    if ticket:
        #debug
        print('debug: failed to buy ticket')

    return redirect('/', code=303)
