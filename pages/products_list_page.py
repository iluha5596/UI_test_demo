from pages.base_page import BasePage
from locators.products_list_locator import ProductsListLocators


class ProductsListPage(BasePage):

    def click_card_product_random(self):
        self.element_is_clickable(*ProductsListLocators.CARD_PRODUCT_RANDOM).click()

    def click_card_product_size(self):
        self.element_is_clickable(*ProductsListLocators.CARD_PRODUCT_SIZE).click()

    def click_card_product_color(self):
        self.element_is_clickable(*ProductsListLocators.CARD_PRODUCT_COLOR).click()

    def click_add_to_cart(self):
        add_to_cart_button = self.presence_of_element_located(*ProductsListLocators.ADD_TO_CART)
        self.driver.execute_script("arguments[0].click();", add_to_cart_button)

    def added_product_in_cart(self):
        self.click_card_product_size()
        self.click_card_product_color()
        self.click_add_to_cart()
        value_date_product = [self.find_element(*ProductsListLocators.SELECTED_NAME_PRODUCT).text,
                              self.find_element(*ProductsListLocators.SELECTED_CARD_PRODUCT_SIZE).get_attribute("option-tooltip-value"),
                              self.find_element(*ProductsListLocators.SELECTED_CARD_PRODUCT_COLOR).get_attribute("option-label"),
                              '1']
        return value_date_product
