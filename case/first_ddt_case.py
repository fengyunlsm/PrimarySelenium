#coding=utf-8
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from handle.register_handle import RegisterHandle
import HTMLTestRunner
import os, time, unittest, ddt
from base.basepage import SeleniumDriver
from util.excel_util import ExcelUtil
from page.register_page import RegisterPage

ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = SeleniumDriver("chrome", 'RegisterElement')
        self.driver.get_url('http://www.5itest.cn/register')
        self.file_name = "D:/pyProject/PrimarySelenium/image/test001.png"
        self.driver.handle_window('max')


    def setUp(self):
        self.driver.handle_window('refresh')
        self.reg = RegisterPage(self.driver)

    def tearDown(self):
        # 将错误信息保存
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screen(file_path)

    @classmethod
    def tearDownClass(self):
        self.driver.close_driver()


    #定义数据
    # @ddt.data(
    #     ['12', 'fengyunlsm', '111111', 'user_email_error', '请输入有效电子邮件地址']
    # )

    #定义函数
    # @ddt.unpack
    # def test_register_case(self, email, username, password, assertCode, assertText):
    #     # email, username, password, self.file_name, assertCode, assertText = data
    #     email_error = self.reg.register_function(email,username,password,self.file_name,assertCode,assertText)
    #     self.assertFalse(email_error, '测试失败')

    # @ddt.data(*data)
    # def test_register_case(self, data):
    #     email, username, password, assertCode, assertText = data
    #     email_error = self.reg.register_function(email,username,password,self.file_name,assertCode,assertText)
    #     self.assertFalse(email_error, '测试失败')

    def test_register_case(self, data):
        self.reg.register('')

if __name__ == "__main__":
    file_path = os.path.join(os.getcwd() + '/report/' + 'first_case1.html')
    f = open(file_path, 'wb')
    # 运行数据驱动的case
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    # 生成测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="This is first report1",description=u"这个是我们第一次测试报告1",verbosity=2)
    runner.run(suite)