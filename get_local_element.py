#code=utf-8
import sys
sys.path.append('d:\\pyProject\\')
from open_browser import SeleniumDriver
from PrimarySelenium.read_ini  import ReadIni
import time

def input_upload():
    selfnium_driver = SeleniumDriver('chrome')
    selfnium_driver.open_url_is_true('https://www.imooc.com/user/newlogin', '慕课网')
    selfnium_driver.find_element('username')
    selfnium_driver.send_value('username', '2399548030@qq.com')
    selfnium_driver.find_element('password')
    selfnium_driver.send_value('password', '6329017abc')
    selfnium_driver.click_element('login_button')
    time.sleep(1)
    selfnium_driver.open_url_is_true('https://www.imooc.com/user/setprofile', '慕课网')
    selfnium_driver.click_element('avatar')
    time.sleep(2)
    selfnium_driver.send_value('upload_avatar','C:\\Users\\Administrator\\Desktop\\meizi.jpg') # 这个地方卡住了
    time.sleep(2)
    selfnium_driver.close_driver()

def not_input_upload():
    pass


def download():
    selfnium_driver = SeleniumDriver('chrome')
    selfnium_driver.open_url_is_true('https://www.imooc.com/mobile/app', '慕课网')
    selfnium_driver.find_list_element('download', 1).click()
    time.sleep(10)
    selfnium_driver.close_driver()

download()

