import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login import LoginPage
from base.drivers import Drivers
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = Drivers('remote').driver
        self.login_page = LoginPage(self.driver)
        self.login_page.open("/admin/")

    def test_check_login_name(self):
        login_info = ("xdchenadmin@admin", "12345678")
        self.assertEqual(self.login_page.login_success_user(*login_info), "xdchenadmin@admin")
    
    def tearDown(self):
        self.driver.quit()