from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.products_list_locator import ProductsListLocators
import allure


class ProductsListPage(BasePage):

    def click_card_product_random(self):
        with allure.step('Проход в карточку продукта'):
            self.element_is_clickable(*ProductsListLocators.CARD_PRODUCT_RANDOM).click()

    def click_card_product_size(self, number_product):
        size_locator = ProductsListLocators.CARD_PRODUCT_SIZE[1].format(number_product)
        self.element_is_clickable(By.XPATH, size_locator).click()

    def click_card_product_color(self, number_product):
        color_locator = ProductsListLocators.CARD_PRODUCT_COLOR[1].format(number_product)
        self.element_is_clickable(By.XPATH, color_locator).click()

    def click_add_to_cart(self, number_product):
        add_to_cart_locator = ProductsListLocators.ADD_TO_CART[1].format(number_product)
        add_to_cart_button = self.presence_of_element_located(By.XPATH, add_to_cart_locator)
        self.driver.execute_script("arguments[0].click();", add_to_cart_button)

    def added_product_in_cart(self, number_product):
        self.click_card_product_size(number_product)
        self.click_card_product_color(number_product)
        self.click_add_to_cart(number_product)
        select_name_locator = ProductsListLocators.SELECTED_NAME_PRODUCT[1].format(number_product)
        value_date_product = [self.find_element(By.XPATH, select_name_locator).text,
                              self.find_element(*ProductsListLocators.SELECTED_CARD_PRODUCT_SIZE).get_attribute(
                                  "option-tooltip-value"),
                              self.find_element(*ProductsListLocators.SELECTED_CARD_PRODUCT_COLOR).get_attribute(
                                  "option-label"),
                              '1']
        return value_date_product
