import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend buy ticket requirements.
The cases have been brocken up into smaller class for easy of testing.
These tests were implemented by Teaghan Laitar (20101224)

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.library.users.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it returns the test user rather than getting a user from the database.

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
The bellow class tests all the requirements for R6.1. This tests the validity of the ticket name entered in terms of the
characters used.
'''
class FrontEndR6_1(BaseCase):
    #Test case R6.1.1 - name of the ticket has to be alphanumeric-only, and space allowed on if it is not the first or the last character. [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_pass(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Sucessfully bought the ticket(s)", '#buy_message')    ## Check the success message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test case R6.1.2 - name of the ticket has to be alphanumeric-only, and space allowed on if it is not the first or the last character. [fail with space at tail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_fail_space_at_tail(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket ")    ## Enter invalid ticket name with space at the end
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("The name of the ticket must be no more than 60 characters", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test case R6.1.3 - name of the ticket has to be alphanumeric-only, and space allowed on if it is not the first or the last character. [fail with space at start]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_fail_space_at_head(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", " TestTicket")    ## Enter invalid ticket name with space at the begining
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("The name of the ticket must be no more than 60 characters", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test case R6.1.4 - name of the ticket has to be alphanumeric-only, and space allowed on if it is not the first or the last character. [fail with space at tail and head]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_fail_space_at_head_tail(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", " TestTicket ")   ## Enter invalid ticket name with spaces at the begining and end
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("The name of the ticket must be no more than 60 characters", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test case R6.1.5 - name of the ticket has to be alphanumeric-only, and space allowed on if it is not the first or the last character. [fail with special char]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_fail_special_char(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTick&t")     ## Enter invalid ticket name with special characters
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("The name of the ticket must be no more than 60 characters", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test case R6.1.6 - name of the ticket has to be alphanumeric-only, and space allowed on if it is not the first or the last character. [fail with special char and spac eat tail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_fail_special_char_tail_space(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTick&t ")    ## Enter invalid ticket name with special characters and space at the end
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("The name of the ticket must be no more than 60 characters", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test case R6.1.7 - name of the ticket has to be alphanumeric-only, and space allowed on if it is not the first or the last character. [fail with special char and space at head]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_fail_special_char_head_space(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", " TestTick&t")    ## Enter invalid ticket name with special characters and space at the begining
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("The name of the ticket must be no more than 60 characters", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test case R6.1.8 - name of the ticket has to be alphanumeric-only, and space allowed on if it is not the first or the last character. [fail with special char and space at head and tail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_fail_special_char_head_tail_space(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", " TestTick&t ")   ## Enter invalid ticket name with special characters and spaces the the begining and end
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("The name of the ticket must be no more than 60 characters", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

'''
The bellow class tests all the requirements for R6.2. This tests the validity of the ticket name entered in terms of the
length.
'''
class FrontEndR6_2(BaseCase):
    #Test Case R6.2.1 - name of the ticket is no longer than 60 characters and at least 6 [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_length_pass(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Sucessfully bought the ticket(s)", '#buy_message')    ## Check the success message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.2.2 - name of the ticket is no longer than 60 characters and at least 6 [failed too long]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_length_long_fail(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "ThisismorethensixtycharacterslongLikeitiswaytolongWhowouldevendothis")   ## Enter invalid ticket name with more then 60 characters
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("The name of the ticket must be no more than 60 characters", '#buy_message')           ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.2.3 - name of the ticket is no longer than 60 characters and at least 6 [failed too short]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_length_short_fail(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "Nopes")          ## Enter invalid ticket name with less then 6 characters
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("The name of the ticket must be no more than 60 characters", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.2.4 - name of the ticket is no longer than 60 characters and at least 6 [pass with length of 6]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_length_pass_with_6(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "SicCha")         ## Enter valid ticket
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Sucessfully bought the ticket(s)", '#buy_message')    ## Check the success message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.2.5 - name of the ticket is no longer than 60 characters and at least 6 [pass with length of 60]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_name_length_pass_with_60(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "SixtycharsSixtycharsSixtycharsSixtycharsSixtycharsSixtychars")         ## Enter valid ticket
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Sucessfully bought the ticket(s)", '#buy_message')    ## Check the success message
        self.open(base_url + '/logout')                 ## invalidate any current sessions


'''
The bellow class tests all the requirements for R6.3. This tests the validity of the quantity entered.
'''
class FrontEndR6_3(BaseCase):
    #Test Case R6.3.1 - quantity of the tickets has to be more than 0, and less than or equal to 100 [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_quantity_pass(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Sucessfully bought the ticket(s)", '#buy_message')    ## Check the success message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.3.2 - quantity of the tickets has to be more than 0, and less than or equal to 100 [pass minimum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_quantity_pass_min(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "1")                 ## Enter valid quantity on the boundary
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Sucessfully bought the ticket(s)", '#buy_message')    ## Check the success message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.3.3 - quantity of the tickets has to be more than 0, and less than or equal to 100 [fail minimum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_quantity_fail_min(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "-1")                ## Enter invalid quantity less then 1
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Quantity must be entered using 0-9", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.3.4 - quantity of the tickets has to be more than 0, and less than or equal to 100 [pass maximum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_quantity_pass_max(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "100")               ## Enter valid quantity on upper bound
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Sucessfully bought the ticket(s)", '#buy_message')    ## Check the success message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.3.5 - quantity of the tickets has to be more than 0, and less than or equal to 100 [fail maximum]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_quantity_fail_max(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "101")               ## Enter invalid quantity with greater then 100
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("You may only buy between 0 and 100 tickets inclusive", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.3.6 - quantity of the tickets has to be more than 0, and less than or equal to 100 [non-numeric fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_quantity_fail_alpha(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "ten")               ## Enter invalid quantity with alphabet
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Quantity must be entered using 0-9", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.3.7 - quantity of the tickets has to be more than 0, and less than or equal to 100 [blank fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_quantity_fail_blank(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", " ")                 ## Enter invalid quantity with nothing
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Quantity must be entered using 0-9", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions


'''
The bellow class tests all the requirements for R6.4 through R6.6. This tests the ability for the ticket quanity to be
bought with the current user balance. Also the redirection is tested for when an error occurs.
'''
class FrontEndR6_4_5_6(BaseCase):
    #Test Case R6.4.1 - ticket name exists in the database and the quantity is more than the quantity requested to buy [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_available_pass(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        ## Mock call will return successful
        self.assert_text("Sucessfully bought the ticket(s)", '#buy_message')    ## Check the success message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.4.2 - ticket name exists in the database and the quantity is more than the quantity requested to buy [fail not enough money]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=" Too few tickets available")
    def test_buy_ticket_available_fail_quantity(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        ## Mock call will return with an error message
        self.assert_text("Too few tickets available", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.4.3 - ticket name exists in the database and the quantity is more than the quantity requested to buy [fail ticket does not exist]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value="Ticket not found")
    def test_buy_ticket_available_fail_exist(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        ## Mock call will return with an error message
        self.assert_text("Ticket not found", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        
    #Test Case R6.5.1 - user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) [pass]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=None)
    def test_buy_ticket_balance_pass(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        ## Mock call will return successful
        self.assert_text("Sucessfully bought the ticket(s)", '#buy_message')    ## Check the success message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.5.2 - user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) [fail]
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=" User balance too low")
    def test_buy_ticket_balance_fail(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicket")     ## Enter valid ticket name
        self.type("#buy-quantity", "10")                ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        ## Mock call will return error message
        self.assert_text(" User balance too low", '#buy_message')    ## Check the error message
        self.open(base_url + '/logout')                 ## invalidate any current sessions

    #Test Case R6.6.1 - for any errors, redirect back to / and show an error message
    @patch('qa327.library.users.get_user', return_value=test_user)
    @patch('qa327.library.tickets.buy_ticket', return_value=" User balance too low")
    def test_buy_ticket_fail_redirect(self, *_):
        self.open(base_url + '/logout')                 ## invalidate any current sessions
        self.open(base_url + '/login')                  ## Go to login page
        self.type("#email", "test_frontend@test.com")   ## Enter valid email
        self.type("#password", "Test_frontend")         ## Enter valid password
        self.click('input[type="submit"]')              ## Submit the from to login
        self.open(base_url + '/')                       ## Open home page
        self.type("#buy-ticket-name", "TestTicke&t ")   ## Enter valid ticket name
        self.type("#buy-quantity", "1000")              ## Enter valid quantity
        self.click('input[type="submit"]')              ## Submit the form
        self.assert_text("Failed to buy ticket.", '#buy_message')    ## Check the error message
        self.assert_element('#welcome-header')          ## Check that we are now on the home page
        self.open(base_url + '/logout')                 ## invalidate any current sessions
