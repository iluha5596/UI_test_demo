from pages.base_page import BasePage
from locators.men_page_locator import MenPageLocator


class MenPage(BasePage):

    def click_hoodies_sweatshirts(self):
        self.element_is_clickable(*MenPageLocator.HOODIES_SWEATSHIRTS).click()

    def click_jackets(self):
        self.element_is_clickable(*MenPageLocator.JACKETS).click()

    def click_tees(self):
        self.element_is_clickable(*MenPageLocator.TEES).click()

    def click_tanks(self):
        self.element_is_clickable(*MenPageLocator.TANKS).click()

    def click_pants(self):
        self.element_is_clickable(*MenPageLocator.PANTS).click()

    def click_shorts(self):
        self.element_is_clickable(*MenPageLocator.SHORTS).click()
