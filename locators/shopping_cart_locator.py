from selenium.webdriver.common.by import By


class ShoppingCartLocator:
    PRODUCTS = (By.XPATH, '//tbody[@class="cart item"]')
    NAME = (By.XPATH, '(//tbody[@class="cart item"])[{}]//strong[@class="product-item-name"]')
    SIZE = (By.XPATH, '((//tbody[@class="cart item"])[{}]//dd)[1]')
    COLOR = (By.XPATH, '((//tbody[@class="cart item"])[{}]//dd)[2]')
    QTY = (By.XPATH, '(//tbody[@class="cart item"])[{}]//input[@title="Qty"]')