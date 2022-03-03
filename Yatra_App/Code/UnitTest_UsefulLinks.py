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
from POM.UsefulLinks import UsefulLinks


class UnitTest_UsefulLinks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(SignIn.url)

    def test_Company_Useful_Links(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # === Click on Company Information ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.ciXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Company Information ->  More About Us ===
        driver.find_element(By.ID, UsefulLinks.mauId).click()
        # === Verify More About Us ===
        try:
            assert UsefulLinks.mauText in driver.find_element(By.XPATH, UsefulLinks.mauXpath).text
            print(UsefulLinks.mauPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Company Information ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.ciXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Company Information ->  Leadership Team ===
        driver.find_element(By.ID, UsefulLinks.ltId).click()
        # === Verify Leadership Team ===
        try:
            assert UsefulLinks.ltText in driver.find_element(By.XPATH, UsefulLinks.ltXpath).text
            print(UsefulLinks.ltPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Company Information ===
        driver.find_element(By.XPATH, UsefulLinks.ciXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Company Information ->  Our Products ===
        driver.find_element(By.ID, UsefulLinks.opId).click()

        try:
            e = driver.find_element(By.CLASS_NAME, UsefulLinks.opClassName)
            h = str(e.location['y'])
            driver.execute_script("window.scrollTo(0,"+h+")")
            time.sleep(3)
            assert UsefulLinks.opText in driver.find_element(By.XPATH, UsefulLinks.opXpath).text
            print(UsefulLinks.opPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Company Information ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.ciXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Company Information ->  Awards Won ===
        driver.find_element(By.ID, UsefulLinks.awId).click()

        try:
            assert UsefulLinks.awText in driver.find_element(By.XPATH, UsefulLinks.awXpath).text
            print(UsefulLinks.awPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Company Information ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.ciXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Company Information ->  Customers Testimonials ===
        driver.find_element(By.ID, UsefulLinks.ctId).click()

        try:
            assert UsefulLinks.ctText in driver.find_element(By.XPATH, UsefulLinks.ctXpath).text
            print(UsefulLinks.ctPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Company Information ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.ciXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Company Information ->  Press Release ===
        driver.find_element(By.ID, UsefulLinks.prId).click()

        try:
            assert UsefulLinks.prText in driver.find_element(By.XPATH, UsefulLinks.prXpath).text
            print(UsefulLinks.prPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

    def test_Investor_Relations(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.investorRelationXpath).click()

        try:
            assert UsefulLinks.irText in driver.find_element(By.XPATH, UsefulLinks.irXpath).text
            print(UsefulLinks.irPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

    def test_Career(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.careerXpath).click()
        print(driver.title)
        try:
            assert UsefulLinks.cText in driver.title
            print(UsefulLinks.cPrint)
        except NoSuchElementException as e:
            print(UsefulLinks.aFail, e)
        driver.back()

    def test_Yatra_for_Business(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.yfbXpath).click()

        print(driver.title)
        try:
            assert UsefulLinks.yfbText in driver.title
            print(UsefulLinks.yfbPrint)
        except NoSuchElementException as e:
            print(UsefulLinks.aFail, e)
        driver.back()

    def test_Customer_Care(self):
        # Customer Care
        driver = self.driver
        driver.implicitly_wait(5)
        # === Click on Customer Care
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.customerCareXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Customer Care ->  Support & FAQs ===
        driver.find_element(By.ID, UsefulLinks.snfId).click()

        try:
            assert UsefulLinks.snfText in driver.title
            print(UsefulLinks.snfPrint)
        except NoSuchElementException as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Customer Care ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.customerCareXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Customer Care ->  Terms & Conditions ===
        driver.find_element(By.ID, UsefulLinks.tncId).click()

        try:
            assert driver.find_element(By.XPATH, UsefulLinks.tncXpath).is_displayed()
            print(UsefulLinks.tncPrint)
        except NoSuchElementException as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Customer Care ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.customerCareXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Customer Care ->  Privacy Policy ===
        driver.find_element(By.ID, UsefulLinks.ppId).click()

        try:
            assert driver.find_element(By.XPATH, UsefulLinks.ppXpath).is_displayed()
            print(UsefulLinks.ppPrint)
        except NoSuchElementException as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Customer Care ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.customerCareXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Customer Care ->  User Agreement ===
        driver.find_element(By.ID, UsefulLinks.uaId).click()

        try:
            assert UsefulLinks.uaText in driver.find_element(By.XPATH, UsefulLinks.uaTextXpath).text
            print(UsefulLinks.uaPrint)
        except NoSuchElementException as e:
            print(UsefulLinks.aFail, e)
        driver.back()

    def text_Partner_With_Yatra(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # === Click on Partner With Yatra ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.partnerWithYatraXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Partner With Yatra ->  Travel Agent Signup ===
        driver.find_element(By.ID, UsefulLinks.tasuId).click()

        try:
            assert UsefulLinks.tasuText in driver.find_element(By.XPATH, UsefulLinks.tasuTextXpath).text
            print(UsefulLinks.tasuPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Partner With Yatra ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.partnerWithYatraXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Partner With Yatra ->  Register Your Hotel ===
        driver.find_element(By.ID, UsefulLinks.ryhId).click()

        try:
            assert driver.find_element(By.XPATH, UsefulLinks.ryhXpath).is_displayed()
            print(UsefulLinks.ryhPrint)
        except NoSuchElementException as e:
            print(UsefulLinks.aFail, e)
        driver.back()

        # === Click on Partner With Yatra ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.partnerWithYatraXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on Partner With Yatra ->  Register your HomeStay===
        driver.find_element(By.ID, UsefulLinks.ryhsId).click()

        try:
            assert UsefulLinks.ryhsText in driver.title
            print(UsefulLinks.ryhPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

    def test_More(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # === Click on More ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.moreXpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on More ->  Retails Stores ===
        driver.find_element(By.ID, UsefulLinks.rsId).click()

        try:
            assert UsefulLinks.rsText in driver.find_element(By.XPATH, UsefulLinks.rsXpath).text
            print(UsefulLinks.rsPrint)
        except AssertionError as e:
            print("page not correct", e)
        driver.back()

        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.find_element(By.XPATH, "//li[@class = 'parentLI']/a/span[text() = 'More']").click()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        # driver.find_element(By.ID, "Sitemap").click()
        #
        # try:
        #     assert "Sitemap" in driver.find_element(By.XPATH, "//div[@class = 'link-wrapper']/div/div[1]").text
        #     print("Sitemap page is displayed")
        # except NoSuchElementException as e:
        #     print("page not correct", e)
        # driver.back()

        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # driver.find_element(By.XPATH, "//li[@class = 'parentLI']/a/span[text() = 'More']").click()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        # driver.find_element(By.ID, "GiftCards").click()
        #
        # try:
        #     assert "Gift Cards" in driver.title
        #     print("Gift Cards page is displayed")
        # except AssertionError as e:
        #     print("page not correct", e)
        # driver.back()

        # === Click on More ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.more2Xpath).click()
        driver.execute_script(UsefulLinks.scroll)
        # === Click on More -> Visa Information ===
        driver.find_element(By.ID, UsefulLinks.viId).click()

        try:
            assert UsefulLinks.viText in driver.find_element(By.XPATH, UsefulLinks.viTextXpath).text
            print(UsefulLinks.viPrint)
        except AssertionError as e:
            print(UsefulLinks.aFail, e)
        driver.back()

    def test_Product_Offerings(self):
        driver = self.driver
        driver.implicitly_wait(5)
        # === Click on Product Offerings ===
        driver.execute_script(UsefulLinks.scroll)
        driver.find_element(By.XPATH, UsefulLinks.pproductOffers).click()
        driver.execute_script(UsefulLinks.scroll)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        driver.close()
        driver.quit()


if __name__ == "__main__":
    unittest.main()
