import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", "sdfjksadf4454564")
        page.should_be_authorized_user()

    # @pytest.mark.parametrize('i', [0, 1, 2, 3, 4, 5, 6,
    #                                pytest.param(7, marks=pytest.mark.xfail(reason="Expected Error")),
    #                                8, 9])
    def test_user_can_add_product_to_basket(self, browser):
        # link = f"{base_link}?promo=offer{i}"
        page = ProductPage(browser, base_link)
        page.open()
        page.add_product_to_basket()
        page.should_be_add_to_basket_message()
        page.should_be_basket_price_message()
        page.should_be_equal_product_titles()
        page.should_be_equal_basket_prices()

    # def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
    #     page = ProductPage(browser, base_link)
    #     page.open()
    #     page.add_product_to_basket()
    #     page.should_not_be_success_message1()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, base_link)
        page.open()
        page.should_not_be_success_message1()


# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, base_link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_not_be_success_message2()
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     page = ProductPage(browser, base_link)
#     page.open()
#     page.go_to_basket()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_be_empty_basket()
#     basket_page.should_be_empty_basket_message()