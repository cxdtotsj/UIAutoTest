import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from base.drivers import Drivers
from base.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.login_info import get_token

driver = Drivers("firefox").driver
bs = BasePage(driver)

uname = (By.NAME, "username")
password = (By.NAME, "password")
login_button = (By.XPATH, "//button")
device_manage = (By.XPATH, "//ul[@class='el-menu']//span[text()='设备管理']")

gateway_add = (By.XPATH, "//span[text()='新建设备']")

# 登录
# bs.open("/admin/")
# bs.send_keys(uname, "xdchenadmin@admin")
# bs.send_keys(password, "12345678")
# bs.click(login_button)
# time.sleep(3)
# bs.quit()


# 免登陆
token = get_token()
bs.open("/admin/#/devicelist/gate")
bs.login_token(token)
time.sleep(3)
bs.quit()