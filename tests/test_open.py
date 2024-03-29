from pages.panel_login import LoginPanel
from data.generate_pairs_login_password import generate_non_valid_pairs
from data.generate_pairs_login_password import generate_valid_pairs
from pages.login_page import LoginPage
import pytest


class TestAuthorization:

    @pytest.mark.parametrize('creds', generate_non_valid_pairs())
    def test_authorization_non_valid_pairs(self, driver, creds):
        url = 'https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/'
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.authorization_using_non_valid_pairs(creds)

    @pytest.mark.parametrize('creds', generate_valid_pairs())
    def test_authorization_valid_pairs(self, driver, creds):
        url = 'https://magento.softwaretestingboard.com/customer/account/login/referer/aHR0cHM6Ly9tYWdlbnRvLnNvZnR3YXJldGVzdGluZ2JvYXJkLmNvbS8%2C/'
        login_page = LoginPage(driver, url)
        login_page.open()
        login_page.authorization_using_valid_pairs(creds)
        panel_login = LoginPanel(driver)
        panel_login.checking_user_authorization()
