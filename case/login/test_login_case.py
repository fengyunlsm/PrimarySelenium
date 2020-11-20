import sys
sys.path.append('d:\\pyProject\\PrimarySelenium')
import os, time, pytest


class TestLoginCase():
    
    # 登录成功
    @pytest.mark.search
    @pytest.mark.buy
    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures("init_driver")
    def test_login_case(self, init_login):
        
        init_login.login_eshop("13544989573", "111111")
        assert init_login.check_login_success() == True
    
    # 登录密码错误
    @pytest.mark.login
    @pytest.mark.usefixtures("init_driver")
    def test_login_password_error_case(self, init_login):
        
        init_login.login_eshop("13544989573", "111112")
        assert init_login.check_login_fail() == True

    # 登录手机号错误
    @pytest.mark.login
    @pytest.mark.usefixtures("init_driver")
    def test_login_phone_error_case(self, init_login):
        
        init_login.login_eshop("13544989571", "111111")
        assert init_login.check_login_fail() == True

    # 密码为空
    @pytest.mark.login
    @pytest.mark.usefixtures("init_driver")
    def test_login_no_password(self, init_login):
       
        init_login.login_eshop("13544989573", "")
        assert init_login.check_login_without_pwd() == True

    # 跳转到忘记密码页面    
    @pytest.mark.usefixtures("init_driver")
    def test_login(self, init_login):
        init_login.click_forget_pwd_link()
        assert init_login.check_to_forget_pwd() == True