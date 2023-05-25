import sys
sys.path.append(sys.path[0]+"/..")

import unittest
#from ddt import ddt, data, unpack
from tests.base_test import BaseTest
from pages.create_account_page import Locators
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.by import By 
from time import sleep

class CreateAccountTest(BaseTest):
    """Create Account tests"""
    def setUp(self):
        super().setUp()
        self.create_account_page = self.home_page.click_create_account()

    def requiredFieldError(self, field_error_locator):
        """ Method to check if expected error message 
        "This field is required." is appeared"""
        # a) Find all error statements on current webpage
        user_error_msg = self.driver.find_elements(*field_error_locator)
        # b) Check that the number of errors is equal to 1.
        self.assertEqual(1, len(user_error_msg))
        # c) Check if error message is "This is required field"
        self.assertEqual("This is a required field.", user_error_msg[0].text)

    def test_no_firstname_enter(self):
        """Test create account with no first name entered"""
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        # not
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter email
        self.create_account_page.enter_email("test@test.pl")
        # 5. Enter Password
        self.create_account_page.enter_password("Testtest!")
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        # 1. User get an information "This is required field." 
        # a) Find all error statements on current webpage
        # b) Check that the number of errors is equal to 1.
        # c) Check if error message is "This is required field"
        self.requiredFieldError(Locators.FIRST_NAME_ERROR)

    def test_no_lastname_entered(self):
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        # Non
        # 4. Enter email
        self.create_account_page.enter_email("test@test.pl")
        # 5. Enter Password
        self.create_account_page.enter_password("Testtest!")
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        self.requiredFieldError(Locators.LAST_NAME_ERROR)

    def test_no_email_entered(self):
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter email
        # None
        # 5. Enter Password
        self.create_account_page.enter_password("Testtest!")
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        self.requiredFieldError(Locators.EMAIL_ERROR)

    def test_no_password_entered(self):
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter email
        self.create_account_page.enter_email("test@test.pl")
        # 5. Enter Password
        # None
        # 6. Enter Confirm Password
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        self.requiredFieldError(Locators.PASSWORD_ERROR)

    def test_no_password_confirmation_entered(self):
        # Steps
        # 1. Click Create an Account
        # Done in setUp
        # 2. Enter first name
        self.create_account_page.enter_firstname("test")
        # 3. Enter last name
        self.create_account_page.enter_lastname("test")
        # 4. Enter email
        self.create_account_page.enter_email("test@test.pl")
        # 5. Enter Password
        self.create_account_page.enter_password("Testtest!")
        # 6. Enter Confirm Password
        # None
        # 7. Click button to create account
        self.create_account_page.click_create_button()
        
        # EXPECTED RESULT
        self.requiredFieldError(Locators.PASSWORD_CONF_ERROR)

