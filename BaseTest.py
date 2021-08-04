import sys
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import WebDriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        driver_path = ChromeDriverManager().install()
        self.driver = webdriver.Chrome(driver_path)
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        # driver_arg = sys.argv[0]
        # if driver_arg.lower() in ["firefox", "chrome", "edge"]:
        #     self.driver = WebDriverManager.get_driver(driver_arg)
        #     self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        #     # return driver
        # else:
        #     print(f"Driver must be provided: firefox chrome edge")

    def tearDown(self):
        self.driver.quit()
