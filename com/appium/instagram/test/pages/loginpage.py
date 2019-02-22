from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from com.appium.instagram.test.setup.devicedriver import DeviceDriver
from com.appium.instagram.test.utils import constants
from com.appium.instagram.test.utils.utils import DeviceDriverUtils


class LoginPage(object):
    def __init__(self):
        self.driver = DeviceDriver().driver
        self.wait = WebDriverWait(self.driver, constants.WAIT_30_SECOND)

    _app_by_id = constants.APP_PKG + constants.BY_ID
    _android_by_id = constants.ANDROID_PKG + constants.BY_ID

    _edt_login = (By.ID, _app_by_id + 'login_username')
    _edt_password = (By.ID, _app_by_id + 'password')
    _btn_login = (By.ID, 'button_text')

    # Set account email on Login page
    def set_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self._edt_login))
        self.driver.find_element(*self._edt_login).set_value(email)

    # Set account password on Login page
    def set_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self._edt_password))
        self.driver.find_element(*self._edt_password).set_value(password)

    # Click login button on Login page
    def click_login_btn(self):
        self.wait.until(EC.visibility_of_element_located(self._btn_login))
        DeviceDriverUtils().tap(self.driver.find_element(*self._btn_login))

    # Login to application
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_btn()
        self.wait.until(
            EC.invisibility_of_element(self._btn_login))

