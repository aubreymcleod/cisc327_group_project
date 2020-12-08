import pytest
from seleniumbase import BaseCase
import qa327.library.users as users
from qa327_test.conftest import base_url
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from unittest.mock import patch

"""
This file defines all unit tests for the backend user class.
These tests were implemented by Teaghan Laitar (20101224)

Patching will be used for calls to the database.
"""

# Mock a sample user that is used to mock the data base return
test_user = User(
    email='test_frontend@test.com',
    name='Test_frontend',
    password=generate_password_hash('Pas$word'),
    balance=500000
)

## Test the get_User function for a valid user
@patch('qa327.library.users.get_user', return_value=test_user)
def test_user_get_user_valid(self, *_):
    test_email = "test_frontend@test.com"           ## Create the test email
    assert users.get_user(test_email) is test_user  ## Validate that get user returns the user

## Test the gut_user function for an invalid user
@patch('qa327.library.users.get_user', return_value=None)
def test_user_get_user_invalid(self, *_):
    test_email = "testfrontend@test.com"            ## Test a non existant email
    assert users.get_user(test_email) is None       ## Validate that get user returns None

## Test the login_user for a valid login
@patch('qa327.library.users.get_user', return_value=test_user)
def test_user_login_user_valid(self, *_):
    test_email = "test_frontend@test.com"                           ## Test an existing email
    test_password = "Pas$word"                                      ## Test an existing password
    assert users.login_user(test_email, test_password) is test_user ## Run  login user and check that the user is returned

## Test the login_user wirh an invalid password
@patch('qa327.library.users.get_user', return_value=test_user)
def test_user_login_user_invalid_password(self, *_):
    test_email = "test_frontend@test.com"                           ## Test an existing email
    test_password = "Pa$sword"                                      ## Test an incorrect password
    assert users.login_user(test_email, test_password) is None      ## Run login user and check that None is returned

## Test the login_user with an invalid email
@patch('qa327.library.users.get_user', return_value=None)
def test_user_login_user_invalid_email(self, *_):
    test_email = "testfrontend@test.com"                            ## Test a non existing email
    test_password = "Pas$word"                                      ## Test a password
    assert users.login_user(test_email, test_password) is None      ## Run login user and check that None is returned

## Test the register_user with valid credentials
@patch('qa327.models.db.session.add', return_value=None)
@patch('qa327.models.db.session.commit', return_value=None)
def test_user_register_user_valid(self, *_): 
    test_email = "testfrontend@test.com"                                ## Test with valid email
    test_name = "Backend Tester"                                        ## Test with valid name
    test_password = "Pa$sword"                                          ## Test with valid password
    test_password2 = "Pa$sword"                                         ## Test with valid password2
    test_balance  = "50000"                                             ## Test with valid balance
    assert users.register_user(test_email, test_name, test_password,
                         test_password2, test_balance) is None          ## Run register and make sure it returns None

## Test the register_user with error in session.add
@patch('qa327.models.db.session.add', side_effect=Exception('mocked error'))
@patch('qa327.models.db.session.commit', return_value=-1)
def test_user_register_user_invalid_add(self, *_): 
    test_email = "testfrontend@test.com"                                ## Test with valid email
    test_name = "Backend Tester"                                        ## Test with valid name
    test_password = "Pa$sword"                                          ## Test with valid password
    test_password2 = "Pa$sword"                                         ## Test with valid password2
    test_balance  = 50000                                               ## Test with valid balance
    assert users.register_user(test_email, test_name, test_password,
                         test_password2, test_balance) == 'error'       ## Run register and make sure it returns an error message

## Test the register_user with error in session.commit
@patch('qa327.models.db.session.add', side_effect=-1)
@patch('qa327.models.db.session.commit', return_value=Exception('mocked error'))
def test_user_register_user_invalid_commit(self, *_): 
    test_email = "testfrontend@test.com"                                ## Test with valid email
    test_name = "Backend Tester"                                        ## Test with valid name
    test_password = "Pa$sword"                                          ## Test with valid password
    test_password2 = "Pa$sword"                                         ## Test with valid password2
    test_balance  = 50000                                               ## Test with valid balance
    assert users.register_user(test_email, test_name, test_password,
                         test_password2, test_balance) == 'error'       ## Run register and make sure it returns an error message
    
## Test the reduce_user success
@patch('qa327.library.users.get_user', return_value=test_user)
@patch('qa327.models.db.session.commit', return_value=None)
def test_user_reduce_balance_success(self, *_):
    test_email = "testfrontend@test.com"                            ## Set tetst email
    test_cost = 10                                                  ## Set test cost
    assert users.reduce_balance(test_email, test_cost) == None      ## Run the reduce balance to make sure it works
