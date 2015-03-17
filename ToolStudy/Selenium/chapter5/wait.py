# coding=utf-8
# implicit wait 隐式等待，多用于处理程序响应时间不一致的情况（比如Ajax请求，一些元素的内容是动态呈现的），
# 它是WebDiriver中常用同步手段，用于让全部的测试或一组步骤同步进行。即等待所有资源就绪后再开始下一步动作。
# 对于处理网页中不会立刻出现并可用的元素
# implicityly_wait(timeout), 设置一次即可

# explict wait 显式等待，在需要的情况下进行设置。
# WebDriverWait用于实现显式等待

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest


class ExplicitWaitTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://demo.magentocommerce.com/")

    def test_account_link(self):
        WebDriverWait(self.driver, 10).until(lambda s:
                                             s.find_element_by_id("select-language").get_attribute("length") == "3")
        # 期望表达式，其功能与find_element系列差不多，可以对比一下
        account = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.LINK_TEXT, "ACCOUNT")))
        account.click()

    def tearDown(self):
        self.driver.quit()

