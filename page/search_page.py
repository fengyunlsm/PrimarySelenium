#coding=utf-8
import sys, time, os
base_path = os.getcwd()
sys.path.append(base_path)

class SearchPage(object):
    def __init__(self, driver):
        self.fd = driver
    
    def search_product(self, key):
        time.sleep(2)
        # self.fd.wait_eleVisible('search', "search_input", "搜索框_等待搜索框的出现")
        self.fd.send_value("search", "search_input", key, "搜索框_输入搜索内容")
        self.fd.keyboard("search", "search_input", "enter", "搜索框_敲回车")

    def navigate_productDetail_page(self):
        self.fd.click_element("search", "first_pic", "商品列表页_跳转到详情页")

    def get_product_list_first_pic(self):
        return self.fd.get_element("search", "first_pic", "搜索页_查找第一张图片").get_attribute('textContent')