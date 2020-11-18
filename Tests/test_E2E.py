import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.CartPage import CartPage
from Pages.CheckOutPage import CheckOutPage
from Pages.ConfirmPage import ConfirmPage
from Pages.FinishPage import FinishPage
from Config.config import TestData
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_e2e(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.input_username(TestData.username)
        self.loginPage.input_password(TestData.password)
        self.loginPage.click_login_button()
        self.homePage = HomePage(self.driver)
        self.homePage.get_item()
        self.homePage.click_add_to_cart_button()
        self.homePage.click_cart()
        self.cartPage = CartPage(self.driver)
        self.cartPage.click_checkout_button()
        self.checkOutPage = CheckOutPage(self.driver)
        self.checkOutPage.input_first_name(TestData.first_name)
        self.checkOutPage.input_last_name(TestData.last_name)
        self.checkOutPage.input_zip_code(TestData.zip_code)
        self.checkOutPage.click_continue_button()
        self.confirmPage = ConfirmPage(self.driver)
        self.confirmPage.click_finish_button()
        self.finishPage = FinishPage(self.driver)
        confirmation_message = self.finishPage.get_confirmation()
        assert confirmation_message == TestData.confirmation_message





