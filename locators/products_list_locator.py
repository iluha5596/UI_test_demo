from selenium.webdriver.common.by import By
import random


class ProductsListLocators:
    CARD_PRODUCT_RANDOM = (By.XPATH, f'(//li[@class="item product product-item"])[{random.randint(1,12)}]')
