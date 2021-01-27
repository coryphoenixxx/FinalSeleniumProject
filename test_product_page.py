import pytest
from .pages.product_page import ProductPage


main_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" #?promo=newYear2019"

@pytest.mark.parametrize('link', [f"{main_link}?promo=offer{i}" for i in range(10)])
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()