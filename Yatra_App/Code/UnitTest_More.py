import logging
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from POM.Signin import SignIn
from POM.More import More


class UnitTest_More(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(SignIn.url)

    def test_More_Cabs(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # ====================================================================#
        # hover over more link
        action = ActionChains(driver)
        mouse_hover = driver.find_element(By.XPATH, More.moreEle)
        action.move_to_element(mouse_hover).perform()
        # ==== click on cabs ====
        driver.find_element(By.XPATH, More.cabs).click()
        try:
            assert driver.find_element(By.ID, More.cabsId).is_displayed()
            print("Icon located")
        except NoSuchElementException as e:
            print("Cab icon is not visible", e)
            # logging.error("logo verification failed")

    def test_More_Gift(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====================================================================#
        # hover over more link
        mouse_hover = driver.find_element(By.XPATH, More.moreEle)
        action.move_to_element(mouse_hover).perform()
        # click on gifts voucher
        driver.find_element(By.XPATH, More.giftVoucher).click()
        handles = driver.window_handles
        # switch to child window
        driver.switch_to.window(handles[1])
        try:
            assert More.giftVoucherText in driver.title
            print("Successfully navigated to Gift Vouchers page")
        except AssertionError as e:
            print("Gift page not correct", e)
        # driver.close()
        driver.switch_to.window(handles[0])

    def test_More_Freight(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====================================================================#
        # hover over more link
        mouse_hover = driver.find_element(By.XPATH, More.moreEle)
        action.move_to_element(mouse_hover).perform()
        # click on freight
        driver.find_element(By.XPATH, More.freight).click()
        handles = driver.window_handles
        # switch to child window
        driver.switch_to.window(handles[1])
        try:
            assert More.freightText in driver.title
            print("Successfully navigated to Freight page")
        except AssertionError as e:
            print("Freight page not correct", e)
        # driver.close()
        driver.switch_to.window(handles[0])

    def test_More_Adventures(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====================================================================#
        # hover over more link
        mouse_hover = driver.find_element(By.XPATH, More.moreEle)
        action.move_to_element(mouse_hover).perform()
        # click on adventure
        driver.find_element(By.XPATH, More.adventures).click()
        try:
            assert driver.find_element(By.CLASS_NAME, More.adventuresLogo).is_displayed()
            print("Advertisement Tour addd. logo id displayed")
        except NoSuchElementException as e:
            print("Adventure page not correct", e)
        driver.back()

    def test_More_Activities(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====================================================================#
        # hover over more link
        mouse_hover = driver.find_element(By.XPATH, More.moreEle)
        action.move_to_element(mouse_hover).perform()
        # click on activities
        driver.find_element(By.XPATH, More.activities).click()
        try:
            assert driver.find_element(By.ID, More.activitiesId).is_displayed()
            print("Activities icon is displayed")
        except NoSuchElementException as e:
            print("Activities page not correct", e)

    def test_More_Monuments(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====================================================================#
        # hover over more link
        mouse_hover = driver.find_element(By.XPATH, More.moreEle)
        action.move_to_element(mouse_hover).perform()
        # click on monuments
        driver.find_element(By.XPATH, More.monuments).click()
        try:
            assert driver.find_element(By.ID, More.monumentsId).is_displayed()
            print("Monuments icon is displayed")
        except NoSuchElementException as e:
            print("Monumnets page not correct", e)

    def test_More_Xplore(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====================================================================#
        # hover over more link
        mouse_hover = driver.find_element(By.XPATH, More.moreEle)
        action.move_to_element(mouse_hover).perform()
        # click on xplore
        driver.find_element(By.XPATH, More.xplore).click()
        try:
            assert More.xploreText in driver.title
            print("Successfully navigated to Xplore page")
        except AssertionError as e:
            print("Xplore page not correct", e)
        driver.back()

    def test_More_CharFlight(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====================================================================#
        # hover over more link
        mouse_hover = driver.find_element(By.XPATH, More.moreEle)
        action.move_to_element(mouse_hover).perform()
        # click on charter flights
        driver.find_element(By.XPATH, More.charterFlights).click()

        try:
            assert driver.find_element(By.ID, More.charterFlightsText).is_displayed()
            print("Charter Flights icon is displayed")
        except NoSuchElementException as e:
            print("Charter flight page not correct", e)

    def test_More_Trains(self):
        driver = self.driver
        driver.implicitly_wait(5)
        action = ActionChains(driver)
        # ====================================================================#
        # hover over more link
        mouse_hover = driver.find_element(By.XPATH, More.moreEle)
        action.move_to_element(mouse_hover).perform()
        # click on trains
        driver.find_element(By.XPATH, More.trains).click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.XPATH, More.trainOk).click()
        try:
            assert driver.find_element(By.ID, More.trainsId).is_displayed()
            print("Train icon located")
            assert More.trainText in driver.find_element(By.XPATH, More.trainTextX).text
            print("main heading is displayed")
        except NoSuchElementException as e:
            print("Train page not correct", e)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()
