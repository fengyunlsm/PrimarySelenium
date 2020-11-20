import sys
sys.path.append('d:\\pyProject\\PrimarySelenium')
import os, time, pytest
from page.shoppingcart_page import ShoppingCartPage


class ShoppingCartBussiness():

    def __init__(self, driver):
        self.cart = ShoppingCartPage(driver)

    # 勾选单个电商商品进行删除
    def del_without_check(self):
        self.cart.click_del_home_delivery_good_button()
        self.cart.click_del_confirm_button()
    
    # 确认已经没有这个电商商品3 19 19g
    def check_del_without_check_success(self):
        
        if self.cart.get_deleted_good() == None:
            return True
        else:
            return False

    # 勾选单个电商商品进行删除
    def del_one(self):
        pass

    # 勾选多个电商商品进行删除
    def del_multi(self):
        pass


    # 不勾选直接删除
    def del_all(self):
        pass


    # 勾选自提商品，不能勾选配送到家



    # 勾选电商商品是，不能勾选自提商品


    # 不勾选O2O电商商品 直接进行删除
    def del_O2O_without_check(self):
        self.cart.del_O2O_without_select()
        self.cart.click_del_confirm_button()

    # 删除O2O商品
    def delete_O2O_with_selected(self):
        self.cart.select_O2O()
        self.cart.click_batch_remove()
        self.cart.click_del_confirm_button()

    # 清空购物车
    def empty_cart(self):
        self.cart.empty_the_cart()
        self.cart.click_del_confirm_button()

    # 增加商品数量，总价和小计计算正确
    def increase_good(self):
        self.cart.select_commerce_good()
        self.cart.get_increase_button()
        

    # 减少商品数量，总价和小计计算正确
    def decrease_good(self):
        self.cart.select_commerce_good()
        self.cart.get_decrease_button()

    # 检查增加/减少商品后，小计计算正确
    def check_subtotal_correct(self):
        return self.cart.get_subtotal()

    # 检查增加/减少商品后，总价计算正确
    def check_total_correct(self):
        return self.cart.get_total()

    # 查看清空cart后的文本
    def check_empty_cart_text(self):
        if self.cart.get_empty_cart_text() == "您的购物袋没有任何物品。":
            return True
        else:
            return False


