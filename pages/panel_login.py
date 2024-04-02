from pages.base_page import BasePage
from locators.panel_login_locator import PanelLogin


class LoginPanel(BasePage):

    def click_sign_in(self):
        self.element_is_clickable(*PanelLogin.SIGN_IN).click()

    def checking_user_authorization(self):
        # self.visibility_of_element_locator(*PanelLogin.LOGIN_IN)
        user_authorization_element = self.find_element(*PanelLogin.LOGIN_IN)
        assert user_authorization_element.is_displayed(), 'Авторизация не прошла'
