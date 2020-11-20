import sys
sys.path.append('d:\\pyProject\\PrimarySelenium')
import os, time, pytest
from page.home_page import HomePage


class HomeBussiness():
    def __init__(self, driver):
        self.home = HomePage(driver)

    # 进入到购物车页面
    def enter_cart(self):
        self.home.enter_cart()