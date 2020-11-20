#coding=utf-8
import sys, time, os
base_path = os.getcwd()
sys.path.append(base_path)
from util.get_code import GetCode


class RegisterPage(object):
    """
    获取元素
    """
    def __init__(self, driver):
        self.fd = driver

    def register(self, email, username, password, file_name):
        self.fd.send_value('user_email', email, "注册页面_输入邮件地址")
        self.fd.send_value('user_name', username, "注册页面_输入用户名")
        self.fd.send_value('password', password, "注册页面_输入密码")
        # self.send_user_code(file_name)
        time.sleep(12)
        self.fd.click_element('register_button', "注册页面_点击注册按钮")


    def check_registerbutton_exist(self):
        # 判断元素是不是不存在
        # self.fd.wait_eleVisible('')
        time.sleep(0.5)
        
        if self.fd.get_element('register_button', "注册页面_查找注册按钮") == None:
            print('元素不存在')
            return False
        else:
            print('元素存在')
            return True
    

    #输入验证码
    def send_user_code(self,file_name):
        get_code_text = GetCode(self.fd)
        code = get_code_text.code_online(file_name)
        self.send_value("code_image", code, "注册页面_输入验证码")