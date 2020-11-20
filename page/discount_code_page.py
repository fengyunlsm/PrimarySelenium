#coding=utf-8
import sys
import time

class DiscountPage(object):
    def __init__(self, driver):
        self.fd = driver


    def set_discount_name(self, key):
        self.fd.send_value("discount_name", key, "折扣码创建页_输入折扣码名")

    def click_select_good_button(self)
        self.fd.click_element("select_good_button", "折扣码创建页_选择商品")

    def set_product_code(self, key):
        self.fd.send_value("product_code", key, "折扣码创建页_输入商品编码")

    # 上架开始时间
    def set_lanuach_time_start(self, key):
        self.fd.send_value("lanuach_time_start", key, "折扣码创建页_输入商品上架开始时间")

    # 上架结束时间
    def set_lanuach_time_end(self, key):
        self.fd.send_value("lanuach_time_end", key, "折扣码创建页_输入商品上架结束时间")

    # 获取查询按钮
    def get_query_button(self):
        self.fd.click_element("query_button", "创建折扣码_查找查询按钮")

    # 确认选择商品
    def confirm_select_product(self):
        self.fd.click_element("product_confirm", "折扣码创建页_确认选择商品")


    # 输入折扣码活动开始时间
    def set_discount_start(self):
        self.fd.send_value("discount_start", "折扣码创建页_输入折扣码活动开始时间")
    
    # 输入折扣码活动结束时间
    def set_discount_end(self):
        self.fd.send_value("discount_end", "折扣码创建页_输入折扣码活动结束时间")

    # 输入折扣码可使用次数
    def set_cycle_time(self):
        self.fd.send_value("cycle_time", "折扣码创建页_输入折扣码可使用次数")

    # 选择规则
    def set_regular(self, key):
        if key == '满减':
            self.fd.click_element("full_reduction", "折扣码创建页_选择满减优惠")
        elif key == "直降":
            self.fd.click_element("straight_down", "折扣码创建页_选择直降优惠")
        else:
            self.fd.click_element("full_fold_reduction", "折扣码创建页_选择满折减优惠")

    # 选择是否叠加使用
    def set_overlay(self)；
        self.fd.click_element("overlay_checkbox", "折扣码创建页_选择是否叠加使用")
    

    # 折扣码活动描述
    def set_activity_description(self):
        self.fd.send_value("activity_description", "折扣码创建页_输入活动描述")

    # 保存
    def click_save(self):
        self.fd.click_element("save_button", "折扣码创建页_点击保存")

    