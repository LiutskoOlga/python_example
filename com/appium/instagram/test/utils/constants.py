import os

WAIT_1_SECOND = 1
WAIT_2_SECOND = 2
WAIT_5_SECOND = 5
WAIT_10_SECOND = 10
WAIT_30_SECOND = 30


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
APP_NAME = BASE_DIR + '/apps/instagram.apk'
PLATFORM_NAME = 'Android'
DEVICE_NAME = 'Galaxy A7'
PLATFORM_VERSION = '8.0'
APP_PACKAGE = 'com.instagram.android'
HOST = 'http://127.0.0.1:4723/wd/hub'
APP_ACTIVITY = 'com.instagram.android.activity.MainTabActivity'
AUTOMATION_NAME = 'uiautomator2'
FULL_RESET = 'true'

USER_GMAIL_EMAIL = 'charliekillo216@gmail.com'
USER_GMAIL_PWD = 'zaxscdvf1'

# Locators
BY_ID = ':id/'

# Packages
APP_PKG = 'com.instagram.android'
ANDROID_PKG = 'android'

