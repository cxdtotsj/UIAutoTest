import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import os

# Base URL
BASE_URL = "https://dt-dev.arctron.cn"

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# logger path
LOG_PATH = os.path.join(BASE_DIR, 'logs')
if not os.path.isdir(LOG_PATH):
    os.makedirs(LOG_PATH)

# Driver path
DRIVER_PATH = os.path.join(BASE_DIR, 'drivers')
CHROME_PATH = os.path.join(DRIVER_PATH, 'chromedriver.exe')
FIREFOX_PATH = os.path.join(DRIVER_PATH, 'geckodriver.exe')

# ScreenShot path
SCREEN_PATH = os.path.join(BASE_DIR, 'screen')