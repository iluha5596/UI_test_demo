import time

from pages.base_page import BasePage
from locators.login_page_locator import LoginPageLocator
from data.read_data import LoginPageData


def value_logins_passwords():
    data_password_login = LoginPageData('data/login_page_data.json')
    logins = [login_value for login_value in data_password_login.logins.values()]
    passwords = [passwords for passwords in data_password_login.passwords.values()]
    return logins, passwords


class LoginPage(BasePage):

    def sign_in(self):
        logins, passwords = value_logins_passwords()
        print(logins, passwords)
        self.visibility_of_element_locator(*LoginPageLocator.EMAIL).send_keys(logins[0])
        self.visibility_of_element_locator(*LoginPageLocator.PASS).send_keys(passwords[0])
        self.element_is_clickable(*LoginPageLocator.SIGN_IN).click()


