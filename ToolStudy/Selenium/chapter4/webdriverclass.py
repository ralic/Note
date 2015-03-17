# coding=utf-8
from selenium import webdriver
# WebDriver --- WebElement  前者是浏览器，后者是元素

# WebDriver属性：current_url, name, page_source
# 获得当前浏览页面的url，浏览器的名字name，页面的html源码（page_source）等
def attribute():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")
    print driver.current_url
    print driver.page_source
    print driver.name
    print driver.title


# WebDriver方法：back(),forward(), close(),quit(),get(url),maximize_window()，refresh()刷新
# 后，前，关闭当前窗口，关闭并销毁当前的webdriver，获得url，最大化，
def method():
    driver = webdriver.Chrome()
    driver.get("http://www.python.org")   # 当前浏览器在python.org页面
    driver.get("http://www.baidu.com")    # 当前浏览器从python.org到baidu.com页面
    driver.back()   # 当前浏览器跳回上一页，即python.org
    driver.forward()  # 当前浏览器跳至下一页，即回到baidu


if __name__ == '__main__':
    attribute()
