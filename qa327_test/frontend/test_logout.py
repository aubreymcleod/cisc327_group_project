import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend logout page.
These tests were implemented by Teaghan Laitar (20101224)

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.library.users.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return returns the test user.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='Test_frontend',
    password=generate_password_hash('Test_frontend'),
    balance=500000
)

'''
This class tests the R7 requirements
This tests all items pertaining to the logout page
'''
class FrontEndR7(BaseCase):
    ## Test case R7.1.1 - Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_logout_no_access(self, *_):
        self.open(base_url + '/logout')                 ## Invalidate any past sessions
        self.open(base_url + '/login')                  ## Go to the log in page
        self.type("#email", "test_frontend@test.com")   ## Enter a valid email
        self.type("#password", "Test_frontend")         ## Enter a valid password
        self.click('input[type="submit"]')              ## Submit the form
        self.open(base_url + '/logout')                 ## Go to the logout page
        self.assert_element ('#log-in-header')          ## Check that you are redirected to the login page
        self.open(base_url + '/buy')                    ## Go to the buy page
        self.assert_element ('#log-in-header')          ## Check that you are redirected to the login page
        self.open(base_url + '/update')                 ## Go to the update page
        self.assert_element ('#log-in-header')          ## Check that you are redirected to the login page
        self.open(base_url + '/sell')                   ## Go to the sell page
        self.assert_element ('#log-in-header')          ## Check that you are redirected to the login page
        self.open(base_url + '/')                       ## Go to the base page
        self.assert_element ('#log-in-header')          ## Check that you are redirected to the login page
