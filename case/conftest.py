#coding=utf-8
import pytest, time, os, sys
base_path = os.getcwd()
sys.path.append(base_path)
from base.basepage import SeleniumDriver

@pytest.fixture()
def init_driver():
    driver = SeleniumDriver("chrome")
    driver.get_url('http://eshop.tslj.cn/#/login')
    driver.handle_window('max')
    yield driver
    driver.close_driver()