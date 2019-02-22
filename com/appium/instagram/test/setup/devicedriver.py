from appium import webdriver

from com.appium.instagram.test.utils import constants


class DeviceDriver():
    @staticmethod
    def set_driver():
        desired_caps = {
            'platformName': constants.PLATFORM_NAME,
            'platformVersion': constants.PLATFORM_VERSION,
            'deviceName': constants.DEVICE_NAME,
            'app': constants.APP_NAME,
            'appPackage': constants.APP_PACKAGE,
            'appActivity': constants.APP_ACTIVITY,
            'automationName': constants.AUTOMATION_NAME,
            'fullReset' : constants.FULL_RESET,
            'autoGrantPermissions' : constants.FULL_RESET,
            'clearSystemFiles': constants.FULL_RESET
        }

        try:
            DeviceDriver.driver = webdriver.Remote(constants.HOST, desired_caps)
        except Exception as e:
            raise e
        return DeviceDriver.driver

    @staticmethod
    def get_driver():
        return DeviceDriver.set_driver()

    @staticmethod
    def quit():
        DeviceDriver.driver.quit()
