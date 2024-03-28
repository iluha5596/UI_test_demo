from selenium.webdriver.common.by import By


class LoginPageLocator:
    EMAIL = (By.XPATH, '//*[@id="email"]')
    PASS = (By.XPATH, '//button[@class="action login primary"]')
    SIGN_IN = (By.XPATH, '//button[@class="action login primary"]')

