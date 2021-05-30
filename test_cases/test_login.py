import unittest
import HtmlTestRunner
from ddt import ddt, file_data
from selenium import webdriver
import sys
import os

from page_objects.login_page import LoginPage

@ddt
class Testlogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://ceita-dev.appiancloud.com/suit/")
        cls.driver.maximize_window()
        cls.login_page = LoginPage(driver = cls.driver)

    @file_data(os.path.join("data", "test_login.json"))
    def test_login(self, username, password):
        self.login_page.login_in_app(username=username, password=password)
        is_login_succesful = self.login_page.is_singin_succesfull()

        assert is_login_succesful is True

    @file_data(os.path.join("data", "fill_the_field.json"))
    def fill_the_field(self, nombre_de_la_exhibicion, tema_de_la_exhibicion):
        self.login_page.fill_the_fields(nombre_exhibicion=nombre_de_la_exhibicion, tema_exhibicion=tema_de_la_exhibicion)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


