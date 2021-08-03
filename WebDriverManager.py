import argparse
import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.utils import ChromeType


class WebDriverManager(object):
    def __init__(self, driver):
        browser_switch = {
            "Chrome",
            "Firefox",
            "Edge"
        }
        if driver not in browser_switch:
            print(f"Invalid argument.")
        elif browser_switch.get(driver) == "Chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        # elif browser_switch.get(driver) == "Firefox":
        #     return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # elif browser_switch.get(driver) == "Edge":
        #     return webdriver.Edge(EdgeChromiumDriverManager().install())
