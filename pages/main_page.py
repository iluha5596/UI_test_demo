from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocator


class MainPage(BasePage):

    def click_men(self):
        self.element_is_clickable(*MainPageLocator.MEN).click()

    def click_show_cart(self):
        self.element_is_clickable(*MainPageLocator.SHOW_CART).click()

    def click_vie_and_edit_cart(self):
        self.element_is_clickable(*MainPageLocator.VIE_AND_EDIT_CART).click()

    def go_shopping_cart(self):
        self.click_show_cart()
        self.click_vie_and_edit_cart()

    def go_men_category(self):
        self.element_is_clickable(*MainPageLocator.MEN_CATEGORY).click()

