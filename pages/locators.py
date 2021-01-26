from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_TITLE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_TITLE_IN_ALERT_SUCCESS = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BASKET_PRICE = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]')
    BASKET_PRICE_IN_ALERT_SUCCESS = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
