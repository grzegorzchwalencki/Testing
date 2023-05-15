from base_page import BasePage
from selenium.webdriver.common.by import By


class Locator:
    """Locators form Create Account Page"""
    FIRST_NANE = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    PASSWORD_CONFIRMATION = (By.ID, "password_confirmation")
    CREATE_BUTTON = (By.XPATH, '//button[@title="Create an Account"]')
    NEWSLETTER_CHECKBOX = (By.XPATH, '//label[@for="is_subscribed"]')



class CreateAccountPage(BasePage):
    """Create Account Page"""
    def _verify_page(self):
        pass

    def enter_firstname(self, username):
        # Find username field
        el_first_name = self.driver.find_element(Locator.FIRST_NANE)
        # Enter first name
        el_first_name.send_keys(username)

    def enter_lastname(self, lastname):
        # Find lastname field
        el_last_name = self.driver.find_element(Locator.LAST_NAME)
        # Enter last name
        el_last_name.send_keys(lastname)

    def enter_email(self, email):
        # Find email field
        el_email = self.driver.find_element(Locator.EMAIL)
        # Enter email
        el_email.send_keys(email)

    def enter_password(self, password):
        # Find password field
        el_password = self.driver.find_element(Locator.PASSWORD)
        # Enter password
        el_password.send_keys(password)

    def enter_password_con(self, password_con):
        # Find password confirmation field
        el_password_con = self.driver.find_element(Locator.PASSWORD_CONFIRMATION)
        # Enter password confirmation
        el_password_con.send_keys(password_con)
    
    def click_create_button(self):
        # Find create button
        el_create_button = self.driver.find_element(Locator.CREATE_BUTTON)
        # Click it!
        el_create_button.click()
    
    def newsletter_accept(self):
        # Find checkbox to accept newsletter
        el_newsletter = self.driver.find_element(Locator.NEWSLETTER_CHECKBOX)
        # Click checkbox
        el_newsletter.click()
