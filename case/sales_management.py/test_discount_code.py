import sys
sys.path.append('d:\\pyProject\\PrimarySelenium')
import os, time, pytest
from page.productdetail_page import ProductDetailPage

class TestDiscountCase():

    # 创建直减优惠的折扣码活动
    @pytest.mark.usefixtures("init_discount")
    def test_create_discount(self, init_discount):
        pass