# coding=utf-8
# 使用chorm抓取数据

import time
from contextlib import contextmanager
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get("https://www.qhee.com/node/company/standard")
atag = driver.find_element_by_id("list_all_ents")
atag.click()

em = driver.find_element_by_xpath("//em[@style='font-style:inherit;']")
print em.text


@contextmanager
def close(driver):
    try:
        yield driver
    finally:
        pass


def driver_action(driver, url):
    driver.get(url)
    atag = driver.find_element_by_id("list_all_ents")
    atag.submit()


def main():
    with close(webdriver.Chrome()) as driver:
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver_action(driver, "https://www.qhee.com/node/company/standard")

if __name__ == '__main__':
    pass



