#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import os, time, pytest
base_path = os.getcwd()
sys.path.append(base_path)
from page.productdetail_page import ProductDetailPage


class TestSearchCase():

    @pytest.mark.usefixtures("init_search")
    def test_search_case(self, init_search):
        search = init_search[1]
        search.search("SNOOPY 史努比系列 18K黄金钻石戒指 13")
        # 判断查找出来的是正确的
        assert search.get_product_list_first_pic() == "SNOOPY"+" "+"史努比系列"+" "+"18K黄金钻石戒指"


    @pytest.mark.search
    @pytest.mark.usefixtures("init_search")
    def test_to_product_detail(self, init_search):
        # 测试跳转页面正常
        init_driver = init_search[0]
        search = init_search[1]
        productdetail = init_search[2]
        search.search("SNOOPY 史努比系列 18K黄金钻石戒指 13")
        product_name = search.get_product_list_first_pic()
        search.to_product_detail()
        init_driver.set_node("productdetaill")
        time.sleep(1)
        assert  product_name in  productdetail.get_product_name()