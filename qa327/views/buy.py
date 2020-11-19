from flask import Blueprint, redirect,  request, render_template
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
        #print('debug: failed to buy ticket')
       buy_message="successfully bought ticket(s)"
    else:
        buy_message="failed to buy ticket(s)"

    return render_template('index.html',buy_message=buy_message)
    return redirect('/', code=303)
