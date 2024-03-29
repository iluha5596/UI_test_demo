from pages.base_page import BasePage
from locators.login_page_locator import LoginPageLocator
from data.read_data import LoginPageData
import pytest


class LoginPage(BasePage):

    def authorization_using_non_valid_pairs(self, creds):
        login, password = creds
        self.find_element(*LoginPageLocator.EMAIL).send_keys(login)
        self.find_element(*LoginPageLocator.PASSWORD).send_keys(password)
        self.element_is_clickable(*LoginPageLocator.SIGN_IN).click()
        error_text = self.find_element(*LoginPageLocator.ERROR).text
        assert \
            'The account sign-in was incorrect or your account is disabled temporarily. ' \
            'Please wait and try again later.' == error_text, 'Не появился текст о неуспешной авторизации'

    def authorization_using_valid_pairs(self, creds):
        login, password = creds
        self.find_element(*LoginPageLocator.EMAIL).send_keys(login)
        self.find_element(*LoginPageLocator.PASSWORD).send_keys(password)
        self.element_is_clickable(*LoginPageLocator.SIGN_IN).click()


