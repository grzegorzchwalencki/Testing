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
        sleep(5)

#    def requiredFieldError(self, field_error_locator):
#        """ Method to check if expected error message 
#        "This field is required." is appeared in correct location """
#        # a) Find all error statements on current webpage
#        user_error_msg = self.driver.find_elements(By.XPATH, '//dev[@class="mege-error"]')
#        # b) Check that the number of errors is equal to 1.
#        self.assertEqual(1, len(user_error_msg))
#        # c) Check if error message is "This is required field"
#        self.assertEqual("This field is required.", user_error_msg)
#        # d) Verify that the location of the error message is correct - below the First Name input field
#        error_msg = self.driver.find_element(locate_with(By.XPATH, '//div[@class="mage-error"]').near(field_error_locator) )
#        # e) Verify that error found using both method is the same error
#        self.assertEqual(user_error_msg[0].id, error_msg.id)
#
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
        # 1. User get an information "This is required field." below First Name input field.
        # a) Find all error statements on current webpage
        # b) Check that the number of errors is equal to 1.
        # c) Check if error message is "This is required field"
        # d) Verify that the location of the error message is correct - below the First Name input field
        # e) Verify that error found using both method is the same error
        #self.requiredFieldError(Locators.FIRST_NANE_INPUT)
#
#
#    #def test_no_lastname_entered(self):
#    #    """Test create account with no last name entered"""
#    #    # Steps
#    #    # 1. Click Create an Account
#    #    # Done in setUp
#    #    # 2. Enter first name
#    #    self.create_account_page.enter_firstname("test")
#    #    # 3. Enter last name
#    #    self.create_account_page.enter_lastname("test")
#    #    # 4. Enter email
#    #    self.create_account_page.enter_email("test@test.pl")
#    #    # 5. Enter Password
#    #    self.create_account_page.enter_password("Testtest!")
#    #    # 6. Enter Confirm Password
#    #    self.create_account_page.enter_password_con("Testtest!")
#    #    # 7. Click button to create account
#    #    self.create_account_page.click_create_button()
##
#    #    # EXPECTED RESULT
#        
#
#
#
#
#
#    