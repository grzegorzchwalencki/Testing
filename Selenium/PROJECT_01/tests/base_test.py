import sys
sys.path.insert(0, "..")
from selenium import webdriver
import unittest
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """Base class to use in every test"""
    def setUp(self):
        """ Initial conditions in every test"""
        # Open browser
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://magento.softwaretestingboard.com/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()