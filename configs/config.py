import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# logger path
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# Driver path
DRIVER_PATH = os.path.join(BASE_DIR, 'drivers')