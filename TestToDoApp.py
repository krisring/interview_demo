import unittest
from LambdaPage import LambdaPage
from BaseTest import BaseTest


class TestToDoApp(BaseTest):

    def test_list_default_amount(self):
        lambda_page = LambdaPage(self.driver)
        self.assertTrue(lambda_page.get_list_count() == 5, "The list did not contain the correct default amount of items")

    def test_default_item_list(self):
        lambda_page = LambdaPage(self.driver)
        self.assertTrue(lambda_page.list_contains_defaults(), "The list did not contain the expected defaults")

    def test_add_button_present(self):
        lambda_page = LambdaPage(self.driver)
        self.assertTrue(lambda_page.add_button_present(), "The add button was not present")

    def test_lambda_test_todo_app(self):
        item_value = 'add value'
        lambda_page = LambdaPage(self.driver)
        lambda_page.enter_item(item_value)
        lambda_page.click_add()
        self.assertTrue(lambda_page.list_contains_item(item_value), "The list did not contain the item after "
                                                                     "clicking add.")


if __name__ == '__main__':
    unittest.main()
