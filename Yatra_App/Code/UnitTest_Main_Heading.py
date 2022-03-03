import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from POM.Signin import SignIn
from POM.Main_Heading import Main_Heading


class UnitTest_Main_Heading(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(SignIn.url)

    def test_RecentSearch(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # ==== Recent Search ====
        # ==== if nothing is in search history then it will not able to locate the Recent Search
        recSech = driver.find_element(By.XPATH, Main_Heading.research)
        try:
            assert Main_Heading.researchText in recSech.text
            print(Main_Heading.aPass, recSech.text)
        except AssertionError as e:
            print(Main_Heading.aFail, e)

    def test_CountryOpenToTravel(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # ==== Countries Open for Travel ====
        contTrav = driver.find_element(By.XPATH, Main_Heading.openTravel)
        h = str(contTrav.location['y'])
        driver.execute_script("window.scrollTo(0," + h + ")")
        time.sleep(5)
        try:
            assert Main_Heading.openTravelText in contTrav.text
            print(Main_Heading.aPass, contTrav.text)
        except AssertionError as e:
            print(Main_Heading.aFail, e)

    def test_YatraSpecial(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # ==== Yatra Specials ====
        yatSpe = driver.find_element(By.XPATH, Main_Heading.yatSpecial)
        h = str(yatSpe.location['y'])
        driver.execute_script("window.scrollTo(0," + h + ")")
        time.sleep(5)
        try:
            assert Main_Heading.yatSpecialText in yatSpe.text
            print(Main_Heading.aPass, yatSpe.text)
        except AssertionError as e:
            print(Main_Heading.aFail, e)

    def test_PopDomesFlight(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # ==== Popular Domestic Flight Routes ====
        popuDom = driver.find_element(By.XPATH, Main_Heading.popDomestic)
        h = str(popuDom.location['y'])
        driver.execute_script("window.scrollTo(0," + h + ")")
        time.sleep(5)
        try:
            assert Main_Heading.popDomesticText in popuDom.text
            print(Main_Heading.aPass, popuDom.text)
        except AssertionError as e:
            print(Main_Heading.aFail, e)

    def test_PopInternaFlight(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # ==== Popular International Flight Routes ====
        popuInt = driver.find_element(By.XPATH, Main_Heading.popInternational)
        h = str(popuInt.location['y'])
        driver.execute_script("window.scrollTo(0," + h + ")")
        time.sleep(5)
        try:
            assert Main_Heading.popInternationalText in popuInt.text
            print(Main_Heading.aPass, popuInt.text)
        except AssertionError as e:
            print(Main_Heading.aFail, e)

    def test_CopyRight(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # ==== Copyright © 2022 Yatra Online Private Limited ====
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        copyRight = driver.find_element(By.XPATH, Main_Heading.copyR)
        try:
            assert Main_Heading.copyRText in copyRight.text
            print(Main_Heading.aPass, copyRight.text)
        except AssertionError as e:
            print(Main_Heading.aFail, e)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()
