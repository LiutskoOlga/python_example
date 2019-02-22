import unittest

from com.appium.instagram.test.pages.loginpage import LoginPage
from com.appium.instagram.test.pages.mainpage import MainPage
from com.appium.instagram.test.pages.landingpage import LandingPage
from com.appium.instagram.test.setup.devicedriver import DeviceDriver
from com.appium.instagram.test.utils import constants


class TestSuite(unittest.TestCase):
    def setUp(self):
        DeviceDriver.get_driver()

    def test_correct_login(self):
        landingPage = LandingPage()
        landingPage.click_login_btn()
        loginPage = LoginPage()
        loginPage.login(constants.USER_GMAIL_EMAIL, constants.USER_GMAIL_PWD)
        mainPage = MainPage()
        self.assertTrue(mainPage.verify_main_page_open())

    def tearDown(self):
        DeviceDriver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
    unittest.TextTestRunner(verbosity=2).run(suite)