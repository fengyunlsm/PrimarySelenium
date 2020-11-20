import sys
import os, time, pytest
base_path = os.getcwd()
sys.path.append(base_path)
from page.login_page import LoginPage


class LoginBussiness():
    def __init__(self, driver):
        self.login = LoginPage(driver)

    # 登录测试用例
    def login_eshop(self, phone, password):
        self.login.login(phone, password)

    def check_login_success(self):
        if self.login.get_login_success_tips() == "登录成功！":
            return True
        else:
            return False

    def check_login_fail(self):
        if self.login.get_login_fail_tips() == "用户名或密码错误":
            return True
        else:
            return False

    def check_login_without_pwd(self):
        if self.login.get_login_fail_tips() == '请输入密码':
            return True
        else:
            return False

    def check_to_forget_pwd(self):
        if self.login.check_to_forget_pwd():
            return True
        else:
            return False