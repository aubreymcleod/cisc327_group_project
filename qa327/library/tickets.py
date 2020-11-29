from qa327.models import db,Ticket
from datetime import date

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


def prune_expired_tickets(tickets):
    """
    this function takes a list of tickets, and returns all tickets in that list that are not expired.
    :return: returns all nonexpired tickets from a list of tickets.
    """
	todays_date = date.today().strftime("%Y/%m/%d")
	valid_tickets = []			#list of all non expired tickets
	for ticket in tickets:
		if ticket.expiration >= todays_date:
			valid_tickets.append(ticket)

	return valid_tickets


def get_existing_tickets(name, qty, pr, ex, email):
    """
    this function takes a ticket name an owners_email and returns all tickets that meet that description in the database
    :return: returns tickets with names matching names, owned by a given seller.
    """
    query = db.session.query(Ticket)
    query = query.filter(Ticket.owners_email==email)
    query = query.filter(Ticket.ticket_name==name)
    tickets = query.all()
    return tickets

#The following 3 functions will allow users to add a ticket to sell, buy a ticket and update a ticket
def add_ticket(ticket_name, quantity, price, expiration, owners_email):
    """
    this function takes a defintion of a ticket, ensures that the seller has not already posted the ticket, then either:
    posts the new ticket to the database, or
    returns an error message explaining why the ticket could not be posted.
    """
    existing = get_existing_tickets(ticket_name, quantity, price, expiration, owners_email)
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

def buy_ticket(ticket_name, quantity):
    return None

def update_ticket(ticket_name, quantity, price, expiration):
    return None
