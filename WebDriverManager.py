import argparse
import sys

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class WebDriverManager(object):
    def __init__(self, driver_arg):
        get_driver(driver_arg)


def get_driver(driver_arg):
    driver = None

    if driver_arg == 'chrome':
        driver_path = ChromeDriverManager().install()
        driver = webdriver.Chrome(driver_path)
    elif driver_arg == 'firefox':
        driver_path = GeckoDriverManager().install()
        driver = webdriver.Firefox(driver_path)
    elif driver_arg == 'edge':
        driver_path = EdgeChromiumDriverManager().install()
        driver = webdriver.Edge(driver_path)
    return driver
