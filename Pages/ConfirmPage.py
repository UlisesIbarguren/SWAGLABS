from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class ConfirmPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    finish_button = (By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.cart_footer > a.btn_action.cart_button")

    def click_finish_button(self):
        self.do_click(self.finish_button)


