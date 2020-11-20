import sys
sys.path.append('d:\\pyProject\\PrimarySelenium')
import os, time, pytest
from page.discount_code_page import DiscountPage


class HomeBussiness():
    def __init__(self, driver):
        self.discount = DiscountPage(driver)

    # 创建直减优惠的折扣码活动 
    