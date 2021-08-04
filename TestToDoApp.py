import unittest
from LambdaPage import LambdaPage
from BaseTest import BaseTest


class TestToDoApp(BaseTest):

    def test_lambda_test_todo_app(self):
        item_value = 'add value'
        lambda_page = LambdaPage(self.driver)
        lambda_page.enter_item(item_value)
        lambda_page.click_add()
        self.assertTrue(lambda_page.list_contains_item(item_value), "The list did not contain the item after "
                                                                     "clicking add.")


if __name__ == '__main__':
    unittest.main()
