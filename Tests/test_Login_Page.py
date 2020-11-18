import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Config.config import TestData
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def test_login_page(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.get_title(TestData.login_page_title)
