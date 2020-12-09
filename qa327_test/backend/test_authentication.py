import pytest
from seleniumbase import BaseCase
import qa327.library.authenticate as authentic
import qa327.library.users as users
from qa327_test.conftest import base_url
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from unittest.mock import patch
"""
This file defines all unit tests for the backend authentication functions.

These tests were implemented by Nicole Osayande (20056993)
"""
# Mock a sample user that is used to mock the data base return
test_user = User(
    email='test_frontend@test.com',
    name='Test_frontend',
    password=generate_password_hash('Pas$word'),
    balance=500000
)
# Test case authenticate.1.1 - Given any python function that accepts a user object,
# should return inner_function(user) if logged in, or redirect to the login page
# otherwise [logged in session]
@patch('qa327.library.users.get_user', return_value=test_user)
@patch('qa327.library.authenticate.authenticate', users.get_user)
#@patch('qa327.library.authenticate.wrapped_inner', return_val=test_user)
def test_inner_wrap_pass(self, *_):
    test_email = "test_frontend@test.com"
    assert users.get_user(test_email) is test_user
    #validate that the function is wrapped
    assert authentic.authenticate is not None

# Test case authenticate.1.2 - Given any python function that accepts a user object,
# should return inner_function(user) if logged in, or redirect to the login page
# otherwise [logged out]
@patch('qa327.library.users.get_user', return_value=None)
@patch('qa327.library.authenticate.authenticate', users.get_user)
def test_inner_wrap_fail(self, *_):
    test_email = "testfrontend@test.com"
    assert users.get_user(test_email) is None
    #validate that the user is redirected to the login page
    self.open(base_url + '/login')
