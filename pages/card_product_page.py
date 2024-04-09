import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.card_product_locator import CardProductLocator
from data.generate_dict_product import GenerateDictProduct


class CardProductPage(BasePage):

    def choose_size(self, size):
        size_locator = CardProductLocator.SIZE[1].format(size)
        self.element_is_clickable(By.XPATH, size_locator).click()

    def choose_color(self, color):
        color_locator = CardProductLocator.COLOR[1].format(color)
        self.element_is_clickable(By.XPATH, color_locator).click()

    def fill_qty(self, count):
        qty = self.find_element(*CardProductLocator.QTY)
        if int(count) > 1:
            qty.clear()
            qty.send_keys(count)

    def add_cart(self):
        self.element_is_clickable(*CardProductLocator.ADD_TO_CARD).click()

    def go_shopping_cart(self):
        self.visibility_of_element_locator(*CardProductLocator.ALERT)
        self.element_is_clickable(*CardProductLocator.SHOPPING_CART).click()

    def add_product(self, size, color, count):
        self.choose_size(size)
        self.choose_color(color)
        self.fill_qty(count)
        self.add_cart()

    def adding_two_identical_products(self, size, color, count):
        self.add_product(size, color, count)
        value_date_product = [self.find_element(*CardProductLocator.NAME_PRODUCT).text,
                              size,
                              self.find_element(*CardProductLocator.SELECTED_COLOR).text,
                              count]
        generate_dict_product = GenerateDictProduct()
        dict_product = generate_dict_product.add_value_in_dict(value_date_product)
        return dict_product

    def adding_products_different_sizes(self, sizes, color, count):
        dict_product = None
        generate_dict_product = GenerateDictProduct()
        name_product = self.find_element(*CardProductLocator.NAME_PRODUCT).text
        self.choose_color(color)
        selected_color = self.find_element(*CardProductLocator.SELECTED_COLOR).text
        for size in sizes:
            self.choose_size(size)
            value_date_product = [name_product,
                                  size,
                                  selected_color,
                                  count]
            dict_product = generate_dict_product.add_value_in_dict(value_date_product)
            self.add_cart()
        self.element_is_clickable(*CardProductLocator.ADD_TO_CARD)
        return dict_product

    def adding_product_different_color(self, size, colors, count):
        dict_product = None
        generate_dict_product = GenerateDictProduct()
        name_product = self.find_element(*CardProductLocator.NAME_PRODUCT).text
        self.choose_size(size)
        for color in colors:
            self.choose_color(color)
            selected_color = self.find_element(*CardProductLocator.SELECTED_COLOR).text
            value_date_product = [name_product,
                                  size,
                                  selected_color,
                                  count]
            dict_product = generate_dict_product.add_value_in_dict(value_date_product)
            self.add_cart()
        self.element_is_clickable(*CardProductLocator.ADD_TO_CARD)
        return dict_product

    def adding_products_from_different_categories(self, size, color, count):
        self.add_product(size, color, count)
        value_date_product = [self.find_element(*CardProductLocator.NAME_PRODUCT).text,
                              size,
                              self.find_element(*CardProductLocator.SELECTED_COLOR).text,
                              count]
        return value_date_product
