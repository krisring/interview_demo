from BasePage import BasePage
from selenium.webdriver.common.by import By


class LambdaPage(BasePage):

    # email = 'test@test.net'
    # password = 'test'

    # passwordform = (By.ID, 'password')
    # button = (By.XPATH, "//*[contains(text(), 'Log In')]")

    # def __init__(self, driver):
    #     super(LambdaPage, self).__init__(driver)
    add_field_value = "//input[@id='sampletodotext']"
    button = "//input[@id='addbutton']"
    item_table = "//ul[@class='list-unstyled']/li"

    def _validate_page(self, driver):
        assert 'Login' in driver.title()

    def enter_item(self, value_text):
        BasePage.fill_the_form(self, By.XPATH, self.add_field_value, value_text)

    def click_add(self):
        BasePage.click_element(self, By.XPATH, self.button)

    def list_contains_item(self, item_value):
        self.list_items = self.driver.find_elements(By.XPATH, self.item_table)
        for item in self.list_items:
            if item.text == item_value:
                return True
        return False

    def list_contains_defaults(self):
        self.list_items = self.driver.find_elements(By.XPATH, self.item_table)
        defaults = ["First Item",
                    "Second Item",
                    "Third Item",
                    "Fourth Item",
                    "Fifth Item"]
        check_list = []
        for item in self.list_items:
            check_list.append(item.text)
        if check_list == defaults:
            return True
        return False

    def get_list_count(self):
        self.list_items = self.driver.find_elements(By.XPATH, self.item_table)
        return len(self.list_items)

    def add_button_present(self):
        BasePage.check_element_presence(self, By.XPATH, self.button)


