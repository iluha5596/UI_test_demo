from pages.panel_login import LoginPanel
from pages.login_page import LoginPage


class TestAuthorization:

    def test_authorization(self, driver):
        url = 'https://magento.softwaretestingboard.com/'
        panel_login = LoginPanel(driver, url)
        panel_login.open()
        panel_login.click_sign_in()
        login_page = LoginPage(driver)
        login_page.sign_in()
