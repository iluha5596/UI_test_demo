from selenium.webdriver.common.by import By


class MenPageLocator:
    HOODIES_SWEATSHIRTS = (By.XPATH, '//a[text()="Hoodies & Sweatshirts"]')
    JACKETS = (By.XPATH, '//a[text()="Jackets"]')
    TEES = (By.XPATH, '//a[text()="Tees"]')
    TANKS = (By.XPATH, '//a[text()="Tanks"]')
    PANTS = (By.XPATH, '//a[text()="Pants"]')
    SHORTS = (By.XPATH, '//a[text()="Shorts"]')
