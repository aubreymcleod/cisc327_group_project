import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url


# integration testing: the test case interacts with the
# browser, and test the whole system (frontend+backend).

@pytest.mark.usefixtures('server')
class Sell_Buy(BaseCase):
    def register_user0(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "test0@test.sb.com")
        self.type("#name", "test0")
        self.type("#password", "Test0!")
        self.type("#password2", "Test0!")
        self.click('input[type="submit"]')

    def login_user0(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "test0@test.sb.com")
        self.type("#password", "Test0!")
        self.click('input[type="submit"]')

    def register_user1(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "test1@test.sb.com")
        self.type("#name", "test1")
        self.type("#password", "Test1!")
        self.type("#password2", "Test1!")
        self.click('input[type="submit"]')

    def login_user1(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "test1@test.sb.com")
        self.type("#password", "Test1!")
        self.click('input[type="submit"]')

    def list_ticket(self):
        self.open(base_url)
        self.type("#sell-ticket-name", "Test Ticket")
        self.type("#sell-quantity", "10")
        self.type("#sell-price", "100")
        self.type("#sell-expiration", "20211231")
        self.click('#sell-submit')

    def buy_ticket(self):
        self.open(base_url)
        self.type("#buy-ticket-name", "Test Ticket")
        self.type("#buy-quantity", "10")
        self.click("#buy-submit")

    def test_init_sell(self):
        self.register_user0()
        self.login_user0()
        self.list_ticket()
        self.assert_text("(x10)", '#ticket1_quantity')
        self.assert_text("Test Ticket", "#ticket1_name")
        self.assert_text("$100", "#ticket1_price")
        self.click("#logout")

    def test_next_buy(self):
        self.register_user1()
        self.login_user1()
        self.assert_text("Your balance is 5000", "#user-balance")
        self.buy_ticket()
        self.assert_text("Your balance is 3600", "#user-balance")
        self.click("#logout")
