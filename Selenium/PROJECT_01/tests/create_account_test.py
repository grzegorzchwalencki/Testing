import unittest
from ddt import ddt, data, unpack
from tests.base_test import BaseTest
from pages.home_page import HomePage


class CreateAccountTest(BaseTest):
    """Create Account tests"""
    def setUp(self):
        super().setUp()
        self.create_account_page = self.home_page.click_create_account()

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
        # a) Find all error statements

        # b) Check that the number of errors is equal to 1.

        # c) Check if error message is "This is required field"

        # d) Verify that the location of the error message is correct - below the First Name input field

    def test_no_lastname_entered(self):
        """Test create account with no last name entered"""
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
        self.create_account_page.enter_password_con("Testtest!")
        # 7. Click button to create account
        self.create_account_page.click_create_button()

        # EXPECTED RESULT
        





    