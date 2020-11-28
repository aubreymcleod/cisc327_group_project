from qa327.models import db,Ticket
from datetime import date
import qa327.library.users as usr

"""
This file defines any and all backend functions relating to operating on tickets.
"""

def get_all_tickets():
    """
    this function takes no arguments and returns all valid tickets in our database.
    :return: returns all valid tickets in the database
    """
    tickets = Ticket.query.all() #list of all tickets in database
    return tickets

def get_ticket(ticket_name):
    query = db.session.query(Ticket)
    query = query.filter(Ticket.ticket_name==ticket_name)
    ticket = query.all()
    return ticket

def prune_expired_tickets(tickets):
	todays_date = date.today().strftime("%Y/%m/%d")
	valid_tickets = []			#list of all non expired tickets
	for ticket in tickets:
		if ticket.expiration >= todays_date:
			valid_tickets.append(ticket)

	return valid_tickets


def get_existing_tickets(name,email):
    query = db.session.query(Ticket)
    query = query.filter(Ticket.owners_email==email)
    query = query.filter(Ticket.ticket_name==name)
    tickets = query.all()
    return tickets

#The following 3 functions will allow users to add a ticket to sell, buy a ticket and update a ticket
def add_ticket(ticket_name, quantity, price, expiration, owners_email):

    existing = get_existing_tickets(ticket_name, owners_email)
    if existing == []:
        ticket = Ticket(ticket_name = ticket_name, quantity = quantity, price = price, expiration = expiration, owners_email = owners_email)
        db.session.add(ticket)
        db.session.commit()
        return None
    else:
        if existing[0].ticket_name == ticket_name:
            return "Failed to list tickets, you have already posted a ticket with that name; if you are updating a batch, please use the update form"
        if existing[0].price != int(price):
            return "Failed to list tickets, please list of this kind of ticket at one price"
    return "Failed to list tickets."


def buy_ticket(ticket_name, quantity, user_balance, email):
    # Get tickets with same name
    available_tickets = get_ticket(ticket_name)

    # Check that there are tickets of that name
    if len(available_tickets) !=0:
        # Pick the first one, in the case that there are more then one
        ticket = available_tickets[0]

        # Check if there are enough tickets to buy
        if ticket.quantity < int(quantity):
            return " Too few tickets available"

        # Checks if user has enough to buy tickets
        cost = ticket.price * int(quantity)
        total_cost = float(cost) * 1.4
        if total_cost > user_balance:
            return " User balance too low"
        
        # Delete the ticket from the data base
        db.session.delete(ticket)
        db.session.commit()
        #usr.reduce_balance(email, total_cost)
        # Return None for a successful buy
        return None
    else:
        # Return -1 if an error occurs
        return "Ticket not found"

def update_ticket(ticket_name, quantity, price, expiration, owners_email):
    #owners_email - we only want users who actually
    #own a ticket to be able to update a ticket
    existing_ticket=get_existing_tickets(ticket_name, owners_email)
    if existing_ticket != []:
        #when we create the database we create a list of ticket objects
        #we can only update if we find a ticket, so if empty, ticket doesn't exist
        ticket = existing_ticket[0] #theoretically there will only be one ticket returned
        #special case: if the user wants to remove ticket post, update the quantity to zero, remove ticket from database
        if int(quantity)==0:
            db.session.delete(ticket)
            db.session.commit()
            return None
        else:
            ticket.quantity=int(quantity) #making sure the quantity is updated

        ticket.price=int(price)
        ticket.expiration=expiration
        db.session.commit()
        
        return None
    else:
        #ticket not found
        return 'failed to find a ticket update'
        
