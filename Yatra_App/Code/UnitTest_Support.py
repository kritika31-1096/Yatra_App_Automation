import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from POM.Signin import SignIn
from POM.Support import Support


class UnitTest_Support(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(SignIn.url)

    def test_Support_RefundLink(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        mouse_hover = driver.find_element(By.XPATH, Support.mouseHover)
        # ====== hover over support link ============
        action.move_to_element(mouse_hover).perform()
        # ======= click on Check your Refund link ========
        driver.find_element(By.XPATH, Support.link1).click()
        # ======= check whether navigated to that page or not ====
        try:
            assert Support.rlText in driver.title
            print(driver.find_element(By.TAG_NAME, Support.rlTabName).text)
        except AssertionError as e:
            print(Support.aFail, e)
        driver.back()

    def test_Support_ContactUs(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====== hover over support link ============
        mouse_hover = driver.find_element(By.XPATH, Support.mouseHover)
        action.move_to_element(mouse_hover).perform()
        # ======= click on Contact us ========
        driver.find_element(By.XPATH, Support.link2).click()
        # ======= check whether navigated to that page or not =========
        try:
            ul_text = driver.find_element(By.XPATH, Support.cuXpath).text
            assert Support.cuText in ul_text
            print(ul_text)
        except AssertionError as e:
            print(Support.aFail, e)
        driver.back()

    def test_Support_CompleteBooking(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====== hover over support link ============
        mouse_hover = driver.find_element(By.XPATH, Support.mouseHover)
        action.move_to_element(mouse_hover).perform()
        # ======= click on Complete Booking ========
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, Support.link3).click()
        # ======= check whether navigated to that page or not =======
        try:
            ul_text = driver.find_element(By.XPATH, Support.cbXpath).text
            assert Support.cbText in ul_text
            print(ul_text)
        except AssertionError as e:
            print(Support.aFail, e)
        driver.back()

    def test_Support_MakePayment(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====== hover over support link ============
        mouse_hover = driver.find_element(By.XPATH, Support.mouseHover)
        action.move_to_element(mouse_hover).perform()
        # ======= click on Make a Payment ========
        driver.find_element(By.XPATH, Support.link4).click()
        # ======= check whether navigated to that page or not ======
        try:
            ul_text = driver.find_element(By.XPATH, Support.mapText).text
            assert Support.mapText in ul_text
            print(ul_text)
        except AssertionError as e:
            print(Support.aFail, e)
        driver.back()

    def test_Support_CancellationCharge(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====== hover over support link ============
        mouse_hover = driver.find_element(By.XPATH, Support.mouseHover)
        action.move_to_element(mouse_hover).perform()
        # ======= click on Flights Cancellation Charges ========
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, Support.link5).click()
        # ======= check whether navigated to that page or not =========
        try:
            ul_text = driver.find_element(By.CLASS_NAME, Support.fccClassName).text
            assert Support.fccText in ul_text
            print(ul_text)
        except AssertionError as e:
            print(Support.aFail, e)
        driver.back()

    def test_Support_HolidayBooking(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====== hover over support link ============
        mouse_hover = driver.find_element(By.XPATH, Support.mouseHover)
        action.move_to_element(mouse_hover).perform()
        # ======= click on Complete Holiday Booking ========
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, Support.link6).click()
        # ======= check whether navigated to that page or not ========
        try:
            ul_text = driver.find_element(By.CLASS_NAME, Support.chbClassName).text
            assert Support.chbText in ul_text
            print(ul_text)
        except AssertionError as e:
            print(Support.aFail, e)
        driver.back()

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()
