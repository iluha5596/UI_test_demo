import pytest
from pages.card_product_page import CardProductPage
from pages.shopping_cart import ShoppingCart
from pages.main_page import MainPage
from pages.men_page import MenPage
from pages.products_list_page import ProductsListPage


def passage_section_men_page(driver, url):
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.click_men()


class TestCheckCart:

    @pytest.mark.skip
    def test_check_cart_tow_identical_products(self, driver):
        url = 'https://magento.softwaretestingboard.com/'
        passage_section_men_page(driver, url)
        men_page = MenPage(driver)
        men_page.click_hoodies_sweatshirts()
        products_list_page = ProductsListPage(driver)
        products_list_page.click_card_product_random()
        card_product_page = CardProductPage(driver)
        added_items_cart = card_product_page.adding_two_identical_products(size='M', color=2, count='2')
        card_product_page.go_shopping_cart()
        shopping_cart = ShoppingCart(driver)
        data_shopping_cart_dict = shopping_cart.add_shopping_cart_in_dict()
        assert added_items_cart == data_shopping_cart_dict, f'Продукты в корзине не соответствуют тем, что были добавлены.' \
                                                            f'\nПродукты добавленные в корзину: {added_items_cart}' \
                                                            f'\nПродукты в корзине: {data_shopping_cart_dict}'

    def test_check_cart_products_different_sizes(self, driver):
        url = 'https://magento.softwaretestingboard.com/'
        passage_section_men_page(driver, url)
        men_page = MenPage(driver)
        men_page.click_jackets()
        products_list_page = ProductsListPage(driver)
        products_list_page.click_card_product_random()
        card_product_page = CardProductPage(driver)
        added_items_cart = card_product_page.adding_products_different_sizes(sizes=['XS', 'S', 'M', 'L', 'XL'], color=0,
                                                                             count='1')
        card_product_page.go_shopping_cart()
        shopping_cart = ShoppingCart(driver)
        data_shopping_cart_dict = shopping_cart.add_shopping_cart_in_dict()
        assert added_items_cart == data_shopping_cart_dict, f'Продукты в корзине не соответствуют тем, что были добавлены.' \
                                                            f'\nПродукты добавленные в корзину: {added_items_cart}' \
                                                            f'\nПродукты в корзине: {data_shopping_cart_dict}'


