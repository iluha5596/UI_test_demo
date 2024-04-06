from pages.base_page import BasePage
from locators.products_list_locator import ProductsListLocators


class ProductsListPage(BasePage):

    def click_card_product_random(self):
        self.element_is_clickable(*ProductsListLocators.CARD_PRODUCT_RANDOM).click()
