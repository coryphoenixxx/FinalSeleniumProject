from .base_page import BasePage
from .locators import ProductPageLocators


import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_CART_BUTTON)
        btn.click()
        self.solve_quiz_and_get_code()
        time.sleep(0)
        self.should_be_add_to_basket_message()
        self.should_be_basket_price_message()
        self.should_be_equal_product_titles()
        self.should_be_equal_basket_prices()

    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE_IN_ALERT_SUCCESS), \
                                        "Add_to_basket message is not presented"

    def should_be_basket_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE_IN_ALERT_SUCCESS), \
                                        "Basket_price_message is not presented"

    def should_be_equal_product_titles(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_title_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_IN_ALERT_SUCCESS).text
        assert product_title == product_title_in_message, f"Titles is not equal ('{product_title}' != '{product_title_in_message}'"

    def should_be_equal_basket_prices(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text.split(' ')[2][:6]
        price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_ALERT_SUCCESS).text.split(' ')[0]
        assert basket_price == price_in_message, f"Prices is not equal ('{basket_price}' != '{price_in_message}'"



