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


# driver = webdriver.Chrome()

# element = driver.find_element_by_tag_name()

# driver.find_element()

logger = Logger("test1").getlog()

uname = (By.NAME, "username")
password = (By.NAME, "password")
login_button = (By.XPATH, "//button")

chrome_path = os.path.join(DRIVER_PATH, 'chromedriver.exe')
driver = webdriver.Chrome(executable_path=chrome_path)



# driver.get("https://dt-dev.arctron.cn/admin/")
# driver.maximize_window()
# e = driver.find_element_by_name("username")
# e.clear()

# time.sleep(3)

# e.send_keys("abc")



# driver.find_element(*uname).clear()



bs = BasePage(driver, "https://dt-dev.arctron.cn/admin/")
logger.info("启动Chrome浏览器成功")
bs.open()
bs.send_keys(uname, "admin@admin")
logger.info("输入的账号为'admin@admin'")
bs.send_keys(password, "abc123")
logger.info("输入的密码为'abc123'")
bs.click(login_button)
logger.info("登录成功")
time.sleep(2)
bs.quit()
logger.info("浏览器退出成功")
