import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from POM.Nav_Bar import Nav_Bar
from POM.Signin import SignIn


class UnitTest_Nav_Bar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(SignIn.url)

    def test_All(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # ====== Handling Alert ========
        # alert = Alert(driver)
        # accept the alert
        # alert.dismiss()

        # === finding all the Nav Bar elements ===
        all = driver.find_elements(By.XPATH, Nav_Bar.allXpath)

        for i in range(5):
            all[i].click()
            time.sleep(3)
            assert driver.current_url.split('/')[-1] in Nav_Bar.url_lst[i], Nav_Bar.errorMsg
            print(driver.current_url.split('/')[-1], '-', Nav_Bar.url_lst[i])
            print(driver.find_element(By.CLASS_NAME, Nav_Bar.mainHeading).text)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()
