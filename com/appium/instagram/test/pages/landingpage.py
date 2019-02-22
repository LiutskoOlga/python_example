from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from com.appium.instagram.test.setup.devicedriver import DeviceDriver
from com.appium.instagram.test.utils import constants
from com.appium.instagram.test.utils.utils import DeviceDriverUtils


class LandingPage(object):
    def __init__(self):
        self.driver = DeviceDriver().driver
        self.wait = WebDriverWait(self.driver, constants.WAIT_1_SECOND)

    _app_by_id = constants.APP_PKG + constants.BY_ID
    _android_by_id = constants.ANDROID_PKG + constants.BY_ID

    _btn_login = (By.ID, _app_by_id + 'log_in_button')

    # Click login button on Landing page
    def click_login_btn(self):
        self.wait.until(EC.visibility_of_element_located(self._btn_login))
        DeviceDriverUtils().tap(self.driver.find_element(*self._btn_login))