import unittest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from POM.Signin import SignIn
from POM.NavBar_Settings import NavBar_Settings


class UnitTest_NavBar_Settings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(SignIn.url)

    def test_Settings(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # clicking on Offers and Yatra For Business
        allSettings = driver.find_elements(By.XPATH, NavBar_Settings.allSettingsX)
        for i in range(2, 4):
            allSettings[i].click()
            title = driver.title
            # verifying it by the title of the page
            try:
                assert title in NavBar_Settings.titleList
                print(NavBar_Settings.aPass, title)
            except AssertionError:
                print(NavBar_Settings.aFail)
            driver.back()
            allSettings = driver.find_elements(By.XPATH, NavBar_Settings.allSettingsX)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()
