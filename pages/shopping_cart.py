from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.shopping_cart_locator import ShoppingCartLocator
from data.generate_dict_product import GenerateDictProduct


class ShoppingCart(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.data_shopping_cart_dict = {}

    def add_shopping_cart_in_dict(self):
        for el in range(1, len(self.find_elements(*ShoppingCartLocator.PRODUCTS)) + 1):
            name_locator = ShoppingCartLocator.NAME[1].format(el)
            size_locator = ShoppingCartLocator.SIZE[1].format(el)
            color_locator = ShoppingCartLocator.COLOR[1].format(el)
            qty_locator = ShoppingCartLocator.QTY[1].format(el)
            name = self.find_element(By.XPATH, name_locator)
            size = self.find_element(By.XPATH, size_locator)
            color = self.find_element(By.XPATH, color_locator)
            qty = self.find_element(By.XPATH, qty_locator)
            self.data_shopping_cart_dict[el] = [name.text,
                                                size.text,
                                                color.text,
                                                qty.get_attribute('value')]
        return self.data_shopping_cart_dict
