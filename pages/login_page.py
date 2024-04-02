from pages.base_page import BasePage
from locators.login_page_locator import LoginPageLocator


class LoginPage(BasePage):

    def authorization_using_valid_pairs(self, creds):
        login, password = creds
        self.visibility_of_element_locator(*LoginPageLocator.EMAIL).send_keys(login)
        self.visibility_of_element_locator(*LoginPageLocator.PASSWORD).send_keys(password)
        self.element_is_clickable(*LoginPageLocator.SIGN_IN).click()

    def authorization_using_non_valid_pairs(self, creds):
        login, password = creds
        self.visibility_of_element_locator(*LoginPageLocator.EMAIL).send_keys(login)
        self.visibility_of_element_locator(*LoginPageLocator.PASSWORD).send_keys(password)
        self.element_is_clickable(*LoginPageLocator.SIGN_IN).click()
        error_text = self.find_element(*LoginPageLocator.ERROR).text
        assert \
            'The account sign-in was incorrect or your account is disabled temporarily. ' \
            'Please wait and try again later.' == error_text, 'Не появился текст о неуспешной авторизации'

    def authorization_using_non_valid_email(self, creds):
        login = creds
        self.visibility_of_element_locator(*LoginPageLocator.EMAIL).send_keys(login)
        self.element_is_clickable(*LoginPageLocator.SIGN_IN).click()
        error_text = self.find_element(*LoginPageLocator.ERROR_NON_VALID_EMAIL).text
        assert 'Please enter a valid email address (Ex: johndoe@domain.com).' == error_text, 'Не появился текст о не корректном email'

    def authorization_using_empty_email_login(self):
        self.element_is_clickable(*LoginPageLocator.SIGN_IN).click()
        error_text_email = self.find_element(*LoginPageLocator.ERROR_NON_VALID_EMAIL).text
        error_text_password = self.find_element(*LoginPageLocator.ERROR_NON_VALID_PASSWORD).text
        assert 'This is a required field.' == error_text_email and 'This is a required field.' == error_text_password


