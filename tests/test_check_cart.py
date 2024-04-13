import pytest
import allure
from pages.card_product_page import CardProductPage
from pages.shopping_cart import ShoppingCart
from pages.main_page import MainPage
from pages.men_page import MenPage
from pages.products_list_page import ProductsListPage
from data.generate_dict_product import GenerateDictProduct


def passage_section_men_page(driver, url):
    main_page = MainPage(driver, url)
    main_page.open()
    main_page.click_men()


def checking_correspondence_added_product_cart(added_items_cart_dict, data_shopping_cart_dict):
    with allure.step('Проверка того, что в корзине имеются добавленные товары'):
        assert added_items_cart_dict == data_shopping_cart_dict, f'Продукты в корзине не соответствуют тем, что были добавлены.' \
                                                                 f'\nПродукты добавленные в корзину: {added_items_cart_dict}' \
                                                                 f'\nПродукты в корзине: {data_shopping_cart_dict}'


@allure.feature('Заполнение корзины')
class TestCheckCart:

    @allure.title('Проверка корзины с двумя одинковыми продукми')
    def test_check_cart_tow_identical_products(self, driver):
        url = 'https://magento.softwaretestingboard.com/'
        passage_section_men_page(driver, url)
        men_page = MenPage(driver)
        men_page.click_hoodies_sweatshirts()
        products_list_page = ProductsListPage(driver)
        products_list_page.click_card_product_random()
        card_product_page = CardProductPage(driver)
        added_items_cart_dict = card_product_page.adding_two_identical_products(size='M', color=2, count='2')
        card_product_page.go_shopping_cart()
        shopping_cart = ShoppingCart(driver)
        data_shopping_cart_dict = shopping_cart.add_shopping_cart_in_dict()
        checking_correspondence_added_product_cart(added_items_cart_dict, data_shopping_cart_dict)

    @allure.title('Проверка корзины по одному продукту с одним цветом и разными размерами')
    def test_check_cart_products_different_sizes(self, driver):
        url = 'https://magento.softwaretestingboard.com/'
        passage_section_men_page(driver, url)
        men_page = MenPage(driver)
        men_page.click_jackets()
        products_list_page = ProductsListPage(driver)
        products_list_page.click_card_product_random()
        card_product_page = CardProductPage(driver)
        added_items_cart_dict = card_product_page.adding_products_different_sizes(sizes=['XS', 'S', 'M', 'L', 'XL'],
                                                                                  color=0,
                                                                                  count='1')
        card_product_page.go_shopping_cart()
        shopping_cart = ShoppingCart(driver)
        data_shopping_cart_dict = shopping_cart.add_shopping_cart_in_dict()
        checking_correspondence_added_product_cart(added_items_cart_dict, data_shopping_cart_dict)

    @allure.title('Проверка корзины по одному продукту с одним размером и разными цветами')
    def test_check_cart_products_different_color(self, driver):
        url = 'https://magento.softwaretestingboard.com/'
        passage_section_men_page(driver, url)
        men_page = MenPage(driver)
        men_page.click_tees()
        products_list_page = ProductsListPage(driver)
        products_list_page.click_card_product_random()
        card_product_page = CardProductPage(driver)
        added_items_cart_dict = card_product_page.adding_product_different_color(size='L', colors=[0, 1, 2], count='1')
        card_product_page.go_shopping_cart()
        shopping_cart = ShoppingCart(driver)
        data_shopping_cart_dict = shopping_cart.add_shopping_cart_in_dict()
        checking_correspondence_added_product_cart(added_items_cart_dict, data_shopping_cart_dict)

    @pytest.mark.smoke
    @allure.title('Проверка корзины по продуктам из разной категории')
    def test_checking_cart_with_one_product_from_each_category(self, driver):
        url = 'https://magento.softwaretestingboard.com/'
        added_items_cart_dict = GenerateDictProduct()
        passage_section_men_page(driver, url)
        men_page = MenPage(driver)
        main_page = MainPage(driver)
        go_categories = [men_page.click_hoodies_sweatshirts, men_page.click_jackets, men_page.click_tees]
        counter = 0
        with allure.step('Добавление в корзину продуктов из разных категорий, не открывая карточку продукта'):
            for go_category in go_categories:
                go_category()
                products_list_page = ProductsListPage(driver)
                dict_product = products_list_page.added_product_in_cart(number_product=5)
                added_items_cart_dict.add_value_in_dict(dict_product)
                counter += 1
                if counter != len(go_categories):
                    main_page.go_men_category()
        main_page.go_shopping_cart()
        shopping_cart = ShoppingCart(driver)
        data_shopping_cart_dict = shopping_cart.add_shopping_cart_in_dict()
        checking_correspondence_added_product_cart(added_items_cart_dict.data, data_shopping_cart_dict)
