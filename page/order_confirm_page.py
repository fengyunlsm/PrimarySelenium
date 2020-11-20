#coding=utf-8
import sys, time, os
base_path = os.getcwd()
sys.path.append(base_path)

class OrderPage(object):
    def __init__(self, driver):
        self.fd = driver


    def order(self):
        # 点击结算
        pass
    

    def get_price_after_promtion(self):
        return self.fd.get_element("order", "price_after_promtion", "订单确认页_查找促销后的价格").get_attribute('textContent')


    def get_total_price(self):
        return self.fd.get_element("order", "total_price", "订单确认页_查找总价").get_attribute('textContent')

    
    def assert_value(self):
        return True