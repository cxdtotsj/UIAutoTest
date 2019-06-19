import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login import LoginPage
from base.drivers import DriversRemote, Drivers
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        # self.driver = DriversRemote('chrome').driver
        self.driver = Drivers('remote', 'chrome')
        self.login_page = LoginPage(self.driver)
        self.login_page.open("/admin/")

    def test_check_login_name(self):
        login_info = ("xdchenadmin@admin", "12345678")
        print(self.login_page.login_success_user())
        self.assertEqual(self.login_page.login_success_user(*login_info), "xdchenadmin@admin")
    
    def tearDown(self):
        self.driver.quit()