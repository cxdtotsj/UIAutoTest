import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from base.drivers import Drivers
from base.base_page import BasePage
from selenium.webdriver.common.by import By

driver = Drivers("firefox").get_driver()
bs = BasePage(driver)

uname = (By.NAME, "username")
password = (By.NAME, "password")
login_button = (By.XPATH, "//button")

bs.open("/admin/")
bs.send_keys(uname, "admin@admin")
bs.send_keys(password, "abc123")
bs.click(login_button)
time.sleep(3)
bs.quit()