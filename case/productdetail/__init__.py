import sys
sys.path.append('d:\\pyProject\\PrimarySelenium')
import os, time, pytest


class TestProductDetailCase():
        
    @pytest.mark.add_to_cart
    @pytest.mark.usefixtures("init_driver")
    def test_add_shoppring_case(self, init_shoppingcart):
        init_shoppingcart.add_to_cart()
