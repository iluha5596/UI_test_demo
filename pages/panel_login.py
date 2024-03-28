from pages.base_page import BasePage
from locators.panel_login_locator import PanelLogin


class LoginPanel(BasePage):

    def click_sign_in(self):
        self.element_is_clickable(*PanelLogin.SIGN_IN).click()
