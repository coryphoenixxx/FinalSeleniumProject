from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), "Basket is not empty"

    def should_be_empty_basket_message(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE).text
        assert text == 'Your basket is empty. Continue shopping', f"Basket is not empty ({text})"

