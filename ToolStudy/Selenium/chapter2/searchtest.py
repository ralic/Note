# coding=utf-8
# 学习如何进行单元测试
# unittest 组件图：
#       TestCase --->Test Fixture
#         \
#       Test Suite --> Test Runner -->Test Report
import unittest
from selenium import webdriver


# 一个TestCase是unitteset中最小的单元，用于对一组特定的输入进行检查，并给出特定的反应
# 创建一个继承自TestCase的类
# assertEqual 用于检查预期的结果
# assertTrue 用于检验表达式
# assertRaises 用于检验预期抛出的异常
# setUp 和 tearDown 一对好机油
class SearchTest(unittest.TestCase):
    # 创建需要测试的对象
    # 在所有测试方法执行前执行，进行一些初始化操作
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo.magentocommerce.com/")

    def test_search_by_category(self):
        print id(self.driver)
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("dress")
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        # 测试products是否为6个
        self.assertEqual(2, len(products))

    def test_search_by_name(self):
        print id(self.driver)
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("dress")
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        # 测试products是否为6个
        self.assertEqual(6, len(products))

    # 在所有测试用例测试完成后执行，进行一些资源释放操作
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)