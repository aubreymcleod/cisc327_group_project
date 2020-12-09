import pytest
from seleniumbase import BaseCase
from flask_sqlalchemy import SQLAlchemy

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend update ticket requirements.
The cases have been brocken up into smaller class for easy of testing.

These tests were implemented by Nicole Osayande (20056993)

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.library.users.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it returns the test user rather than getting a user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='Test_frontend',
    password=generate_password_hash('Test_frontend'),
    balance=500000
)

test_ticket= Ticket(
    ticket_name='ticket1',
    quantity=11,
    price=30,
    expiration=20201210,
    owners_email='test_update_frontend@hotmail.com'
)

class FrontEndUpdateTest(BaseCase):
    #Test case R5.1.1 - name of the ticket has to be alphanumeric-only,
    #and space allowed on if it is not the first or the last character. [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_name(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter test_ticket's name into element `#update-ticket-name`
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully updated the ticket(s)', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.1.2 name of the ticket has to be alphanumeric-only, and space
    #allowed on if it is not the first or the last character. [white space at tail, fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_name_whitespace_tail(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
         # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        #entering name with whitespace at the tail
        self.type("#update-ticket-name", 'test_ticket_no ')
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Failed to update the ticket(s): The name of the ticket cannot be: blank, contain more than 60 characters, contain soecial characters, or any white space', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.1.3 - name of the ticket has to be alphanumeric-only, and space
    #allowed on if it is not the first or the last character. [white space at head, fail]   
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_name_whitespace_head(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        #entering name with whitespace at the head
        self.type("#update-ticket-name",' test_ticket_no')
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Failed to update the ticket(s): The name of the ticket cannot be: blank, contain more than 60 characters, contain soecial characters, or any white space', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.1.4 - name of the ticket has to be alphanumeric-only, and space
    #allowed on if it is not the first or the last character. [white space at head and tail, fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_name_whitespace_head_tail(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        #entering name with whitespace at the head and tail
        self.type("#update-ticket-name",' test_ticket_no ')
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Failed to update the ticket(s): The name of the ticket cannot be: blank, contain more than 60 characters, contain soecial characters, or any white space', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.1.5 - name of the ticket has to be alphanumeric-only, and space
    #allowed on if it is not the first or the last character. [special characters, fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_name_special_chars(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        #entering name with special chars
        self.type("#update-ticket-name",'+35+_+!c|<3+_y0')
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Failed to update the ticket(s): The name of the ticket cannot be: blank, contain more than 60 characters, contain soecial characters, or any white space', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test case R5.1.6 - name of the ticket has to be alphanumeric-only, and space
    #allowed on if it is not the first or the last character. [special characters and white space at tail, fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_name_special_chars_whitespace_tail(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        #entering name with special chars and whitespace at the tail
        self.type("#update-ticket-name",'+35+_+!c|<3+_y0 ')
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows failure message
        self.assert_text('Failed to update the ticket(s): The name of the ticket cannot be: blank, contain more than 60 characters, contain soecial characters, or any white space', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test case R5.1.7 - name of the ticket has to be alphanumeric-only, and space
    #allowed on if it is not the first or the last character. [special characters and white space at head, fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_name_special_chars_whitespace_head(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        #entering name withspecial chars and whitespace at the head
        self.type("#update-ticket-name",' +35+_+!c|<3+_y0')
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows failure message
        self.assert_text('Failed to update the ticket(s): The name of the ticket cannot be: blank, contain more than 60 characters, contain soecial characters, or any white space', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')
    

    #Test case R5.1.8 - name of the ticket has to be alphanumeric-only, and space
    #allowed on if it is not the first or the last character. [special characters and white space at tail and head, fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_name_special_chars_whitespace_head_tail(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        #entering name with special chars and whitespace at the head and tail
        self.type("#update-ticket-name",' +35+_+!c|<3+_y0 ')
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows failure message
        self.assert_text('Failed to update the ticket(s): The name of the ticket cannot be: blank, contain more than 60 characters, contain soecial characters, or any white space', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

      
    #Test Case R5.2.1 - name of the ticket is no longer than 60 characters [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_name_length(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter test_ticket's name into element `#update-ticket-name`
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully updated the ticket(s)', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.2.2 - name of the ticket is no longer than 60 characters [fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_name_too_long(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter >60 chars into element `#update-ticket-name`
        self.type("#update-ticket-name", '0123456789012345678901234567890123456789012345678901234567890')
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows failure message
        self.assert_text('Failed to update the ticket(s): The name of the ticket cannot be: blank, contain more than 60 characters, contain soecial characters, or any white space', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.3.1 - quantity of the tickets has to be more than 0,
    #and less than or equal to 100 [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_quantity_inrange(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter test_ticket's name into element `#update-ticket-name`
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element `#update-quantity`
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully updated the ticket(s)', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.3.2 - quantity of the tickets has to be more than 0,
    #and less than or equal to 100 [pass minimum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_quantity_minRange(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter test_ticket's name into element `#update-ticket-name`
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # entering minimum quantity into element `#update-quantity`
        self.type("#update-quantity", '1')
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows success message
        self.assert_text('Successfully updated the ticket(s)', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.3.3 - quantity of the tickets has to be more than 0,
    #and less than or equal to 100 [fail minimum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_quantity_UnderMinRange(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter test_ticket's name into element `#update-ticket-name`
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # entering quantity under minimum range into element `#update-quantity`
        self.type("#update-quantity", '0')
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows failure message
        self.assert_text('You may only sell between one and a hundred tickets inclusive, and quantity listed must be in numeric form', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.3.4 - quantity of the tickets has to be more than 0,
    #and less than or equal to 100 [pass maximum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_quantity_maxRange(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter test_ticket's name into element `#update-ticket-name`
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # entering maximum quantity into element `#update-quantity`
        self.type("#update-quantity", '100')
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully updated the ticket(s)', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.3.5 - quantity of the tickets has to be more than 0,
    #and less than or equal to 100 [fail maximum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_quantity_OverMaxRange(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter test_ticket's name into element `#update-ticket-name`
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # entering quantity over maximum range into element `#update-quantity`
        self.type("#update-quantity", '101')
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('You may only sell between one and a hundred tickets inclusive, and quantity listed must be in numeric form', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')
        
    #Test Case R5.3.6 - quantity of the tickets has to be more than 0,
    #and less than or equal to 100 [non-numeric fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_quantity_nonNumeric(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter test_ticket's name into element `#update-ticket-name`
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # entering non numeric quantity into element `#update-quantity`
        self.type("#update-quantity", 'abc')
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows `successfully listed the ticket(s)`
        self.assert_text('You may only sell between one and a hundred tickets inclusive, and quantity listed must be in numeric form', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test Case R5.3.7 - quantity of the tickets has to be more than 0,
    #and less than or equal to 100 [blank fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_quantity_blank(self, *_):
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open /
        self.open(base_url + '/')
        # enter test_ticket's name into element `#update-ticket-name`
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # entering non numeric quantity into element `#update-quantity`
        self.type("#update-quantity", ' ')
        # enter test_ticket's price into element `#sell_price`
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element `#update-expiration`
        self.type("#update-expiration", str(test_ticket.expiration))
        # click `#update-submit`.
        self.click('#update-submit')
        # validate that the `#update_message` element shows failure message
        self.assert_text('You may only sell between one and a hundred tickets inclusive, and quantity listed must be in numeric form', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')



