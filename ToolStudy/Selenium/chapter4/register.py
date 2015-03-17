# coding=utf-8
# 注册账号

from selenium import webdriver
import unittest
from time import gmtime, strftime


class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo.magentocommerce.com/")
        driver = self.driver
        driver.find_element_by_link_text("Log In").click()  # 找到登陆按钮并点击
        create_account_button = driver.find_element_by_xpath("//a[@title='Create an Account']")  # 找到注册按钮
        self.assertTrue(create_account_button.is_enabled() and create_account_button.is_displayed())    # 测试注册按钮可用且可见
        create_account_button.click()   # 点击注册按钮进入注册页面
        self.assertEquals("Create New Customer Account", driver.title)  # 测试注册页面的标题是否与给定标题一致

        # 获得要填写的注册信息相关tag
        first_name = driver.find_element_by_id("firstname")
        last_name = driver.find_element_by_id("lastname")
        email_addresss = driver.find_element_by_id("email_address")
        new_letter_subscription = driver.find_element_by_id("is_subscribed")
        password = driver.find_element_by_id("password")
        confirm_password = driver.find_element_by_id("confirmation")
        submit_button = driver.find_element_by_xpath("//button[@title='Register']")
        self.assertEqual("255", first_name.get_attribute("maxlength"))  # 测试文本框可输入最大长度
        self.assertEqual("255", last_name.get_attribute("maxlength"))
        # 测试所有的tag可用
        self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and email_addresss.is_enabled() and
                        password.is_enabled() and confirm_password.is_enabled() and submit_button.is_enabled())
        self.assertFalse(new_letter_subscription.is_selected())  # 测试是否未被选中（即是否为False）
        # 组织测试数据
        user_name = "user_" + strftime("%Y%m%d%H%M%S", gmtime())
        first_name.send_keys("Test")
        last_name.send_keys(user_name)
        new_letter_subscription.click()
        email_addresss.send_keys(user_name + "@example.com")
        password.send_keys("tester")
        confirm_password.send_keys("tester")
        submit_button.click()

        driver.find_element_by_link_text("ACCOUNT").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)



