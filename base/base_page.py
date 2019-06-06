from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from utils.logger import Logger
from configs.config import BASE_URL

logger = Logger("BasePage").getlog()

class BasePage:
    def __init__(self, driver, base_url=None):
        if base_url is None:
            self.base_url = BASE_URL
        else:
            self.base_url = base_url
        self.driver = driver
        self.timeout = 10
    
    def open(self, url=None):
        if url is not None:
            url = self.base_url + url
        else:
            url = self.base_url
        self.driver.get(url)
        self.driver.maximize_window()
    
    def quit(self):
        self.driver.quit()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url
    
    def getElement(self, locator):
        # 显示等待
        # element = WebDriverWait(self.driver, self.timeout).until(lambda driver: driver.find_element(*locator))
        element = self.driver.find_element(*locator)
        return element
    
    def getElements(self, locator):
        # 显示等待
        # elements = WebDriverWait(self.driver, self.timeout).until(lambda driver: driver.find_elements(*locator))
        elements = self.driver.find_element(*locator)
        return elements
    
    def send_keys(self, locator, value):
        try:
            el = self.getElement(locator)
            # 输入框存在默认的value值
            el.send_keys(Keys.CONTROL, 'a')
            el.send_keys(Keys.DELETE)
            # 输入框不存在默认值
            # el.clear()
            el.send_keys(value)
        except Exception as e:
            # print(f"未找到{locator}")
            # print(f"error is: {e}")
            logger.error(f"未找到: {locator}")
            logger.critical(f"异常为: {e}")
    
    def click(self, locator):
        try:
            self.getElement(locator).click()
        except Exception as e:
            # print(f"未找到{locator}")
            # print(f"error is: {e}")
            logger.debug(locator)
            logger.error(e)