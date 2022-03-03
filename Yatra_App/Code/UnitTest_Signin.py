# import unittest
import unittest
# import webdriver from selenium
from selenium import webdriver
# import BY class
from selenium.webdriver.common.by import By
# import Signin from POM
from POM.Signin import SignIn


class UnitTest_Signin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get(SignIn.url)

    def test_Signin(self):
        driver = self.driver
        driver.find_element(By.XPATH, SignIn.myAccount).click()
        driver.find_element(By.XPATH, SignIn.signInBtn).click()
        driver.find_element(By.ID, SignIn.login).send_keys(SignIn.mobNo)
        driver.find_element(By.ID, SignIn.continueBtn).click()
        driver.find_element(By.XPATH, SignIn.pwdLink).click()
        driver.find_element(By.XPATH, SignIn.pwd).send_keys(SignIn.pwdLogin)
        driver.find_element(By.ID, SignIn.loginBtn).click()

    def tearDown(self):
        driver = self.driver
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()
