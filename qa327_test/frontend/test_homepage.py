import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
import requests

"""
This file defines all unit tests for the frontend homepage.
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

# Mock a sample ticket
test_ticket = Ticket(
     owners_email='test_frontend@test.com',
     ticket_name='ticket_two',
     quantity=22,
     price=30,
     expiration=20210617
)
     

class FrontEndHomePageTest(BaseCase):
    ### Test case R3.9.2 - Check to ensure that when the sell form is filled out incorrectly, a failure post response is returned
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=test_ticket)
    def test_incorrect_sell_form(self, *_):
        # open /logout to invalidate any logged-in sessions that may exist
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open "/" again
        self.open(base_url + '/')
        self.type("#sell-ticket-name", "!@#$%^&*()-=")
        self.type("#sell-quantity", "10000000")
        self.type("#sell-price","-10")
        self.type("#sell-expiration", "19700101")
        self.click('#sell-submit')
        self.assert_element('#sell_message')
        ### clean up
        self.open(base_url + '/logout')

    ### Test case R3.10.1 - The ticket-buying form can be posted to /buy. [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_buy_form(self, *_):
        # open /logout to invalidate any logged-in sessions that may exist
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open "/" again
        self.open(base_url + '/')
        self.type("#buy-ticket-name", "ticket_two")
        self.type("#buy-quantity", "10")
        self.click("#buy-submit")
        self.assert_text("successfully bought ticket(s)", '#buy_message')
        ### clean up
        self.open(base_url + '/logout')
        
    ### Test case R3.10.2 - The ticket-buying form can be posted to /buy. [fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=test_ticket)
    def test_incorrect_buy_form(self, *_):
        # open /logout to invalidate any logged-in sessions that may exist
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open "/" again
        self.open(base_url + '/')
        self.type("#buy-ticket-name", "!@#$%^&*()-=")
        self.type("#buy-quantity", "-1")
        self.click("#buy-submit")
        self.assert_text("failed to buy ticket(s)", '#buy_message')
        ### clean up
        self.open(base_url + '/logout')

    ### Test case R3.11.1 - The ticket-update form can be posted to /update. [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=None)
    def test_update_form(self, *_):
          # open /logout to invalidate any logged-in sessions that may exist
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open "/" again
        self.open(base_url + '/')
        self.type("#update-ticket-name", "ticket_two")
        self.type("#update-quantity", "11")
        self.type("#update-price", "11")
        self.type("#update-expiration", "20210101")
        self.click("#update-submit")
        self.assert_text("successfully updated ticket listing", '#update_message')
        ### clean up
        self.open(base_url + '/logout')
        
    ### Test case R3.11.2 - The ticket-update form can be posted to /update. [fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.add_ticket', return_value=test_ticket)
    def test_incorrect_update_form(self, *_):
        # open /logout to invalidate any logged-in sessions that may exist
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open "/" again
        self.open(base_url + '/')
        self.type("#update-ticket-name", "ticket_two")
        self.type("#update-quantity", "-1")
        self.type("#update-price", "-1")
        self.type("#update-expiration", "19700101")
        self.click("#update-submit")
        self.assert_text("failed to update ticket", '#update_message')
        ### clean up
        self.open(base_url + '/logout')


