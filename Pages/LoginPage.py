from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)

    def input_username(self, username):
        self.do_send_keys(self.username, username)

    def input_password(self, password):
        self.do_send_keys(self.password, password)

    def click_login_button(self):
        self.do_click(self.login_button)

