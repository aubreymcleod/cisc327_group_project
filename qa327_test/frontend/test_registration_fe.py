import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend registration page.
The cases have been brocken up into smaller class for easy of testing.
These tests were implemented by Teaghan Laitar (20101224)

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.library.users.register_user', return_value = None)

Will patch the backend register_user function (within the scope of the current test case)
so that it return returns nothing rather than storing the new user in the database.

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
Test case for R2.1, R2.2, and R2.3
Tests for redirection if logged in, not redirected if not logged in, and the form being displayed 
'''
class FrontEndR2_1_2_3(BaseCase):

    ## Test case R2.1.1 - If the user has logged in, redirect back to the user profile page [user is logged in]
    @patch('qa327.library.users.register_user', return_value = None)
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_register_logged_in_redirect(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/register')               ## Try to go to register page
        self.assert_element("#welcome-header")          ## Validate that the welcome header is present

    ## Test case R2.2.1 - Otherwise show the user registration page [user is not logged in]
    @patch('qa327.library.users.register_user', return_value = None)
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_register_not_logged_in(self, *_):
        self.open(base_url + '/logout')                 ## Invalidate any current sessions
        self.open(base_url + '/register')               ## Open register
        self.assert_element('#message')                 ## Check for register message

    ## Test case R2.3.1 - the registration page shows a registration form requesting: email, user name, password, password2
    @patch('qa327.library.users.register_user', return_value = None)
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_register_validate_form(self, *_):
        self.open(base_url + '/logout')                 ## Invalidate any current sessions
        self.open(base_url + '/register')               ## Open register page
        self.assert_element('#email')                   ## Check for email element
        self.assert_element('#name')                    ## Check for name element
        self.assert_element('#password')                ## Check for password element
        self.assert_element('#password2')               ## Check for password2 element

       
'''
Test case for R2.4
Validates the submission of a POST request.
'''
class FrontEndR2_4(BaseCase):
    ## Test case R2.4.1 - The registration form can be submitted as a POST request to the current URL (/register)
    @patch('qa327.library.users.register_user', return_value = None)
    def test_register_form_submission(self, *_):
        self.open(base_url + '/logout')                 # Invalidate any current session
        self.open(base_url + '/register')               # Open register page
        self.type("#email", "test_frontend@test.com")   # Enter email
        self.type("#name", "Test Frontend")             # Enter name
        self.type("#password", "Pas$word")              # Enter password
        self.type("#password2", "Pas$word")             # Enter password 2
        self.click('input[type="submit"]')              # Submit
        self.assert_element('#log-in-header')           # Validate the submission


'''
Test case for R2.5
Validate that the email and password meet requirements from R1
'''
class FrontEndR2_5(BaseCase):

    ## Test case R2.5.1 - Email, password, password2 all have to satisfy the same required as defined in R1 [all pass]
    @patch('qa327.library.users.register_user', return_value = None)
    def test_register_email_valid_pass(self, *_,):
        self.open(base_url + '/logout')                             ## Invalidate any current session
        self.open(base_url + '/register')                           ## Go to register page
        self.type("#email", "test_frontend@test.com")               ## Enter valid email
        self.type("#name", "Test Frontend")                         ## Enter valid name
        self.type("#password", "Pas$word")                          ## Enter valid password
        self.type("#password2", "Pas$word")                         ## Enter valid password2
        self.click('input[type="submit"]')                          ## Submit the form
        self.assert_element('#log-in-header')                       ## Check that the log in header is visable

    ## Test case R2.5.2 - Email, password, password2 all have to satisfy the same required as defined in R1 [email fails]
    @patch('qa327.library.users.register_user', return_value = None)
    def test_register_email_valid_fail_with_email(self, *_,):
        self.open(base_url + '/logout')                             ## Invalidate any current session
        self.open(base_url + '/register')                           ## Go to register page
        self.type("#email", "test_frontendtest.com")                ## Enter invalid email
        self.type("#name", "Test Frontend")                         ## Enter valid name
        self.type("#password", "Pas$word")                          ## Enter valid password
        self.type("#password2", "Pas$word")                         ## Enter valid password2
        self.click('input[type="submit"]')                          ## Submit the form
        self.assert_text("Email format is incorrect", '#message')   ## Check the error message

    ## Test case R2.5.3 - Email, password, password2 all have to satisfy the same required as defined in R1 [password fails]
    @patch('qa327.library.users.register_user', return_value = None)
    def test_register_email_valid_fail_with_password(self, *_,):
        self.open(base_url + '/logout')                             ## Invalidate any current session
        self.open(base_url + '/register')                           ## Go to register page
        self.type("#email", "test_frontend@test.com")               ## Enter valid email
        self.type("#name", "Test Frontend")                         ## Enter valid name
        self.type("#password", "Password")                          ## Enter invalid password
        self.type("#password2", "Password")                         ## Enter invalid password2
        self.click('input[type="submit"]')                          ## Submit the form
        self.assert_text("Password format is incorrect", '#message')## Check the error message

    ## Test case R2.5.4 - Email, password, password2 all have to satisfy the same required as defined in R1 [password2 fails]
    @patch('qa327.library.users.register_user', return_value = None)
    def test_register_email_valid_fail_with_password2(self, *_,):
        self.open(base_url + '/logout')                             ## Invalidate any current session
        self.open(base_url + '/register')                           ## Go to register page
        self.type("#email", "test_frontend@test.com")               ## Enter valid email
        self.type("#name", "Test Frontend")                         ## Enter valid name
        self.type("#password", "Password")                          ## Enter invalid password
        self.type("#password2", "Password")                         ## Enter invalid password2
        self.click('input[type="submit"]')                          ## Submit the form
        self.assert_text("Password format is incorrect", '#message')## Check the error message


'''
Test case for R2.6 and R2.7
Validate that the email and password meet requirements from R1
'''
class FrontEndR2_6_7(BaseCase):

    ## Test case R2.6.1 - Password and password2 have to be exactly the same [pass]
    @patch('qa327.library.users.register_user', return_value = None)
    def test_register_password_match(self, *_,):
        self.open(base_url + '/logout')                             ## Invaldate any current session
        self.open(base_url + '/register')                           ## Go to register page
        self.type("#email", "test_frontend@test.com")               ## Enter valid email
        self.type("#name", "Test Frontend")                         ## Enter valid name
        self.type("#password", "Pas$word")                          ## Enter valid password
        self.type("#password2", "Pas$word")                         ## Enter valid password2
        self.click('input[type="submit"]')                          ## Submit the form
        self.assert_element('#log-in-header')                       ## Check that log in header is visable

    ## Test case R2.6.2 - Password and password2 have to be exactly the same [fail]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_password_not_match(self, *_):
        self.open(base_url + '/logout')                                     ## Invalidate any current session
        self.open(base_url + '/register')                                   ## Go to register page
        self.type("#email", "test_frontend@test.com")                       ## Enter valid email
        self.type("#name", "Test Frontend")                                 ## Enter valid name
        self.type("#password", "Pas$word")                                  ## Enter valid password
        self.type("#password2", "Pa$sword")                                 ## Enter valid password but different
        self.click('input[type="submit"]')                                  ## Submit form
        self.assert_text("The passwords format is incorrect", '#message')   ## Check error message

    ## Test case R2.7.1 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. [pass with space]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_pass_with_space(self, *_):
        self.open(base_url + '/logout')                 ## Invalidate any current session
        self.open(base_url + '/register')               ## Go to register page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email 
        self.type("#name", "Test Frontend")             ## Enter valid name with a space
        self.type("#password", "Pas$word")              ## Enter valid password
        self.type("#password2", "Pas$word")             ## Enter valid matching password
        self.click('input[type="submit"]')              ## Submit form
        self.assert_element('#log-in-header')           ## Check that the log in header is visable

    ## Test case R2.7.2 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. [pass without space]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_pass_without_space(self, *_):
        self.open(base_url + '/logout')                 ## Invalidate any current session
        self.open(base_url + '/register')               ## Go to register page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#name", "Testfrontend")              ## Enter valid name with a space
        self.type("#password", "Pas$word")
        self.type("#password2", "Pas$word")
        self.click('input[type="submit"]')              ## Submit form
        self.assert_element('#log-in-header')           ## Check that the log in header is visable

    ## Test case R2.7.3 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. [fail with non alphanumeric characters]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_with_nonalpha(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", "Test Frontend&")                            ## Enter invalid name with a character
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message

    ## Test case R2.7.4 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. [fail with space at begining]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_with_space_at_start(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", " Test Frontend")                            ## Enter invalid name with a space at start
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message

    ## Test case R2.7.5 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. [fail with space at end]
    @patch('qa327.library.users.register_user', return_value=None)    
    def test_register_username_fail_with_space_at_end(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", "Test Frontend ")                            ## Enter invalid name with a space at end
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message

    ## Test case R2.7.6 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. [fail with space at begining and end]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_with_space_at_start_and_end(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", " Test Frontend ")                           ## Enter invalid name with space at start and end
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message

    ## Test case R2.7.7 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. [fail with space at begining and end and special character]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_with_space_at_start_end_and_specical(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", " Test Fro&ntend ")                          ## Enter invalid name with a space at start and end and a special character
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message

    ## Test case R2.7.8 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. [fail with space at begining and special character]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_with_space_at_start_and_special(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", " Test Frontend&")                           ## Enter invalid name with space at front and special character 
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message

    ## Test case R2.7.9 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. [fail with space at end and special character]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_with_space_at_end_and_special(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", "&Test Frontend ")                           ## Enter invalid name with special character and space at end
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message


'''
Test case for R2.8
Validate the user name length follows specifications
'''
class FrontEndR2_8(BaseCase):

    ## Test case R2.8.1 - User name has to be longer than 2 characters and less than 20 characters. [pass]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_pass(self, *_):
        self.open(base_url + '/logout')                 ## Invalidate any current session
        self.open(base_url + '/register')               ## Go to register page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#name", "Test Frontend")             ## Enter valid name of correct length
        self.type("#password", "Pas$word")              ## Enter valid password
        self.type("#password2", "Pas$word")             ## Enter valid and matching passwordc
        self.click('input[type="submit"]')              ## Submit form
        self.assert_element('#log-in-header')           ## Check that the log in header is visable

    ## Test case R2.8.2 - User name has to be longer than 2 characters and less than 20 characters. [fail with 2 characters]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_length_2(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", "My")                                        ## Enter invalid name of boundary case 2
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message

    ## Test case R2.8.3 - User name has to be longer than 2 characters and less than 20 characters. [fail with 20 characters]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_length_20(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", "thisIsTwentyCharacte")                      ## Enter invalid name of boundary case 20
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message

    ## Test case R2.8.4 - User name has to be longer than 2 characters and less than 20 characters. [fail with less then 2 characters]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_length_less_2(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", "T")                                         ## Enter invalid name that has too few letters
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message

    ## Test case R2.8.5 - User name has to be longer than 2 characters and less than 20 characters. [fail with more then 20 characters]
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_username_fail_length_more_20(self, *_):
        self.open(base_url + '/logout')                                 ## Invalidate any current session
        self.open(base_url + '/register')                               ## Go to register page
        self.type("#email", "test_frontend@test.com")                   ## Enter valid email
        self.type("#name", "thisNotIsTwentyCharacters")                 ## Enter invalid name that has too many characters
        self.type("#password", "Pas$word")                              ## Enter valid password
        self.type("#password2", "Pas$word")                             ## Enter valid and matching password
        self.click('input[type="submit"]')                              ## Submit form
        self.assert_text("Username format is incorrect", '#message')    ## Check error message


'''
Test case for R2.9, R2.10, and R2.11
Validate the user name length follows specifications
'''
class FrontEndR2_9_10_11(BaseCase):
    ## Test case R2.9.1 - For any formatting errors, redirect back to /register and show message '{} format is incorrect.'.format(the_corresponding_attribute)
    @patch('qa327.library.users.register_user', return_value=None)
    def test_register_fail_place_check(self, *_):
        self.open(base_url + '/logout')                     ## Invalidate any current session
        self.open(base_url + '/register')                   ## Go to register page
        self.type("#email", "noatsign.com")                 ## Enter invalid email
        self.type("#name", "g&rg")                          ## Enter invalid name
        self.type("#password", "h ")                        ## Enter invalid password
        self.type("#password2", "p ")                       ## Enter invalid and non matching password
        self.click('input[type="submit"]')                  ## Submit form
        self.assert_element('#message')                     ## Check that on the registration page still
        assert '#message'.find("format is incorrect") != 0  ## Check that there is an error message

    ## Test case R2.10.1 - If the email already exists, show message 'this email has been ALREADY used' [email already used]
    @patch('qa327.library.users.register_user', return_value=None)
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_register_fail_used_email(self, *_):   
        self.open(base_url + '/logout')                                     ## Invalidate any current session
        self.open(base_url + '/register')                                   ## Go to register page
        self.type("#email", "test_frontend@test.com")                       ## Enter used email
        self.type("#name", "Test Frontend")                                 ## Enter valid username
        self.type("#password", "Pas$word")                                  ## Enter valid password
        self.type("#password2", "Pas$word")                                 ## Enter valid and matching password
        self.click('input[type="submit"]')                                  ## Submit form
        self.assert_text("This email has ALREADY been used", '#message')    ## Check error message

    ## Test case R2.11.1 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page [no errors in input]
    @patch('qa327.library.users.register_user', return_value=None)
    ##@patch('qa327.library.users.get_user', return_value=test_user)
    def test_register_success_check_location(self, *_):
        self.open(base_url + '/logout')                ## Invalidate any current session
        self.open(base_url + '/register')               ## Go to register page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email 
        self.type("#name", "Test Frontend")             ## Enter valid name with a space
        self.type("#password", "Pas$word")              ## Enter valid password
        self.type("#password2", "Pas$word")             ## Enter valid matching password
        self.click('input[type="submit"]')              ## Submit form
        self.assert_element('#log-in-header')           ## Check that the log in header is visable

    ## Test case R2.11.2 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page [no errors in input]
    @patch('qa327.library.users.get_user', return_value=test_user)
    def test_register_success_check_balance(self, *_):
        self.open(base_url + '/logout')                     ## Invalidate any current session
        self.open(base_url + '/login')                      ## Go to login page
        self.type("#email", "newTest_frontend@test.com")    ## Enter valid email
        self.type("#password", "Pas$word")                  ## Enter valid password
        self.click('input[type="submit"]')                  ## Submit form
        assert test_user.balance == 500000                  ## Check balance
