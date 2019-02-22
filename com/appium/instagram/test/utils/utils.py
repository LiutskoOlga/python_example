from appium.webdriver.common.touch_action import TouchAction

from com.appium.instagram.test.setup.devicedriver import DeviceDriver


class DeviceDriverUtils:
    def __init__(self):
        self.driver = DeviceDriver.driver

    # Tap on element
    def tap(self, element):
        TouchAction(self.driver).tap(element).perform()

    # Swipe element on screen
    def swipe(self):
        self.driver.swipe(50, 50, 50, 50)