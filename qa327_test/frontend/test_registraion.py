import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

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


'''
# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='Test_frontend',
    password=generate_password_hash('Test_frontend'),
    balance=500000
)

# Moch some sample tickets
test_tickets = [Ticket(
ticket_name='t1',
price=100,
quantity=1,
expiration='9999/12/31',
owners_email='test_frontend@test.com'
)]


class FrontEndHomePageTest(BaseCase):

    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.get_all_tickets', return_value=test_tickets)
    def test_login_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Test_frontend")
        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Hi Test_frontend", "#welcome-header")
        self.assert_element("#tickets div h4")
        self.assert_text("(x1) t1 $100 Sold By: test_frontend@test.com", "#tickets div h4")

    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.get_all_tickets', return_value=test_tickets)
    def test_login_password_failed(self, *_):
        """ Login and verify if the tickets are correctly listed."""
        # open login page
        self.open(base_url + '/login')
        # fill wrong email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "Wrong_password")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text('email/password combination incorrect', "#message")
    '''