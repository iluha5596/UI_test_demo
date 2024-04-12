from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocator


class MainPage(BasePage):

    def click_men(self):
        self.element_is_clickable(*MainPageLocator.MEN).click()

    def click_show_cart(self):
        cart_button = self.visibility_of_element_locator(*MainPageLocator.SHOW_CART)
        cart_button.click()

    def click_vie_and_edit_cart(self):
        edit_cart = self.visibility_of_element_locator(*MainPageLocator.VIE_AND_EDIT_CART)
        edit_cart.click()

    def go_shopping_cart(self):
        self.click_show_cart()
        self.click_vie_and_edit_cart()

    def go_men_category(self):
        self.element_is_clickable(*MainPageLocator.MEN_CATEGORY).click()

