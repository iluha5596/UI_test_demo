from selenium.webdriver.common.by import By


class CardProductLocator:
    NAME_PRODUCT = (By.XPATH, '//*[@itemprop="name"]')
    SELECTED_SIZE = (By.XPATH, '(//*[@class="swatch-attribute-selected-option"])[1]')
    SELECTED_COLOR = (By.XPATH, '(//*[@class="swatch-attribute-selected-option"])[2]')
    SIZE = (By.XPATH, '//*[@option-label="{}"]')
    COLOR = (By.XPATH, '//div[@aria-labelledby="option-label-color-93"]//div[@index="{}"]')
    QTY = (By.XPATH, '//input[@name="qty"]')
    ADD_TO_CARD = (By.XPATH, '//button[@title="Add to Cart"]')
    ALERT = (By.XPATH, '//div[@role="alert"]')
    SHOPPING_CART = (By.XPATH, '//a[text()="shopping cart"]')


