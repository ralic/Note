import cookielib
import urllib2
from selenium import webdriver
driver = webdriver.PhantomJS()
# driver.get("http://zhushou.360.cn/detail/index/soft_id/77208?recrefer=SE_D_360")
# data = driver.title
# click_item = driver.find_element_by_xpath("//span[@class='s-3'][1]")
# print click_item.text
driver.get("http://shouji.baidu.com/soft/item?docid=7501796&from=landing&f=search_app_%E5%BE%AE%E4%BF%A1%40listsp_1_title%401%40")
# print driver.page_source
# pages = driver.find_element_by_xpath("//span[@class='review-count-all']")
# pages = driver.find_element_by_id('comment-num')
pages1 = driver.find_elements_by_xpath("//div[@class='pager']//li")

print pages1
