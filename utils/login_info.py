import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from utils.logger import Logger

logger = Logger("login_info")

def get_token(url=None, data=None, **kwargs):
    if not url and data:
        url = url
        data = data
    else:
        url = "https://dt-dev.arctron.cn/api/user/login"
        data = {
            "email": "xdchenadmin@admin",
            "password": "12345678"
        }
        try:
            res = requests.post(url=url, data=data, **kwargs)
            token = res.json()["token"]
        except (KeyError, Exception) as err:
            logger.error(f"获取Token异常: {err}")
        return token