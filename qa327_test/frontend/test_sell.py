import pytest
from seleniumbase import BaseCase
from flask_sqlalchemy import SQLAlchemy

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import User, Ticket
from werkzeug.security import generate_password_hash

"""
This file defines all unit tests for the frontend sell route.

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='Test_frontend',
    password=generate_password_hash('Test_frontend'),
    balance=500000
)

# Mock some sample tickets
test_tickets = [
    Ticket(ticket_name='test ticket yo', price=10, quantity=10, expiration='20201231',
           owners_email='test_frontend@test.com'),
    Ticket(ticket_name='ticket two', price=10, quantity=10, expiration='20201231',
           owners_email='test_frontend@test.com'),
    Ticket(ticket_name='old ticket yo', price=10, quantity=10, expiration='18971231',
           owners_email='test_frontend@test.com')
]


class FrontEndSellTest(BaseCase):
    # Test case R4.1.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the
    # first or the last character. [passing]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_pass(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", test_tickets[0].ticket_name)
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully listed the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.1.2 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the
    # first or the last character. [fail due to white space at tail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_fail_whitehead(self, *_):
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
        # enter 'test_ticket_yo	 ' into element `#sell_name`
        self.type("#sell-ticket-name", "test_ticket_yo   ")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `Failed to list the ticket(s); no white space allowed at
        # front or back`
        self.assert_text('Failed to list the ticket(s): The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')


    # Test case R4.1.3 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the
    # first or the last character. [fail due to white space at head]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_fail_whitetail(self, *_):
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
        # enter '    test_ticket_yo' into element `#sell_name`
        self.type("#sell-ticket-name", "   test_ticket_yo")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `Failed to list the ticket(s); no white space allowed at
        # front or back`
        self.assert_text('Failed to list the ticket(s): The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')


    # Test case R4.1.4 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the
    # first or the last character. [fail due to white space at head and tail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_fail_whiteboth(self, *_):
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
        # enter '    test_ticket_yo   ' into element `#sell_name`
        self.type("#sell-ticket-name", "   test_ticket_yo   ")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `Failed to list the ticket(s); no white space allowed at
        # front or back`
        self.assert_text('Failed to list the ticket(s): The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.1.5 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the
    # first or the last character. [special character]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_fail_special(self, *_):
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
        # enter '+35+_+!c|<3+_y0' into element `#sell_name`
        self.type("#sell-ticket-name", "+35+_+!c|<3+_y0")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `Failed to list the ticket(s); no special characters allowed`
        self.assert_text('Failed to list the ticket(s): The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.1.6 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the
    # first or the last character. [fail due to tail white space and special characters]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_fail_whitetail_special(self, *_):
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
        # enter '+35+_+!c|<3+_y0 	' into element `#sell_name`
        self.type("#sell-ticket-name", "+35+_+!c|<3+_y0 	")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `Failed to list the ticket(s); no white space at front or back, or special characters allowed`
        self.assert_text('Failed to list the ticket(s): The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.1.7 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the
    # first or the last character. [fail due to head white space and special characters]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_fail_whitehead_special(self, *_):
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
        # enter ' 	+35+_+!c|<3+_y0' into element `#sell_name`
        self.type("#sell-ticket-name", " 	+35+_+!c|<3+_y0")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `Failed to list the ticket(s); no white space at front or back, or special characters allowed`
        self.assert_text('Failed to list the ticket(s): The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.1.8 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the
    # first or the last character. [fail due to head and tail white space and special characters]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_fail_whiteboth_special(self, *_):
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
        # enter '	 +35+_+!c|<3+_y0 	' into element `#sell_name`
        self.type("#sell-ticket-name", "	 +35+_+!c|<3+_y0 	")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `Failed to list the ticket(s); no white space at front or back, or special characters allowed`
        self.assert_text('Failed to list the ticket(s): The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')


    # Test case R4.2.1 - The name of the ticket is no longer than 60 characters. [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_length_pass(self, *_):
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
        # enter '012345678901234567890123456789012345678901234567890123456789' into element `#sell_name`
        self.type("#sell-ticket-name", "012345678901234567890123456789012345678901234567890123456789")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully listed the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')


    # Test case R4.2.2 - The name of the ticket is no longer than 60 characters. [fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_length_fail(self, *_):
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
        # enter '0123456789012345678901234567890123456789012345678901234567890' into element `#sell_name`
        self.type("#sell-ticket-name", "0123456789012345678901234567890123456789012345678901234567890")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Failed to list the ticket(s): The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')


    # Test case R4.3.1 - The quantity of the tickets has to be more than 0, and less than or equal to 100. [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_quantity_pass(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully listed the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.3.2 - The quantity of the tickets has to be more than 0, and less than or equal to 100. The quantity of the tickets has to be more than 0, and less than or equal to 100. [pass - minimum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_quantity_pass(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter 1 into element `#sell_quantity`
        self.type("#sell-quantity", "1")
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully listed the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.3.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100. The quantity of the tickets has to be more than 0, and less than or equal to 100. [pass - maximum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_quantity_pass(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter 100 into element `#sell_quantity`
        self.type("#sell-quantity", "100")
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully listed the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.3.4 - The quantity of the tickets has to be more than 0, and less than or equal to 100. The quantity of the tickets has to be more than 0, and less than or equal to 100. [fail - below minimum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_quantity_fail_low(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter 0 into element `#sell_quantity`
        self.type("#sell-quantity", "0")
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to listed the ticket(s); quantity must be between 1 and 100`
        self.assert_text('Failed to list the ticket(s): You may only sell between 1 and 100 tickets at a time with SeetGeek.', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.3.5 - The quantity of the tickets has to be more than 0, and less than or equal to 100. The quantity of the tickets has to be more than 0, and less than or equal to 100. [fail - above maximum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_quantity_fail_high(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter 101 into element `#sell_quantity`
        self.type("#sell-quantity", "101")
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to listed the ticket(s); quantity must be between 1 and 100`
        self.assert_text('Failed to list the ticket(s): You may only sell between 1 and 100 tickets at a time with SeetGeek.', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.3.6 - The quantity of the tickets has to be more than 0, and less than or equal to 100. The quantity of the tickets has to be more than 0, and less than or equal to 100. [fail - non-numeric]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_quantity_fail_not_num(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter 101 into element `#sell_quantity`
        self.type("#sell-quantity", "101")
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to listed the ticket(s); quantity must be between 1 and 100`
        self.assert_text('Failed to list the ticket(s): You may only sell between 1 and 100 tickets at a time with SeetGeek.', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.4.1 - Price has to be of range [10, 100] [pass - minimum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_price_pass_low(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter `10` into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully listed the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.4.2 - Price has to be of range [10, 100] [pass - maximum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_price_pass_high(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter `100` into element `#sell_price`
        self.type("#sell-price", "100")
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully listed the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.4.3 - Price has to be of range [10, 100] [fail- below minimum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_price_fail_low(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter `-1` into element `#sell_price`
        self.type("#sell-price", "-1")
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", test_tickets[0].expiration)
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to listed the ticket(s); price must be between 10 and 100`
        self.assert_text('Failed to list the ticket(s): Prices must be between $10 and $100 (whole numbers only).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')


    # Test case R4.4.4 - Price has to be of range [10, 100] [fail- above maximum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_price_fail_high(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter `101` into element `#sell_price`
        self.type("#sell-price", "101")
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", test_tickets[0].expiration)
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to listed the ticket(s); price must be between 10 and 100`
        self.assert_text('Failed to list the ticket(s): Prices must be between $10 and $100 (whole numbers only).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.4.5 - Price has to be of range [10, 100] [fail- non-numeric]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_price_fail_nonnumeric(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter `abcdefg` into element `#sell_price`
        self.type("#sell-price", "abcdefg")
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", test_tickets[0].expiration)
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to listed the ticket(s); price must be between 10 and 100`
        self.assert_text('Failed to list the ticket(s): Prices must be between $10 and $100 (whole numbers only).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')


    # Test case R4.5.1 -Date must be given in the format YYYYMMDD (e.g. 20200901) [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_date_valid(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter `10` into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", "99991231")
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully listed the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.5.2 -Date must be given in the format YYYYMMDD (e.g. 20200901) [fail - seperators]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_date_fail_seperator(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter `10` into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter "9999.12.31" into element `#sell_date`
        self.type("#sell-expiration", "9999.12.31")
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to list the ticket(s); invalid date format please use YYYYMMDD`
        self.assert_text('Failed to list the ticket(s): Ticket cannot be expired and must conform to YYYYMMDD format', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.5.3 -Date must be given in the format YYYYMMDD (e.g. 20200901) [fail - YYYYDDMM]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_date_fail_format(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter `10` into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter "99993112" into element `#sell_date`
        self.type("#sell-expiration", "99993112")
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to list the ticket(s); invalid date format please use YYYYMMDD`
        self.assert_text('Failed to list the ticket(s): Ticket cannot be expired and must conform to YYYYMMDD format', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.5.4 -Date must be given in the format YYYYMMDD (e.g. 20200901) [fail - non-numeric]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_date_fail_badchar(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", str(test_tickets[0].ticket_name))
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter `10` into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter "abcdefgh" into element `#sell_date`
        self.type("#sell-expiration", "abcdefgh")
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to list the ticket(s); invalid date format please use YYYYMMDD`
        self.assert_text('Failed to list the ticket(s): Ticket cannot be expired and must conform to YYYYMMDD format', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.6 - For any errors, redirect back to / and show an error message
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_general_error(self, *_):
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
        # enter `!@#$%^&*()_=` into element `#sell_name`
        self.type("#sell-ticket-name", "!@#$%^&*()_=")
        # enter `-1` quantity into element `#sell_quantity`
        self.type("#sell-quantity", "-1")
        # enter `9999` into element `#sell_price`
        self.type("#sell-price", "9999")
        # enter `202031012` into element `#sell_date`
        self.type("#sell-expiration", "202031012")
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element contains `failed to list the ticket(s);`
        self.assert_text('Failed to list the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.8.1 - The name of the ticket must be at least 6 characters long [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_short_pass(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", test_tickets[0].ticket_name)
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text('Successfully listed the ticket(s)', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    # Test case R4.8.2 - The name of the ticket must be at least 6 characters long [fail - blank]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_name_short_fail(self, *_):
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
        # enter "a" into element `#sell_name`
        self.type("#sell-ticket-name", "a")
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter test_ticket's date into element `#sell_date`
        self.type("#sell-expiration", str(test_tickets[0].expiration))
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `failed to list the ticket(s); name must be between 6 and 60 characters.`
        self.assert_text('Failed to list the ticket(s): The name of the ticket names must be longer than 6-characters, shorter than 60 characters, and be alpha-numeric with spaces (spaces are not allowed at the beginning or the end).', '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')


    # Test case R4.9 - The ticket(s) must not be expired
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_sell_expired_tickets(self, *_):
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
        # enter test_ticket's name into element `#sell_name`
        self.type("#sell-ticket-name", test_tickets[0].ticket_name)
        # enter test_ticket's quantity into element `#sell_quantity`
        self.type("#sell-quantity", str(test_tickets[0].quantity))
        # enter test_ticket's price into element `#sell_price`
        self.type("#sell-price", str(test_tickets[0].price))
        # enter "19700101" into element `#sell_date`
        self.type("#sell-expiration", "19700101")
        # click `#sell_submit`.
        self.click('#sell-submit')
        # validate that the `#sell_message` element shows `successfully listed the ticket(s)`
        self.assert_text("Failed to list the ticket(s): Ticket cannot be expired and must conform to YYYYMMDD format.", '#sell_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')
