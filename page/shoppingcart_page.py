#coding=utf-8
import sys, os, pytest
base_path = os.getcwd()
sys.path.append(base_path)
from util.read_ini import read_ini


class ShoppingCartPage(object):
    def __init__(self, driver):
        self.fd = driver

    # 清空购物车按钮
    def empty_cart(self):
        self.fd.click_element("shoppingcart", "empty_cart_button", "购物车页面_清空购物车")
        self.fd.click_element("shoppingcart", "confirm_empty_cart", "购物车页面_点击确认清空购物车按钮")

    # 断言购物车是否为空
    def assert_cart_empty(self):
        assert self.fd.get_element("shoppingcart", "cart_empty_status", "购物车_查看购物车是否为空") is not None

    # 判断购物车是否为空
    def is_cart_empty(self):
        if self.fd.get_element("shoppingcart", "cart_empty_status", "购物车_查看购物车是否为空") is not None:
            return False
        else:
            return True

    # 点击批量删除
    def remove_multi_goods(self):
        self.fd.click_element("shoppingcart", "remove_multi_button", "购物车页面_点击批量删除")

    # 点击删除
    def remove_an_goods(self, product_name):
        read_ini.set_value("shoppingcart", "remove_button", product_name)
        self.fd.click_element("shoppingcart", "remove_button", "购物车页面_删除电商商品")
        read_ini.replace_value("shoppingcart", "remove_button", product_name)

    # 确认删除
    def confirm_remove(self):
        self.fd.wait_eleVisible("shoppingcart", "confirm_button", "购物车页面_等待删除确认按钮")
        self.fd.click_element("shoppingcart", "confirm_button", "购物车页面_点击删除确认按钮")

    # 断言商品是否被删除
    def assert_goods_removed(self, product_name):
        read_ini.set_value("shoppingcart", "remove_button", product_name)
        result = self.fd.has_element("shoppingcart", "has_goods", "购物车页面_查找已删除的商品") is None
        read_ini.replace_value("shoppingcart", "remove_button", product_name)
        assert result

    # 断言删除不成功的提示
    def assert_remove_fail(self, product_name):
        read_ini.set_value("shoppingcart", "remove_button", product_name)
        assert self.fd.has_element("shoppingcart", "has_goods", "购物车页面_查找已删除的商品") is None
        read_ini.replace_value("shoppingcart", "remove_button", product_name)
        assert self.fd.has_element("shoppingcart", "remove_fail_tip", "购物车页面_查找删除失败的提示") is not None


    # 查找已删除的商品
    def get_deleted_good(self):
        self.fd.get_element("shoppingcart", "good", "购物车页面_查找已删除的商品")

    
    # 点击结算
    def click_settlement(self):
        self.fd.click_element("shoppingcart", "settlement", "购物车页面_点击结算")
    
    # 点击+
    def click_increase_button(self):
        read_ini.set_value("shoppingcart", "increase_button", product_name)
        self.fd.click_element("shoppingcart", "increase_button", "购物车页_点击+")
        read_ini.replace_value("shoppingcart", "remove_button", product_name)

    # 断言商品数量增加
    def assert_incre_success(self, product_name):
        read_ini.set_value("shoppingcart", "goods_amount", product_name)
        assert self.fd.get_element("shoppingcart", "goods_amount", "购物车页_查找商品数量").get_attribute("value") == '2'
        # 断言商品数量
        # 拿到商品价格，然后再乘以2
        # 先拿到商品价格
        goods_price = self.fd.get_element("shoppingcart", "good_price", "购物车页_查找商品单价").get_attribute("textContent")
        goods_amount = self.fd.get_element("shoppingcart", "goods_amount", "购物车页_查找商品数量").get_attribute("value")
        assert self.fd.has_element("shoppingcart", "increase_button", "购物车页_查找+按钮") is not None
        read_ini.set_value("shoppingcart", "goods_amount", product_name)
    
    # 点击-
    def click_reduce_button(self, product_name):
        read_ini.set_value("shoppingcart", "decrease_button", product_name)
        self.fd.click_element("shoppingcart", "decrease_button", "购物车页_点击-")
        read_ini.replace_value("shoppingcart", "remove_button", product_name)
    
    # 断言商品数量减少至1时，无法再减少
    def assert_reduce_fail(self, product_name):
        read_ini.set_value("shoppingcart", "goods_amount", product_name)
        read_ini.set_value("shoppingcart", "none_reduce_button", product_name)
        assert self.fd.get_element("shoppingcart", "goods_amount", "购物车页_查找商品数量").get_attribute("value") == '1'
        assert self.fd.has_element("shoppingcart", "none_reduce_button", "购物车页_查找-按钮") is not None
        read_ini.replace_value("shoppingcart", "goods_amount", product_name)
        read_ini.replace_value("shoppingcart", "none_reduce_button", product_name)


    # 勾选电商商品
    def check_commerce_good(self, product_name):
        read_ini.set_value("shoppingcart", "e-commerce-checkbox", product_name)
        self.fd.click_element("shoppingcart", "e-commerce-checkbox", "购物车页面_勾选电商商品")
        read_ini.replace_value("shoppingcart", "e-commerce-checkbox", product_name)
    
    def check_goods_after_persell(self, product_name):
        read_ini.set_value("shoppingcart", "e-commerce-checkbox", product_name)
        self.fd.click_element("shoppingcart", "e-commerce-checkbox", "购物车页面_勾选电商商品")
        read_ini.replace_value("shoppingcart", "e-commerce-checkbox", product_name)

    # 断言勾选失败
    def assert_check_fail(self):
        assert self.fd.has_element("shoppingcart", "check_fail_tip", "购物车页_查找勾选失败提示") is not None
        self.fd.click_element("shoppingcart", "confirm_check_fail", "购物车页_确认勾选失败")
        
    # 查看小计
    def get_subtotal(self):
        return self.fd.get_element("subtotal", "购物车页_小计计算正确").get_attribute("textContent")

    # 查看总计
    def get_total(self):
        return self.fd.get_element("total", "购物车页_查看总计计算正确").get_attribute("textContent")