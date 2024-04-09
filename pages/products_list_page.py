from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.products_list_locator import ProductsListLocators
import random


class ProductsListPage(BasePage):

    def click_card_product_random(self):
        self.element_is_clickable(*ProductsListLocators.CARD_PRODUCT_RANDOM).click()

    def click_card_product_size(self):
        self.element_is_clickable(*ProductsListLocators.CARD_PRODUCT_SIZE).click()

    def click_card_product_color(self):
        self.element_is_clickable(*ProductsListLocators.CARD_PRODUCT_COLOR).click()

    def click_add_to_cart(self):
        element = self.find_element(*ProductsListLocators.CARD_PRODUCT_5)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()  # Наведение курсора на элемент
        self.element_is_clickable(*ProductsListLocators.ADD_TO_CART).click()
        self.element_is_clickable(*ProductsListLocators.ADD_TO_CART)

    def added_product_in_cart(self):
        self.click_card_product_size()
        self.click_card_product_color()
        self.click_add_to_cart()
        value_date_product = [self.find_element(*ProductsListLocators.SELECTED_NAME_PRODUCT).text,
                              self.find_element(*ProductsListLocators.SELECTED_CARD_PRODUCT_SIZE).get_attribute("option-tooltip-value"),
                              self.find_element(*ProductsListLocators.SELECTED_CARD_PRODUCT_COLOR).get_attribute("option-label"),
                              '1']
        return value_date_product
