from selenium.webdriver.common.by import By


class PanelLogin:
    SIGN_IN = (By.XPATH, '(//li[@class="authorization-link"])[1]')
    LOGIN_IN = (By.XPATH, '(//*[@class="logged-in"])[1]')