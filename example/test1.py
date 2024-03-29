import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configs.config import DRIVER_PATH
import os
import time
from base.base_page import BasePage
from utils.logger import Logger
from utils.login_info import get_token


# driver = webdriver.Chrome()

# element = driver.find_element_by_tag_name()

# driver.find_element()

logger = Logger("test1").getlog()

token = get_token()

uname = (By.NAME, "username1")
password = (By.NAME, "password1")
login_button = (By.XPATH, "//button")

chrome_path = os.path.join(DRIVER_PATH, 'chromedriver.exe')
firefox_path = os.path.join(DRIVER_PATH, 'geckodriver.exe')
driver = webdriver.Firefox(executable_path=firefox_path)

driver.get("https://dt-dev.arctron.cn/admin/#")
driver.maximize_window()

driver.execute_script('localStorage.setItem("TOKEN", %s);' % token)
# driver.execute_script('console.log("123")')
driver.refresh()

driver.get("https://dt-dev.arctron.cn/admin/#/devicelist/gate")

time.sleep(3)

# e = driver.find_element_by_name("username1")
# e.clear()

# time.sleep(3)

# e.send_keys("abc")



# bs = BasePage(driver, "https://dt-dev.arctron.cn/admin/")
# logger.info("启动Chrome浏览器成功")
# bs.open()
# logger.info("输入账号")
# bs.send_keys(uname, "admin@admin")
# logger.info("输入密码")
# bs.send_keys(password, "abc123")
# bs.click(login_button)
# logger.info("登录成功")
# time.sleep(2)
# bs.quit()
# logger.info("浏览器退出成功")