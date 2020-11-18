from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    checkout_button = (By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_footer > a.btn_action.checkout_button")

    def click_checkout_button(self):
        self.do_click(self.checkout_button)
