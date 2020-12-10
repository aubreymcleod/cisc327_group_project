import pytest
from seleniumbase import BaseCase
from flask_sqlalchemy import SQLAlchemy

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import User, Ticket
from werkzeug.security import generate_password_hash

"""
This file defines all unit tests for the frontend update ticket route.
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



class FrontEndUpdateTest(BaseCase):
    #Test case R5.4.1 - price has to be in the range [10, 100] (pass minimum)
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_price_minRange(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter '10' into element '#update-price'
        self.type("#update-price", '10')
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the `#update_message` element shows 'successfully listed the ticket(s)'
        self.assert_text('Successfully updated the ticket(s)', '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')
        

    #Test case R5.4.2 - price has to be in the range [10, 100] (pass maximum)
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_price_maxRange(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter '100' into element '#update-price'
        self.type("#update-price", '100')
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows 'successfully listed the ticket(s)'
        self.assert_text('Successfully updated the ticket(s)', '#update_message')
        # open `/logout` (clean up)
        self.open(base_url + '/logout')

    #Test case R5.4.3 - price has to be in the range [10, 100] (fail minimum)
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_price_underMin(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter '9' into element '#update-price'
        self.type("#update-price", '9')
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Prices must be between $10 and $100 (whole numbers only) and cannot be blank", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.4.4 - price has to be in the range [10, 100] (fail maximum)
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_price_overMax(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter 101 into element '#update-price'
        self.type("#update-price", '101')
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Prices must be between $10 and $100 (whole numbers only) and cannot be blank", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.4.5 - price has to be in the range [10, 100] (fail non-numeric)
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_price_nonNumeric(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter 'abc' into element '#update-price'
        self.type("#update-price", 'abc')
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Prices must be between $10 and $100 (whole numbers only) and cannot be blank", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.4.6 - price has to be in the range [10, 100] (blank fail)
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_price_blank(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter '' into element '#update-price'
        self.type("#update-price", '')
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Prices must be between $10 and $100 (whole numbers only) and cannot be blank", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.5.1 - date must be given in the format YYYYMMDD [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_date_correctFormat(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element '#update-price'
        self.type("#update-price", str(test_ticket.price))
        # enter '19990802' into element '#update-expiration'
        self.type("#update-expiration", '19990802'))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows 'successfully listed the ticket(s)'
        self.assert_text('Successfully updated the ticket(s)', '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.5.2 - date must be given in the format YYYYMMDD [fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_date_incorrectFormat(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element '#update-price'
        self.type("#update-price", str(test_ticket.price))
        # enter '199908021' into element '#update-expiration'
        self.type("#update-expiration", '199908021'))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Date must be in the format YYYYMMDD, no separators and cannot be blank", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.5.3 - date must be given in the format YYYYMMDD [fail non-numeric]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_date_nonNumeric(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element '#update-price'
        self.type("#update-price", str(test_ticket.price))
        # enter 'abc' into element '#update-expiration'
        self.type("#update-expiration", 'abc'))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Date must be in the format YYYYMMDD, no separators and cannot be blank", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.5.4 - date must be given in the format YYYYMMDD [blank fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_date_blank(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element '#update-price'
        self.type("#update-price", str(test_ticket.price))
        # enter '' into element '#update-expiration'
        self.type("#update-expiration", ''))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Date must be in the format YYYYMMDD, no separators and cannot be blank", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.5.5 - date must be given in the format YYYYMMDD [fail separators]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_date_separators(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element '#update-price'
        self.type("#update-price", str(test_ticket.price))
        # enter '1999.08.02' into element '#update-expiration'
        self.type("#update-expiration", '1999.08.02'))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Date must be in the format YYYYMMDD, no separators and cannot be blank", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.6.1 - ticket of the given name must exist [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_ticket_exists(self, *_):
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
        # enter test_ticket's name into element '#update-ticket-name'
        self.type("#update-ticket-name", test_ticket.ticket_name)
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element '#update-price'
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the `#update_message` element shows 'successfully listed the ticket(s)'
        self.assert_text('Successfully updated the ticket(s)', '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.6.2 - ticket of the given name must exist [fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_ticket_doesNotExist(self, *_):
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
        # enter 'abcdef' into element '#update-ticket-name'
        self.type("#update-ticket-name", 'abcdef')
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element '#update-price'
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Ticket not found. The name of the ticket cannot be: blank, contain more than 60 characters, contain special characters, contain only numbers, or any white space", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.6.3 - ticket of the given name must exist [fail numeric]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_ticket_numeric(self, *_):
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
        # enter '1234' into element '#update-ticket-name'
        self.type("#update-ticket-name", '1234')
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element '#update-price'
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Ticket not found. The name of the ticket cannot be: blank, contain more than 60 characters, contain special characters, contain only numbers, or any white space", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.6.4 - ticket of the given name must exist [blank fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_ticket_blank(self, *_):
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
        # enter '' into element '#update-ticket-name'
        self.type("#update-ticket-name", '')
        # enter test_ticket's quantity into element '#update-quantity'
        self.type("#update-quantity", str(test_ticket.quantity))
        # enter test_ticket's price into element '#update-price'
        self.type("#update-price", str(test_ticket.price))
        # enter test_ticket's date into element '#update-expiration'
        self.type("#update-expiration", str(test_ticket.expiration))
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text("Ticket not found. The name of the ticket cannot be: blank, contain more than 60 characters, contain special characters, contain only numbers, or any white space", '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')

    #Test case R5.7.1 - for any errors, redirect back to / and show an error message
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.update_ticket', return_value=None)
    def test_update_general_error(self, *_):
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
        # enter '' into element '#update-ticket-name'
        self.type("#update-ticket-name", '')
        # enter 0 into element '#update-quantity'
        self.type("#update-quantity", '0')
        # enter 9 into element '#update-price'
        self.type("#update-price", '9')
        # enter '1999.08.02' into element '#update-expiration'
        self.type("#update-expiration", '1999.08.02')
        # click '#update-submit'
        self.click('#update-submit')
        # validate that the '#update_message' element shows failure message
        self.assert_text('Failed to update ticket', '#update_message')
        # open '/logout' (clean up)
        self.open(base_url + '/logout')















