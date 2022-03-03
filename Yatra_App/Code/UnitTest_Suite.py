import unittest

from selenium import webdriver

import UnitTest_Signin
import UnitTest_Nav_Bar
import UnitTest_NavBar_Settings
import UnitTest_Main_Heading
import UnitTest_Support
import UnitTest_More
import UnitTest_UsefulLinks
import UnitTest_Keep_In_Touch


class UnitTest_Suite(unittest.TestCase):

    def test_Yatra_App(self):
        # self of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest_Signin.UnitTest_Signin),
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest_Nav_Bar.UnitTest_Nav_Bar),
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest_NavBar_Settings.UnitTest_NavBar_Settings),
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest_Support.UnitTest_Support),
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest_More.UnitTest_More),
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest_Main_Heading.UnitTest_Main_Heading),
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest_UsefulLinks.UnitTest_UsefulLinks),
            unittest.defaultTestLoader.loadTestsFromTestCase(UnitTest_Keep_In_Touch.UnitTest_Keep_In_Touch)
        ])
        runner = unittest.TextTestRunner()
        runner.run(self.suite)


if __name__ == "__main__":
    unittest.main()

