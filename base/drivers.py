#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : bearchen
# @Email  : cxdtsj@gmail.com

import os
from selenium import webdriver
from utils.logger import Logger
from configs.config import DRIVER_PATH

logger = Logger("Drivers").getlog()
chrome_path = os.path.join(DRIVER_PATH, 'chromedriver.exe')

class Drivers:
    
    def __init__(self, brower):
        if brower =='Chrome' or brower =='chrome' or brower =='Ch' or brower=='ch':
            driver = webdriver.Chrome(executable_path=chrome_path)
            logger.info("启动Chrome浏览器")
        elif brower =='firefox' or brower =='Firefox' or brower =='f' or brower =='F':
            driver = webdriver.Firefox()
            logger.info("启动Firefox浏览器")
        elif brower =='Ie' or brower =='ie' or brower =='i' or brower=='I':
            driver = webdriver.Ie()
            logger.info("启动IE浏览器")
        else:
            raise NameError("只能输入firefox,Ie,Chrome")
            logger.error(brower)
        self.driver = driver
            