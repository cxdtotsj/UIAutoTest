#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : bearchen
# @Email  : cxdtsj@gmail.com

import os
from selenium import webdriver
from utils.logger import Logger
from config import CHROME_PATH,FIREFOX_PATH

logger = Logger("Drivers").getlog()

# class Drivers:
    
#     def __init__(self, brower):
#         if brower =='Chrome' or brower =='chrome' or brower =='Ch' or brower=='ch':
#             driver = webdriver.Chrome(executable_path=CHROME_PATH)
#             logger.info("启动Chrome浏览器")
#         elif brower =='firefox' or brower =='Firefox' or brower =='f' or brower =='F':
#             driver = webdriver.Firefox(executable_path=FIREFOX_PATH)
#             logger.info("启动Firefox浏览器")
#         elif brower =='Ie' or brower =='ie' or brower =='i' or brower=='I':
#             driver = webdriver.Ie()
#             logger.info("启动IE浏览器")
#         else:
#             raise NameError("只能输入firefox,Ie,Chrome")
#             logger.error(brower)
#         self.driver = driver
            
    # def get_driver(self):
    #     return self.driver


## selenium Headless
# class Drivers:
#     def __init__(self, brower):
#         if brower =='Chrome' or brower =='chrome' or brower =='Ch' or brower=='ch':
#             option = webdriver.ChromeOptions()
#             option.add_argument("headless")
#             # 禁用GPU硬件加速，防止出现BUG
#             option.add_argument("disable-gpu")
#             driver = webdriver.Chrome(executable_path=CHROME_PATH, options=option)
#             logger.info("启动 Chrome--Headless 浏览器")
#         elif brower =='firefox' or brower =='Firefox' or brower =='f' or brower =='F':
#             option = webdriver.FirefoxOptions()
#             option.add_argument("headless")
#             # 禁用GPU硬件加速，防止出现BUG
#             option.add_argument("disable-gpu")
#             driver = webdriver.Firefox(executable_path=FIREFOX_PATH, options=option)
#             logger.info("启动 Firefox-Headless 浏览器")
#         elif brower =='Ie' or brower =='ie' or brower =='i' or brower=='I':
#             option = webdriver.IeOptions()
#             option.add_argument("headless")
#             # 禁用GPU硬件加速，防止出现BUG
#             option.add_argument("disable-gpu")
#             driver = webdriver.Ie(options=option)
#             logger.info("启动 IE-Headless 浏览器")
#         else:
#             raise NameError("只能输入firefox,Ie,Chrome")
#             logger.error(brower)
#         self.driver = driver

class Drivers:
    def __init__(self, brower):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('disable-gpu')
        if brower == 'remote':
            chrome_capabilities = {
                "browserName": "chrome",
                "platform": "LINUX",
                "version": "75.0.3770.80",
                "javascriptEnabled": True,
                "webdriver.chrome.driver": CHROME_PATH
            }
            driver = webdriver.Remote(command_executor='http://10.42.0.8:4444/wd/hub', desired_capabilities=chrome_capabilities, options=option)
            logger.info("remote chrome 启动成功")
            self.driver = driver
