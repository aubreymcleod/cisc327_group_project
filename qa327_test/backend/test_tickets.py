import pytest
from seleniumbase import BaseCase
import qa327.library.tickets as tickets
from qa327_test.conftest import base_url
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from unittest.mock import patch

"""
This file defines all unit tests for the backend tickets class.
These tests were implemented by Melissa Zhu (20071132)
Patching will be used for calls to the database.
"""

# Mock some sample tickets
test_tickets = [
    Ticket(ticket_name='test ticket yo', price=10, quantity=10, expiration='20201231',
           owners_email='test_frontend@test.com'),
    Ticket(ticket_name='ticket two', price=10, quantity=10, expiration='20201231',
           owners_email='test_frontend@test.com'),
    Ticket(ticket_name='old ticket yo', price=10, quantity=10, expiration='18971231',
           owners_email='test_frontend@test.com')
]

valid_test_tickets = [
    Ticket(ticket_name='test ticket yo', price=10, quantity=10, expiration='20201231',
           owners_email='test_frontend@test.com'),
    Ticket(ticket_name='ticket two', price=10, quantity=10, expiration='20201231',
           owners_email='test_frontend@test.com')
]

#TICKET.1.1 Given a ticket name the function should return the ticket if found, and None if not (ticket exists)
@patch('qa327.library.tickets.get_ticket', return_value=test_tickets)
def test_ticket_exists(self, *_):
    test_ticket_name = "test ticket yo"
    assert tickets.get_ticket(test_ticket_name) is test_tickets

#TICKET.1.2 Given a ticket name the function should return the ticket if found, and None if not (ticket does not exist)
@patch('qa327.library.tickets.get_ticket', return_value=None)
def test_ticket_does_not_exist(self, *_):
    test_ticket_name = "incorrect ticket name"
    assert tickets.get_ticket(test_ticket_name) is None

#TICKET.2.1 A ticket's expiry date should be verified to be not expired. If ticket is not expired the function should return the ticket, if not return None (valid)    
@patch('qa327.library.tickets.prune_expired_tickets', return_value=valid_test_tickets)
def test_ticket_not_expired(self, *_):
    assert tickets.prune_expired_tickets(test_tickets) is valid_test_tickets

#TICKET.2.2 A ticket's expiry date should be verified to be not expired. If ticket is not expired the function should return the ticket, if not return None (invalid)
@patch('qa327.library.tickets.get_ticket', return_value=None)
def test_ticket_expired(self, *_):
    test_ticket_name = "test ticket yo"
    test_ticket_date = "19990101"
    assert tickets.get_ticket(test_ticket_name) is None

#TICKET.3.1 The ticket should be added to the database when all input requriements check out, if an error occurs it should be reported (pass)
@patch('qa327.models.db.session.add', return_value=None)
@patch('qa327.models.db.session.commit', return_value=None)
def test_ticket_valid(self, *_):
    test_ticket_name = "test ticket yo"
    test_ticket_owner = "test_frontend@test.com"
    test_ticket_quantity = 10
    test_ticket_price = 10
    test_ticket_date = "20201231"
    assert tickets.add_ticket(test_ticket_name, test_ticket_quantity, test_ticket_price, test_ticket_date, test_ticket_owner) is None

#TICKET.3.2 The ticket should be added to the database when all input requriements check out, if an error occurs it should be reported (error from .add)
@patch('qa327.models.db.session.add', side_effect=Exception('mocked error'))
@patch('qa327.models.db.session.commit', return_value=-1)
def test_ticket_add_error(self, *_):
    test_ticket_name = "test ticket yo"
    test_ticket_owner = "test_frontend@test.com"
    test_ticket_quantity = 10
    test_ticket_price = 10
    test_ticket_date = "20201231"
    assert tickets.add_ticket(test_ticket_name, test_ticket_quantity, test_ticket_price, test_ticket_date, test_ticket_owner) == 'mocked error'

#TICKET.3.3 The ticket should be added to the database when all input requriements check out, if an error occurs it should be reported (error from .commit)
@patch('qa327.models.db.session.add', return_value=-1)
@patch('qa327.models.db.session.commit', side_effect=Exception('mocked error'))
def test_ticket_commit_error(self, *_):
    test_ticket_name = "test ticket yo"
    test_ticket_owner = "test_frontend@test.com"
    test_ticket_quantity = 10
    test_ticket_price = 10
    test_ticket_date = "20201231"
    assert tickets.add_ticket(test_ticket_name, test_ticket_quantity, test_ticket_price, test_ticket_date, test_ticket_owner) == 'mocked error'

