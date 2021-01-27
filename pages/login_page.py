import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(self.email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_INPUT_FIELD).send_keys(self.password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Incorrect url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
