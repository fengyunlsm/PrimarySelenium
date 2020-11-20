import sys, os, time, pytest
base_path = os.getcwd()
sys.path.append(base_path)
from page.productdetail_page import ProductDetailPage


class TestShoppingCartCase():

   
    @pytest.mark.usefixtures("init_order")
    def test_pruchase_immediately(self, init_order):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_order
        login.login("13544989573", "111111")        
        search.search_product("铂金钻石戒指")
        search.navigate_productDetail_page()
        productDetail.click_purchase_button()
        orderConfirm.assert_value()


    @pytest.mark.usefixtures("init_order")
    def test_pruchase_whitout_login(self, init_order):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_order
        search.search_product("铂金钻石戒指")
        search.navigate_productDetail_page()
        productDetail.click_purchase_button()
        productDetail.click_login_buttion()
        login.login("13544989573", "111111")
        orderConfirm.assert_value()

    @pytest.mark.usefixtures("init_order")
    def test_pruchase_with_cart(self, init_order):
        init_driver, login, home, cart, productDetail, orderConfirm, search = init_order
        login.login("13544989573", "111111")
        search.search_product("铂金钻石戒指")
        search.navigate_productDetail_page()
        productDetail.add_cart()
        home.enter_cart()
        cart.check_commerce_good("铂金钻石戒指")
        cart.click_settlement()
        orderConfirm.assert_value()

    @pytest.mark.order
    @pytest.mark.usefixtures("init_order")
    def test_pruchase_with_cart(self, init_order):
        pass

