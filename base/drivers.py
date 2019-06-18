#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : bearchen
# @Email  : cxdtsj@gmail.com

import os
from selenium import webdriver
from utils.logger import Logger
from configs.config import CHROME_PATH,FIREFOX_PATH

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
class Drivers:
    def __init__(self, brower):
        if brower =='Chrome' or brower =='chrome' or brower =='Ch' or brower=='ch':
            option = webdriver.ChromeOptions()
            option.add_argument("headless")
            # 禁用GPU硬件加速，防止出现BUG
            option.add_argument("disable-gpu")
            driver = webdriver.Chrome(executable_path=CHROME_PATH, chrome_options=option)
            logger.info("启动 Chrome--Headless 浏览器")
        elif brower =='firefox' or brower =='Firefox' or brower =='f' or brower =='F':
            option = webdriver.FirefoxOptions()
            option.add_argument("headless")
            # 禁用GPU硬件加速，防止出现BUG
            option.add_argument("disable-gpu")
            driver = webdriver.Firefox(executable_path=FIREFOX_PATH, firefox_options=option)
            logger.info("启动 Firefox-Headless 浏览器")
        elif brower =='Ie' or brower =='ie' or brower =='i' or brower=='I':
            option = webdriver.IeOptions()
            option.add_argument("headless")
            # 禁用GPU硬件加速，防止出现BUG
            option.add_argument("disable-gpu")
            driver = webdriver.Ie(ie_options=option)
            logger.info("启动 IE-Headless 浏览器")
        else:
            raise NameError("只能输入firefox,Ie,Chrome")
            logger.error(brower)
        self.driver = driver