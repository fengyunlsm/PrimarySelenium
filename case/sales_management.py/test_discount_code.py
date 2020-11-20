#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os, time, pytest
base_path = os.getcwd()
sys.path.append(base_path)
from page.productdetail_page import ProductDetailPage

class TestDiscountCase():

    # 创建直减优惠的折扣码活动
    @pytest.mark.usefixtures("init_discount")
    def test_create_discount(self, init_discount):
        pass