from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from locators.panel_login_locator import PanelLogin
import allure


class LoginPanel(BasePage):

    def click_sign_in(self):
        self.element_is_clickable(*PanelLogin.SIGN_IN).click()

    def checking_user_authorization(self):
        with allure.step('Проверка, что авторизация прошла успешна'):
            try:
                user_authorization_element = self.find_element(*PanelLogin.LOGIN_IN)
            except NoSuchElementException:
                assert user_authorization_element.is_displayed(), 'Авторизация не прошла'
