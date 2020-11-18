import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Config.config import TestData
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_home_page(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.input_username(TestData.username)
        self.loginPage.input_password(TestData.password)
        self.loginPage.click_login_button()
        self.homePage = HomePage(self.driver)
        self.homePage.get_title(TestData.home_page_title)






