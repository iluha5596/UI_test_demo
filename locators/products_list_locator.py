from selenium.webdriver.common.by import By
import random


class ProductsListLocators:
    CARD_PRODUCT_RANDOM = (By.XPATH, f'(//li[@class="item product product-item"])[{random.randint(1, 11)}]')
    CARD_PRODUCT_5 = (By.XPATH, '(//li[@class="item product product-item"])[5]')
    CARD_PRODUCT_SIZE = (By.XPATH, f'(//li[@class="item product product-item"]/..//div[@option-tooltip-value="M"])[5]')
    CARD_PRODUCT_COLOR = (
        By.XPATH, '(//li[@class="item product product-item"]//div[@attribute-code="color"]//div[@index="0"])[5]')
    ADD_TO_CART = (By.XPATH, '(//button//span[text()="Add to Cart"])[5]')
    SELECTED_NAME_PRODUCT = (
        By.XPATH, '(//li[@class="item product product-item"]//strong[@class="product name product-item-name"]//a)[5]')
    SELECTED_CARD_PRODUCT_SIZE = (By.XPATH, '//div[@attribute-code="size"]//div[@aria-checked="true"]')
    SELECTED_CARD_PRODUCT_COLOR = (By.XPATH, '//div[@attribute-code="color"]//div[@aria-checked="true"]')
