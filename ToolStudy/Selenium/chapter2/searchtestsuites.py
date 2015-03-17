# coding=utf-8
import unittest
from __builtin__ import classmethod

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from selenium import webdriver


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://demo.magentocommerce.com/")

    def test_search_field(self):
        # 测试搜索框是否在主页
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    def test_shopping_cart_empty_message(self):
        shopping_cart_status = self.driver.find_element_by_css_selector("div.header-minicart span.icon")
        shopping_cart_status.click()
        shopping_cart_icon = self.driver.find_element_by_css_selector("p.empty").text
        self.assertEqual("You have no items in your shopping cart.", shopping_cart_icon)
        close_button = self.driver.find_element_by_css_selector("div.minicart-wrapper a.close")
        close_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        else:
            return True


def testsuites():
    from Selenium.chapter2.searchtest import SearchTest

    # 创建测试集， 取得特定的测试用例
    search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
    homepage_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

    # 确定测试集（列表）
    smoke_tests = unittest.TestSuite([homepage_test, search_tests])
    # 运行测试集
    unittest.TextTestRunner(verbosity=2).run(smoke_tests)

if __name__ == '__main__':
    testsuites()