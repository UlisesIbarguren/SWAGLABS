from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class FinishPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    confirmation = (By.CSS_SELECTOR, "#checkout_complete_container > h2")

    def get_confirmation(self):
        return self.get_element_text(self.confirmation)

