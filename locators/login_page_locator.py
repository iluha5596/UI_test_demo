from selenium.webdriver.common.by import By


class LoginPageLocator:
    EMAIL = (By.XPATH, '//*[@id="emailф"]')
    PASSWORD = (By.XPATH, '(//input[@id="pass"])[1]')
    SIGN_IN = (By.XPATH, '//button[@class="action login primary"]')
    CUSTOMER_LOGIN = (By.XPATH, '(//*[text()="Customer Login"])[2]')
    ERROR = (By.XPATH, '//*[@class="message-error error message"]')
    ERROR_NON_VALID_EMAIL = (By.XPATH, '//*[@id="email-error"]')
    ERROR_NON_VALID_PASSWORD = (By.XPATH, '//*[@id="pass-error"]')

