# coding=utf-8
# 使用各种find_element_by_XXX方法 和find_elements_by_XXX方法
# 前者一般返回匹配的第一个元素，后者返回元素列表
# 未找到元素则抛出NoSuchElementException异常
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://demo.magentocommerce.com/")

    # 检查标签的属性值
    def test_search_text_field_max_length(self):
        search_field = self.driver.find_element_by_id("search")  # 通过id查找
        self.assertEqual("128", search_field.get_attribute("maxlength"))    # 获得标签的maxlength属性值

    # 检查button是否可点击
    def test_search_button_enable(self):
        button = self.driver.find_element_by_class_name("button")  # 通过class name查找
        self.assertTrue(button.is_enabled())

    # 检查链接是否可见
    def test_my_account_link_is_displayed(self):
        account_link = self.driver.find_element_by_link_text("ACCOUNT")  # 通过标签之间的内容查找
        self.assertTrue(account_link.is_displayed())

    # 获得包含对应内容的所有标签
    def test_accounts_links(self):
        account_links = self.driver.find_elements_by_partial_link_text("ACCOUNT")
        self.assertEqual(2, len(account_links))  # 判断获得链接数

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)