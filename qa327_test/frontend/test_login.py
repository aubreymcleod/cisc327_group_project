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

# Moch a sample user with an invalid email address
test_user_bad1 = User(
    email='test..frontend@test.com',
    name='Test_frontend',
    password=generate_password_hash('Test_frontend'),
    balance=500000
)

# Moch a sample user with a quoted email address
test_user_special = User(
    email='"test..frontend"@test.com',
    name='Test_frontend',
    password=generate_password_hash('Test_frontend'),
    balance=500000
)

# Moch a sample user with an invalid quoted email address
test_user_special_bad = User(
    email='"test..frontend\\"@test.com',
    name='Test_frontend',
    password=generate_password_hash('Test_frontend'),
    balance=500000
)

# Moch a sample user with an inadequate password
test_user_bad_pass = User(
    email='test_frontend@test.com',
    name='Test_frontend',
    password=generate_password_hash('testfrontend'),
    balance=500000
)

# Moch a sample user with an inadequate password and an inadequate email
test_user_bad_both = User(
    email='"test_frontend\\"@test.com',
    name='Test_frontend',
    password=generate_password_hash('testfrontend'),
    balance=500000
)

class FrontEndLoginPageTest(BaseCase):
    ### Test case R1.1 - If the user hasn't logged in, show the login page.
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_page_no_session(self, *_):
        """
        If the user has not logged in and attempts to access the "/login" route,
         they should remain on the "/login" route.
        """
        #open /logout to invalidate the current session
        self.open(base_url+'/logout')
        #open /login
        self.open(base_url+'/login')
        #validate that current page contains the #log-in-header element
        self.assert_element('#log-in-header')


    ### Test case R1.2 - The login page has a message that by default says “please login”
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_banner_exists(self, *_):
        """
        If the user has not logged in and attempts to access the "/login" route,
        they should be able to see the login header, and the header should say "please log in"
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # validate that current page contains the #log-in-header element
        self.assert_element('#message')
        # validate that the #log-in-header element says "please login"
        self.assert_text('Please login', '#message')

    ### Test case R1.3 - If the user has logged in, redirect to the user profile page
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_page_with_session(self, *_):
        """
        If the user has logged in and attempts to access the "/login" route,
        they should be directed to the home page.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open "/login" again
        self.open(base_url + '/login')
        # validate that current page contains #welcome-header element
        self.assert_element("#welcome-header")


    ### Test case R1.4 - The login page provides a login form which requests two fields: email and password
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_contents(self, *_):
        """
        If the user has not logged in and attempts to access the "/login" route,
        the login route should provide the user with an email field and a password field.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # validate that the email field exists
        self.assert_element('#email')
        # validate that the password field exists
        self.assert_element('#password')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # open "/login" again
        self.open(base_url + '/login')
        # validate that current page contains #welcome-header element
        self.assert_element("#welcome-header")

    ### Test case R1.5 - The login form can be submitted as a POST request to the current URL (/login)
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_page_submission(self, *_):
        """
        If the user has not logged in and attempts to access the "/login" route,
        they should be presented with a login form that can be submitted through post request
        and redirect the user to the home page.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # test to make sure we were redirected
        self.assert_element("#welcome-header")

    ### Test case R1.6.1 - Email and password both cannot be empty (check populated)
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_field_full(self, *_):
        """
        If the user enters valid username and password, then the form can be submitted.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # test to make sure we were redirected
        self.assert_element("#welcome-header")

    ### Test case R1.6.2 - Email and password both cannot be empty (check fail)
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_field_empty(self, *_):
        """
        Test to see if the fields on the UI can be submitted while empty
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.get_attribute("#email", "required")
        # enter test_user’s password into element #password
        self.get_attribute("#password", "required")

    ### Test case R1.6.3 - Email and password both cannot be empty (check external post request)
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_post_empty(self, *_):
        """
        Test to see if an empty post request will redirect away from login
        """
        r=requests.post(base_url+'/login', {'email':'', 'password':''})
        assert not r.is_redirect


    ### Test case R1.7.1 - Email has to follow addr-spec defined in RFC 5322, normal form
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_email_normal(self, *_):
        """
        Test to see if a correctly formatted email address will allow the user to
        Log in without issue
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test_frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # test to make sure we were redirected
        self.assert_element("#welcome-header")

    ### Test case R1.7.2 - Email has to follow addr-spec defined in RFC 5322, bad normal form
    @patch('qa327.library.users.get_user', return_value=test_user_bad1)
    def test_login_email_bad(self, *_):
        """
        Test to see if an invalid email address fails to post.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", "test..frontend@test.com")
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # validate that current page is /login again with error message
        self.assert_text("email/password format is incorrect.", '#message')

    ### Test case R1.7.3 - Email has to follow addr-spec defined in RFC 5322,in quoted form
    @patch('qa327.library.users.get_user', return_value=test_user_special)
    def test_login_email_quoted(self, *_):
        """
        Test to see if a user can succesfully submit while their email is of the special quoted case.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", '"test..frontend"@test.com')
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # validate that current page is /login again with error message
        self.assert_element("#welcome-header")


    ### Test case R1.7.4 - Email has to follow addr-spec defined in RFC 5322,in invalid quoted form
    @patch('qa327.library.users.get_user', return_value=test_user_special_bad)
    def test_login_email_quoted_bad(self, *_):
        """
        test to see if an incorrectly formatted quoted email fails to submit.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", '"test..frontend\\"@test.com')
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # validate that current page is /login again with error message
        self.assert_text("email/password format is incorrect.", '#message')

    ### Test case R1.8.1 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_password_valid(self, *_):
        """
        test to see if a correctly formatted password can be submitted.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # validate that current page is "/"
        self.assert_element("#welcome-header")

    ### Test case R1.8.2 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
    @patch('qa327.library.users.get_user', return_value=test_user_bad_pass)
    def test_login_password_invalid(self, *_):
        """
        Test to see if an incorrectly formatted password fails to submit.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter test_user’s password into element #password
        self.type("#password", "testfrontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # validate that current page is /login again with error message
        self.assert_text("email/password format is incorrect.", '#message')

    ### Test case R1.9 - For any formatting errors, render the login page and show the message “email/password format is incorrect.”
    @patch('qa327.library.users.get_user', return_value=test_user_bad_both)
    def test_login_formatting_error(self, *_):
        """
        Test to ensure that a bad email/password will cause an error to be displayed
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", '"test_frontend\"@test.com')
        # enter test_user’s password into element #password
        self.type("#password", "testfrontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # validate that current page is /login again with error message
        self.assert_text("email/password format is incorrect.", '#message')

    ### Test case R1.10 - If email/password are correct, redirect to /
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_endpoint_test(self, *_):
        """
        Test to see if a correctly submitted form redirects the user to home.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter test_user’s password into element #password
        self.type("#password", "Test_frontend")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # validate that current page is "/"
        self.assert_element("#welcome-header")

    ### Test case R1.11 - If email/password is not correct, redirect to /login and show message “email/password combination incorrect”
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_login_invalid(self, *_):
        """
        Test to see if an incorrectly submitted form redirects back to the login page.
        """
        # open /logout to invalidate the current session
        self.open(base_url + '/logout')
        # open /login
        self.open(base_url + '/login')
        # enter the test_user's email into #email
        self.type("#email", 'test_frontend@test.com')
        # enter not test_user’s password into element #password
        self.type("#password", "Wrong_password")
        # click element input[type=“submit”]
        self.click('input[type="submit"]')
        # validate that current page is "/"
        self.assert_element("#log-in-header")