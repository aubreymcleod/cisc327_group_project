from flask import Blueprint, redirect,  request, render_template, make_response, session
import qa327.library.tickets as tic
import qa327.library.validation as valid

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
    email=session['logged_in']
    quantity = request.form.get('quantity')
    #price = request.form.get('price')
    #expiration = request.form.get('expiration')
    errors=[]
    buy_msg = 'failed to buy ticket'


    if not valid.validate_name(ticket_name):
        errors.append("The name of the ticket must be no more than 60 characters")
    if not valid.validate_quantity(quantity) and int (quantity)!=0:
         errors.append("You may only buy between 0 and 100 tickets inclusive")   
    
    if len(errors) == 0:
        ticket = tic.buy_ticket(ticket_name, quantity)
        if ticket is None:
            buy_msg = 'Sucessfully bought the ticket(s).'
        else:
            errors.append(ticket)

    elif len(errors) > 0:
        buy_msg += ", ".join(errors)+"." #adding all of the errors to the updat message

    '''   
    if ticket:
        #debug
        #print('debug: failed to buy ticket')
       buy_message="successfully bought ticket(s)"
    else:
        buy_message="failed to buy ticket(s)"
        

    return render_template('index.html',buy_message=buy_message)
    return redirect('/', code=303)
    '''
    resp=make_response(redirect('/', code=303))
    resp.set_cookie('buy_msg', buy_msg)
    return resp
