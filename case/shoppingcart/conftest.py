#coding=utf-8
import pytest, time
from page.shoppingcart_page import ShoppingCartPage
from page.productdetail_page import ProductDetailPage
from page.order_confirm_page import OrderPage
from page.login_page import LoginPage
from page.home_page import HomePage
from page.search_page import SearchPage
from page.order_confirm_page import OrderPage
from base.basepage import SeleniumDriver



@pytest.fixture()
@pytest.mark.usefixtures("init_driver")
def init_cart(init_driver):
    login = LoginPage(init_driver)
    home = HomePage(init_driver)
    cart = SearchPage(init_driver)
    productDetail = ProductDetailPage(init_driver)
    orderConfirm = OrderPage(init_driver)
    cart = ShoppingCartPage(init_driver)
    search = SearchPage(init_driver)
    yield init_driver, login, home, cart, productDetail, orderConfirm, search
    time.sleep(1)