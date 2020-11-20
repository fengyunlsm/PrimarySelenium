#coding=utf-8
import sys, os, time
base_path = os.getcwd()
sys.path.append(base_path)

class HomePage(object):
    def __init__(self, driver):
        self.fd = driver

    def enter_cart(self):
        time.sleep(1)
        self.fd.wait_eleVisible("home", "cart_button", "首页_等待购物车图标出现")
        self.fd.click_element("home", "cart_button", "首页_进入到购物车")

    def search(self, content):
        self.fd.send_value("home", "search_input", content, "首页_输入要搜索的内容")
        self.fd.click_element("home", "search_confirm", "首页_确认要搜索的内容")