#coding=utf-8
import sys, os
base_path = os.getcwd()
sys.path.append(base_path)

class ProductDetailPage(object):
    def __init__(self, driver):
        self.fd = driver
    
    def add_cart(self):
        self.fd.click_element("productdetail", "add_cart_button", "商品详情页_添加到购物车")
        

    def click_cart_button(self):
        self.fd.click_element("productdetail", "cart_button", "商品详情页_点击购物车按钮")


    def get_product_name(self):
        return self.fd.get_element("productdetail", "shop_name", "商品详情页_查找商品名字").get_attribute("innerHTML")

    def click_purchase_button(self):
        self.fd.click_element("productdetail", "buy_button", "商品详情页_点击立即购买按钮")

    def click_login_buttion(self):
        self.fd.click_element("productdetail", "login_button", "商品详情页_点击去登陆按钮")

    