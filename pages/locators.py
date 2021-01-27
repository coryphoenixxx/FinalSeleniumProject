from selenium.webdriver.common.by import By

class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_INPUT_FIELD = (By.ID, 'id_registration-email')
    PASSWORD_INPUT_FIELD = (By.ID, 'id_registration-password1')
    CONFIRM_INPUT_FIELD = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')

class ProductPageLocators():
    ADD_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_TITLE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_TITLE_IN_ALERT_SUCCESS = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BASKET_PRICE = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]')
    BASKET_PRICE_IN_ALERT_SUCCESS = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')

class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p')
    BASKET_IS_NOT_EMPTY = (By.CLASS_NAME, 'basket_summary')
