import sys, os
base_path = os.getcwd()
sys.path.append(base_path)
import os, time, pytest

class TestShoppingCartCase():

    @pytest.mark.usefixtures("init_cart")
    def test_cart_empty(self, init_cart):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_cart
        login.login("13544989573", "111111")       
        home.enter_cart()
        if (cart.is_cart_empty() != False):
            cart.empty_cart()
            cart.assert_cart_empty()
        else:
            cart.assert_cart_empty()

    @pytest.mark.usefixtures("init_cart")
    def test_empty_cart(self, init_cart):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_cart
        login.login("13544989573", "111111")
        search.search_product("铂金钻石戒指")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        home.enter_cart()
        cart.empty_cart()
        cart.assert_cart_empty()


    
    @pytest.mark.usefixtures("init_cart")
    def test_del_an_goods(self, init_cart):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_cart
        login.login("13544989573", "111111")
        search.search_product("铂金钻石戒指")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        home.enter_cart()
        cart.check_commerce_good("铂金钻石戒指")
        cart.remove_an_goods("铂金钻石戒指")
        cart.confirm_remove()
        cart.assert_goods_removed("铂金钻石戒指")

    @pytest.mark.usefixtures("init_cart")
    def test_remove_multi_goods(self, init_cart):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_cart
        login.login("13544989573", "111111")
        search.search_product("KUHASHI 细萃系列 18K红色黄金项链")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        search.search_product("【门店精选】18K红色黄金钻石项链")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        home.enter_cart()
        cart.check_commerce_good("KUHASHI 细萃系列 18K红色黄金项链")
        cart.check_commerce_good("【门店精选】18K红色黄金钻石项链")
        cart.remove_multi_goods()
        cart.confirm_remove()
        cart.assert_goods_removed("KUHASHI 细萃系列 18K红色黄金项链")
        cart.assert_goods_removed("【门店精选】18K红色黄金钻石项链")

    @pytest.mark.usefixtures("init_cart")
    def test_remove_without_check(self, init_cart):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_cart
        login.login("13544989573", "111111")
        search.search_product("KUHASHI 细萃系列 18K红色黄金项链")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        home.enter_cart()
        cart.remove_multi_goods()
        cart.assert_remove_fail("KUHASHI 细萃系列 18K红色黄金项链")
        cart.empty_cart()

    @pytest.mark.usefixtures("init_cart")
    def test_check_presell(self, init_cart):
        # 还没调通
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_cart
        login.login("13544989573", "111111")
        search.search_product("KUHASHI 细萃系列 18K红色黄金项链")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        search.search_product("TSL | Atelier 18K白金钻石戒指")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        search.search_product("【门店精选】18K三色黄金戒指 13")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        home.enter_cart()
        cart.check_commerce_good("TSL | Atelier 18K白金钻石戒指")
        cart.check_goods_after_persell("【门店精选】18K三色黄金戒指")
        cart.assert_check_fail()
        cart.empty_cart()

    @pytest.mark.cart
    @pytest.mark.usefixtures("init_cart")
    def test_reduce_goods(self, init_cart):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_cart
        login.login("13544989573", "111111")
        search.search_product("KUHASHI 细萃系列 18K红色黄金项链")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        home.enter_cart()
        cart.click_reduce_button("KUHASHI 细萃系列 18K红色黄金项链")
        cart.assert_reduce_fail("KUHASHI 细萃系列 18K红色黄金项链")
        cart.empty_cart()


    
    @pytest.mark.usefixtures("init_cart")
    def test_incre_goods(self, init_cart):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_cart
        login.login("13544989573", "111111")
        # 验证价格是否新增，商品数量是否比原来多
        search.search_product("SNOOPY 史努比系列 18K黄金钻石戒指 13")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        home.enter_cart()

        