from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CheckOutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    zip_code = (By.ID, "postal-code")
    continue_button = (By.CSS_SELECTOR, "#checkout_info_container > div > form > div.checkout_buttons > input")

    def input_first_name(self, first_name):
        self.do_send_keys(self.first_name, first_name)

    def input_last_name(self, last_name):
        self.do_send_keys(self.last_name, last_name)

    def input_zip_code(self, zip_code):
        self.do_send_keys(self.zip_code, zip_code)

    def click_continue_button(self):
        self.do_click(self.continue_button)



