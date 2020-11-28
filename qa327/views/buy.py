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
    ticket_name = request.form.get('ticket_name')   # Set ticket name from form
    email=session['logged_in']                      # Set email from logged in session
    quantity = request.form.get('quantity')         # Set quanity from from
    errors=[]                                       # Create an empty arry to store errors
    buy_msg = 'Failed to buy ticket. '              # Set buy_msg to a failed message


    # Check that the ticket name meets requirements
    if not valid.validate_name(ticket_name):
        errors.append("The name of the ticket must be no more than 60 characters")
    # Check that the quantity is valid
    if not valid.validate_quantity(quantity) and int (quantity)!=0:
         errors.append("You may only buy between 0 and 100 tickets inclusive")   

    # If no errors in input
    if len(errors) == 0:

        # Try to buy the ticket
        ticket = tic.buy_ticket(ticket_name, quantity)

        # If successfully bought change buy msg to show that
        if ticket is None:
            buy_msg = 'Sucessfully bought the ticket(s).'

        # If failed add to errors
        else:
            errors.append(ticket)

    # If there are errors in input create message
    elif len(errors) > 0:
        buy_msg += ", ".join(errors)+"." #adding all of the errors to the updat message

    resp=make_response(redirect('/', code=303)) 
    resp.set_cookie('buy_msg', buy_msg)
    return resp
