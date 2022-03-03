import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from POM.Keep_In_Touch import Keep_In_Touch
from POM.Signin import SignIn


class UnitTest_Keep_In_Touch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(SignIn.url)

    def test_Facebook(self):
        driver = self.driver
        driver.execute_script(Keep_In_Touch.scroll)
        driver.find_element(By.XPATH, Keep_In_Touch.connectWithUs1 ).click()
        handles = driver.window_handles
        # switch to child window
        driver.switch_to.window(handles[1])
        time.sleep(3)
        driver.switch_to.window(handles[0])

    def test_Twitter(self):
        driver = self.driver
        driver.execute_script(Keep_In_Touch.scroll)
        driver.find_element(By.XPATH, Keep_In_Touch.connectWithUs2 ).click()
        handles = driver.window_handles
        # switch to child window
        driver.switch_to.window(handles[1])
        time.sleep(3)
        driver.switch_to.window(handles[0])

    def test_Youtube(self):
        driver = self.driver
        driver.execute_script(Keep_In_Touch.scroll)
        driver.find_element(By.XPATH, Keep_In_Touch.connectWithUs3).click()
        handles = driver.window_handles
        # switch to child window
        driver.switch_to.window(handles[1])
        time.sleep(3)
        driver.switch_to.window(handles[0])

    def test_Instagram(self):
        driver = self.driver
        driver.execute_script(Keep_In_Touch.scroll)
        driver.find_element(By.XPATH, Keep_In_Touch.connectWithUs4).click()
        handles = driver.window_handles
        # switch to child window
        driver.switch_to.window(handles[1])
        time.sleep(3)
        driver.switch_to.window(handles[0])

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()
