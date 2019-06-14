import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base.base_page import BasePage
from selenium.webdriver.common.by import By
from base.drivers import Drivers

class LoginPageLocators:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN = (By.XPATH, "//button")
    LOGIN_USER = (By.XPATH, "//span[text()='xdchenadmin@admin']")


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locators = LoginPageLocators
        super(LoginPage, self).__init__(driver)
    
    def enter_user(self, username):
        self.getElement(self.locators.USERNAME)
        self.send_keys(self.locators.USERNAME, username)
    
    def enter_password(self, password):
        self.getElement(self.locators.PASSWORD)
        self.send_keys(self.locators.PASSWORD, password)
    
    def click_login_button(self):
        self.getElement(self.locators.LOGIN).click()
    
    def login(self, username, password):
        self.enter_user(username)
        self.enter_password(password)
        self.click_login_button()
    
    def login_success_user(self, username, password):
        self.login(username, password)
        return self.getElement(self.locators.LOGIN_USER).text
    
if __name__ == '__main__':
    driver = Drivers("chrome").driver
    page = LoginPage(driver)
    page.open("/admin/")
    name = page.login_success_user("xdchenadmin@admin", "12345678")
    print(name)
