#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : bearchen
# @Email  : cxdtsj@gmail.com

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
import time
import os
from configs.config import LOG_PATH

class Logger:
    def __init__(self, logger):
        
        # 创建logger文件
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handle，用来写入日志文件
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        log_name = os.path.join(LOG_PATH, now) + '.log'

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    def getlog(self):
        return self.logger

if __name__ == "__main__":
    logger = Logger("Logger")
    logger.getlog()