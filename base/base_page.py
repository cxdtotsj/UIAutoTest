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
        # 设定隐式等待
        self.driver.implicitly_wait(self.timeout)
        self.timeout = 10
    
    def open(self, url=None):
        """打开网站"""
        if url is not None:
            url = self.base_url + url
        else:
            url = self.base_url
        self.driver.get(url)
        self.driver.maximize_window()
    
    def quit(self):
        """浏览器退出"""
        self.driver.quit()

    def get_title(self):
        """获取当前title"""
        return self.driver.title

    def get_url(self):
        """获取当前页面的URL"""
        return self.driver.current_url
    
    def getElement(self, locator):
        """获取element"""
        try:
            element = self.driver.find_element(*locator)
        except Exception as e:
            logger.error(f"未找到元素: {locator}")
            logger.critical(f"异常为: {e}")
        return element
    
    def getElements(self, locator):
        """获取elements"""
        try:
            elements = self.driver.find_element(*locator)
        except Exception as e:
            logger.error(f"未找到元素: {locator}")
            logger.critical(f"异常为: {e}")
        return elements
    
    def send_keys(self, locator, value):
        """文本框输入"""
        el = self.getElement(locator)
        # 输入框存在默认的value值
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(Keys.DELETE)
        # 输入框不存在默认值
        # el.clear()

        el.send_keys(value)
    
    def click(self, locator):
        """点击按钮"""
        self.getElement(locator).click()