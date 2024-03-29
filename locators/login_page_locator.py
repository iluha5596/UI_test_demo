from selenium.webdriver.common.by import By


class LoginPageLocator:
    EMAIL = (By.XPATH, '//*[@id="email"]')
    PASSWORD = (By.XPATH, '(//input[@id="pass"])[1]')
    SIGN_IN = (By.XPATH, '//button[@class="action login primary"]')
    CUSTOMER_LOGIN = (By.XPATH, '(//*[text()="Customer Login"])[2]')
    ERROR = (By.XPATH, '//*[@class="message-error error message"]')

