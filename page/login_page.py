#coding=utf-8
import sys, os
base_path = os.getcwd()
sys.path.append(base_path)
from util.read_ini import ReadIni
import time

class LoginPage(object):
    def __init__(self, driver):
        self.fd = driver

    def login(self, phone, password):
        phone_element = self.fd.find_level_element('login', 'login_phone_parent', 'login_phone_children', "登录页面_查找手机号输入框", 1, 0)
        self.fd.send_value('login', phone_element, phone, "登录页面_输入手机号")
        password_element = self.fd.find_level_element('login', 'login_password_parent', 'login_password_children', '登录页面_查找密码输入框', 2, 0)
        self.fd.send_value('login', password_element, password, "登录页面_输入密码")
        self.fd.click_element('login', "login_button", "登录页面_点击登录按钮")


    def get_login_success_tips(self):
        # document.getElementsByTagName("span")[11]
        self.fd.wait_eleVisible('login', "login_message_success", "登录成功_等待成功提示出现")
        return self.fd.find_list_element('login', "login_success_tip", 11, "校验登录_登录成功").get_attribute('textContent')

    def get_login_fail_tips(self):
        # 判断提示 用户名或密码错误
        self.fd.wait_eleVisible('login', "login_error_tip_parent", "登录失败_等待错误提示出现")
        return self.fd.find_level_element('login', "login_error_tip_parent", "login_error_tip_child", "校验登录_用户名或密码错误", 0, 0).get_attribute('textContent')

    def click_forget_pwd_link(self):
        self.fd.get_element('login', "forget_password", "登录页面_点击忘记密码")

    def check_to_forget_pwd(self):
        return self.fd.get_element('login', "forget_password_check", "忘记密码页_校验跳转正常")

    