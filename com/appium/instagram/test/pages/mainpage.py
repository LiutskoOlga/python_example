from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from com.appium.instagram.test.setup.devicedriver import DeviceDriver
from com.appium.instagram.test.utils import constants


class MainPage(object):
    def __init__(self):
        self.driver = DeviceDriver().driver
        self.wait = WebDriverWait(self.driver, constants.WAIT_30_SECOND)

    _app_by_id = constants.APP_PKG + constants.BY_ID
    _android_by_id = constants.ANDROID_PKG + constants.BY_ID

    _btn_avatar = (By.ID, _app_by_id + 'tab_bar')

    # Verify Element
    def verify_main_page_open(self):
        self.wait.until(EC.visibility_of_element_located(self._btn_avatar))
        return self.driver.find_element(*self._btn_avatar).is_displayed()
