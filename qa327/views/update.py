from flask import Blueprint, redirect,  request, render_template
import qa327.library.tickets as tic

'''
The following functions allow the user to fill out ticket name, quantity,
price and expiration date in order to update a ticket.
If the ticket fails to post, users are given an error message and redirected
to the homepage
'''

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
        #print('debug: failed to update ticket')
        #print("successfully updated ticket listing")
        update_message="successfully updated ticket listing"
    
    else:
        update_message="failed to update ticket"
        
    return render_template('index.html',update_message=update_message)
    return redirect('/', code=303)
