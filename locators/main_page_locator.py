from selenium.webdriver.common.by import By


class MainPageLocator:
    MEN = (By.XPATH, '//span[text()="Men"]')
    SHOW_CART = (By.XPATH, '//a[@class="action showcart"]')
    VIE_AND_EDIT_CART = (By.XPATH, '//span[text()="View and Edit Cart"]')
    MEN_CATEGORY = (By.XPATH, '//a[text()="Men"]')
