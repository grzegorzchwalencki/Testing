from base_page import BasePage
from selenium.webdriver.common.by import By


class Locator:
    """Locators form Create Account Page"""
    FIRST_NANE = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    PASSWORD_CONFIRMATION = (By.ID, "password_confirmation")



class CreateAccountPage(BasePage):
    
    pass