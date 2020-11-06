from qa327.models import db,Ticket

"""
This file defines any and all backend functions relating to operating on tickets.
"""

def get_all_tickets():
    """
    this function takes no arguments and returns all valid tickets in our database.
    :return: returns all valid tickets in the database
    """
    return []

def add_ticket(ticket_name, quantity, price, expiration):
    ticket = Ticket(ticket_name = ticket_name, quantity = quantity, price = price, expiration = expiration)
    db.session.add(ticket)
    db.session.commit()
    return None

def buy_ticket(ticket_name, quantity):
    return None

def update_ticket(ticket_name, quantity, price, expiration):
    return None
