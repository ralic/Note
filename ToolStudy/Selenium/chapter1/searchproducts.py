# coding=utf-8
# 对一个购物网站进行测试: http://demo.magentocommerce.com/
import time
from selenium import webdriver
# 创建一个Firefox 的 session, （其他浏览器 including Firefox, Chrome, Internet Explorer, Safari）
driver = webdriver.Ie()
driver.implicitly_wait(30)
driver.maximize_window()   # 浏览器窗口最大化

# 导航到要浏览的页面
driver.get("http://demo.magentocommerce.com/")

# 通过使用标签元素的name属性值，获取搜索框（当前页面搜索框的name="q"）
search_field = driver.find_element_by_name("q")   # 得到第一个name属性值为q的标签
search_field.clear()    # 清除搜索框中旧的内容

# 键入搜索关键字
search_field.send_keys("dress")
search_field.submit()   # 提交搜索

# 通过xpath获得当前页面所有产品a标签
products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")
print "Found %d products:" % len(products)  # 打印获得的链接数量

# 遍历所有的a标签，打印商品名称
for product in products:
    print product.text
time.sleep(5)
# 关闭浏览器
driver.quit()

print "The next one....."

# 使用上下文管理器实现同样的功能
import contextlib


@contextlib.contextmanager
def closing(drivers):
    try:
        yield drivers
    finally:
        drivers.quit()

# 自动关闭浏览器
with closing(webdriver.Firefox()) as w:
    w.maximize_window()