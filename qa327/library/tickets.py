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
    
    todays_date = date.today().strftime("%Y/%m/%d")
    
    #ticket.expiration = date (string)
    tickets = Ticket.query.all() #list of all tickets in database
    valid_tickets = []
    for ticket in tickets:
        if ticket.expiration >= todays_date:
            valid_tickets.append(ticket)
    
    return valid_tickets
    

def add_ticket(ticket_name, quantity, price, expiration, owners_email):
    ticket = Ticket(ticket_name = ticket_name, quantity = quantity, price = price, expiration = expiration, owners_email = owners_email)
    db.session.add(ticket)
    db.session.commit()
    return None

def buy_ticket(ticket_name, quantity):
    return None

def update_ticket(ticket_name, quantity, price, expiration):
    return None
