from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    item = (By.ID, "item_4_title_link")
    add_to_cart_button = (By.CSS_SELECTOR, "#inventory_item_container > div > div > div > button")
    cart = (By.CSS_SELECTOR, "#shopping_cart_container > a > svg > path")
    page_title = (By.CSS_SELECTOR, "head > title")

    def get_item(self):
        self.do_click(self.item)

    def click_add_to_cart_button(self):
        self.do_click(self.add_to_cart_button)

    def click_cart(self):
        self.do_click(self.cart)



