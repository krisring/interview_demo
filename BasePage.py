import unittest
from abc import abstractmethod
from selenium import webdriver


class BasePage(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def _validate_page(self, driver):
        return

    def click_element(self, locator, locator_value):
        self.button = self.driver.find_element(locator, locator_value)
        self.button.click()

    def check_element_presence(self, locator, locator_value):
        self.element_to_check = self.driver.find_element(locator, locator_value)

        return self.element_to_check.id is not None

    def fill_the_form(self, locator, locator_value, value_text):
        self.form = self.driver.find_element(locator, locator_value)
        self.form.clear()
        self.form.send_keys(value_text)
