import sys
sys.path.append('d:\\pyProject\\PrimarySelenium')
import os, time, pytest


class TestProductDetailCase():
    
    @pytest.mark.buy
    @pytest.mark.usefixtures("init_productdetail")
    def test_order(self, init_productdetail):
        init_productdetail.click_buy_button()
        time.sleep(3)
