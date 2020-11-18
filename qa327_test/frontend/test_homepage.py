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

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='Test_frontend',
    password=generate_password_hash('Test_frontend'),
    balance=500000
)

# Moch some sample tickets
test_ticket1 = [Ticket(
ticket_name='test_ticket_yo',
price=10,
quantity=10,
expiration='2020/12/31',
owners_email='test_frontend@test.com'
)]

test_ticket2 = [Ticket(
ticket_name='test_ticket_yo',
price=10,
quantity=10,
expiration='2020/12/31',
owners_email='test_frontend@test.com'
)]

class FrontEndHomePageTest(BaseCase):
    ### Test case R3.1.1/ R3.1.2 - If the user is not logged in, redirect to login page
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_redirect_login(self, *_):
        """
        Test to see if a user is not logged in, redirects back to the login page.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /
        self.open(base_url + '/')
        # validate that current page is "/login"
        self.assert_element("#log-in-header")
        

    ### Test case R3.2 - This page shows a header 'Hi {}'.format(user.name)
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_check_header(self, *_):
        """
        Test to see if page shows header "Hi Username".
        """
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
        # validate that current page contains the #greeting header element
        self.assert_element('#welcome-header')
        # validate that the #greeting header element says "Hi Username"
        self.assert_text('Hi Test_frontend', '#welcome-header')
        # open /logout (clean up)
        self.open(base_url + '/logout')

    ### Test case R3.3 - This page shows user balance
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_user_balance(self, *_):
        """
        Test to see if page shoes user balance.
        """
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
        # validate that the #user_balance element says "Your current balance is 5000.0"
        self.assert_text('Your balance is 5000.0', '#user-balance')
        # open /logout (clean up)
        self.open(base_url + '/logout')

    ###****** Test case R3.4 - This page shows logout link
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_logout_link(self, *_):
        """
        Test to see if page shows logout link.
        """
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
        # validate that the '#logout' element exists
        self.assert_element('#logout')
        # validate that the '#logout' element makes a '[GET] request' to '/logout'
        #self.get(base_url + '/logout')
        # click element '#logout'
        #link=self.get_attribute('#logout', 'href')
        #assert link=='/logout'
        self.click('a[rel="/logout"]')
        # validate that the current page is '/login'
        self.open(base_url + '/login')
        # open /
        self.open(base_url + '/')
        # validate that the current page is '/login'
        self.open(base_url + '/login')
        # open /logout (clean up)
        self.open(base_url + '/logout')
    '''
    ### Test case R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_available_tickets(self, *_):
        """
        Test to see if page lists all available tickets.
        """
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
        
        # validate that the `#tickets` element contains 2 child element.
        #self.assert_text('')
        # validate that the `#ticket1_owner` element shows `test_frontend@test.com`.
        self.assert_text('','#')
        # validate that the `#ticket2_owner` element shows `test_frontend@test.com`.
        
        # validate that the `#ticket1_name` element shows `test_ticket_yo`.
        
        # validate that the `#ticket2_name` element shows `test_ticket_yo`.
        
        # validate that the `#ticket1_price` element shows `10`.
        
        # validate that the `#ticket2_price` element shows `10`.
        # validate that the `#ticket1_quantity` element shows `10`.
        # validate that the `#ticket2_quantity` element shows `10`.
        # validate that the `#ticket1_date` element shows `20201231`.
        # validate that the `#ticket2_date` element shows `20201231`.

        # open /logout (clean up)
        self.open(base_url + '/logout')


    ### Test case R3.6 - This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date.
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_sell_form(self, *_):
        """
        Test to see if page contains a form for user to submit tickets to sell.
        """
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
        # validate that the '#sell_form' element exists.
        self.assert_text('Sell Ticket', '#sell-ticket')
        # validate that the '#sell_name' element exists.
        self.assert_text('ticket_name', '#ticket_name')
        # validate that the '#sell_quantity' element exists.

        # validate that the '#sell_price' element exists.

        # validate that the '#sell_date' element exists.

        # validate that the '#sell_submit' element exists.

        # validate that the '#sell_submit' element makes a post request to '/sell' on submission.
        
        # open /logout (clean up)
        self.open(base_url + '/logout')
    '''

