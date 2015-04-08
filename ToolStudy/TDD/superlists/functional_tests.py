# coding=utf-8
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
# 从用户的角度测试


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute("placeholder"),
            'Enter a to-do item'
        )
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 判断是否存在一行的内容与给定内容一致
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in table\n %s" % (table.text, )
        # )
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.fail("Finish the test!")

if __name__ == '__main__':
    unittest.main(verbosity=2)