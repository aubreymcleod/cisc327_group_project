from qa327.models import db,Ticket
from datetime import date
import re

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
	todays_date = date.today().strftime("%Y/%m/%d")
	valid_tickets = []			#list of all non expired tickets
	for ticket in tickets:
		if ticket.expiration >= todays_date:
			valid_tickets.append(ticket)

	return valid_tickets

#The following 3 functions will allow users to add a ticket to sell, buy a ticket and update a ticket
def add_ticket(ticket_name, quantity, price, expiration, owners_email):
    ticket = Ticket(ticket_name = ticket_name, quantity = quantity, price = price, expiration = expiration, owners_email = owners_email)
    db.session.add(ticket)
    db.session.commit()
    return None

def buy_ticket(ticket_name, quantity):
    return None

def update_ticket(ticket_name, quantity, price, expiration):
    return None


#Ticket validation functions
def validate_ticket(ticket):
	if validate_name(ticket.ticket_name) and validate_date(ticket.ticket_expiration) and validate_quantity(ticket.quantity) and validate_price(ticket.price):
		return True #is valid
	return False

def validate_name(name):
	if re.match("^[a-zA-Z0-9][a-zA-Z0-9 ]*$", name) and 6<=len(name)<=60:
		return True
	return False
	
def validate_date(expiration_date):
	todays_date = date.today().strftime("%Y/%m/%d")
	if re.match("^[0-9][0-9][0-9][0-9](0[1-9]|1[0-2])([0][1-9]|[1-2][0-9]|3[0-1])$", expiration_date) and expiration_date >= todays_date:
		return True
	return False
	
def validate_quantity(qty):
	if 0<int(qty)<=100:
		return True
	return False
	
def validate_price(price):
	if 10<=int(price)<=100:
		return True
	return False
	