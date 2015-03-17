# coding=utf-8
# 实现在同一个浏览器中进行测试
# 类级上的setUp、tearDown方法
# 与普通的区别在于，类级的单元测试，setUp和tearDown只需执行一次，即所有的测试用例可以共享相同变量

import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):
    # 创建需要测试的对象
    # 在所有测试方法执行前执行，进行一些初始化操作
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://demo.magentocommerce.com/")

    def test_search_by_category(self):
        print id(self.driver)   # 打印当前测试用例的id
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("dress")
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        # 测试products是否为6个
        self.assertEqual(6, len(products))

    def test_search_by_name(self):
        print id(self.driver)    # 打印当前测试用例的id
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("dress")
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        # 测试products是否为6个
        self.assertEqual(6, len(products))
    
    # 在所有测试用例测试完成后执行，进行一些资源释放操作
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()