import sys, os
base_path = os.getcwd()
sys.path.append(base_path)
print (base_path)
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from util.read_ini import read_ini
from util.handle_json import handle_json
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
# from pykeyboard import PyKeyboard
import time, datetime, os
from util.usr_log import UserLog
from util.dir_config import screenshot_dir


class SeleniumDriver:
    def __init__(self, browser, node=None):
        self.node = node
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()
        self.driver = self.open_window(browser) 
  
    def open_window(self, browser):
        self.loger.info({"开始打开{}浏览器".format(browser)})
        try:
            if browser == 'chrome':
                # options = webdriver.ChromeOptions()
                # prefs = {'download.default_directory': 'D:\\Download\\', 'profile.default_content_settings.popups': 0} # 设置自定义路径
                # options.add_experimental_option('prefs', prefs) # 设置默认路径
                binary_location = '/usr/bin/google-chrome'
                chrome_driver_binary = '/usr/bin/chromedriver'

                chrome_options = Options()
                chrome_options.binary_location = binary_location
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--disable-dev-shm-usage')
                chrome_options.add_argument("service_args=['–ignore-ssl-errors=true', '–ssl-protocol=TLSv1']") 
                chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
                chromedriver = chrome_driver_binary
                os.environ["webdriver.chrome.driver"] = chromedriver
                # chromedriver = '/usr/bin/chromedriver'
                driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options =chrome_options) # 输入参数为options=options
                # WAIT = WebDriverWait(driver, 5)
            elif browser == 'firefox':
                profile = webdriver.FirefoxProfile()
                profile.set_preference('browser.download.dir', 'D:\\Download\\')
                profile.set_preference('browser.download.folderlist', 2)
                profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
                driver = webdriver.Firefox(firefox_profile=profile)
            elif browser == 'ie':
                driver = webdriver.Ie()
            elif browser == 'Edge':
                driver = webdriver.Edge()
            else:
                self.loger.exception("打开浏览器失败，请检查是否输入参数有误")
            return driver
        except:
            self.loger.exception("打开浏览器失败, 请检查是否是driver版本不正确")
            return None


    def get_url(self, url):
        self.loger.info("开始打开地址 {}".format(url))
        if self.driver != None:
            if 'https://' in url:
                self.driver.get(url) # 打开对应的网站
            elif 'http://' in url:
                self.driver.get(url)
            else:
                self.loger.exception("打开地址失败")
        else:
            self.loger.exception("打开地址失败")
    
    def getLocation(self, node, info):
        by, value = self.read_ini(node, info)
        if by == 'id':
            loc = (By.ID, value)
        elif by == 'name':
            loc = (By.NAME, value)
        elif by == 'class':
            loc = (By.CLASS_NAME, value)
        elif by == 'css':
            loc = (By.CSS_SELECTOR, value)
        elif by == 'tag':
            loc = (By.TAG_NAME, value)
        elif by == 'link':
            loc = (By.LINK_TEXT, value)
        elif by == 'partial_link':
            by = (By.PARTIAL_LINK_TEXT, value)
        else:
            loc = (By.XPATH, value)
        return loc


    def wait_eleVisible(self, node, info, img_doc="", timeout=30, frequency=0.5):
        self.loger.info("等待元素 {} 可见。".format(info))
        try:
            # 等待元素是否可见
            # info 怎么转换成loc
            loc = self.getLocation(node, info)
            # 起始等待的时间 datetime
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
            # 结束等待的时间
            end = datetime.datetime.now()
            self.loger.info("开始等待时间点：{}，结束等待时间点：{}，等待时长为：{}".
                format(start,end,end-start))
        except:
            # 日志
            self.loger.exception("等待元素可见失败：")
            # 截图 - 哪一个页面哪一个操作导致的失败。+ 当前时间
            self.save_screen(img_doc)
            raise

    def js_execute(self, js):
        time.sleep(1)
        self.driver.execute_script(js)

    def handle_window(self, *args):
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.loger.info("对窗口的操作-最大化")
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.loger.info("对窗口的操作-最小化")
                self.driver.minimize_window()
            elif args[0] == 'back':
                self.loger.info("对窗口的操作-回退")
                self.driver.back()
            elif args[0] == 'go':
                self.loger.info("对窗口的操作-前进")
                self.driver.forward()
            else:
                self.loger.info('对窗口的操作-刷新')
                self.driver.refresh()
        elif value == 2:
            self.driver.set_window_size(args[0], args[1])
            time.sleep(1)
        else:
            self.loger.exception("在对窗口进行操作时，输入参数有误")
        time.sleep(2)

    def save_screen(self, img_doc):
        # 截图保存在哪里啊
        # 创建一个文件夹，以时间作为后缀命名
        # 每次保存日志的时候都会先查看是否存在某个文件夹
        tody = datetime.datetime.now().strftime("%Y-%m-%d")
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_folder = os.path.join(screenshot_dir, tody)
        if os.path.exists(screenshot_folder) == False:
            try:
                self.loger.info("开始创建文件夹, 名为{}".format(screenshot_folder))
                os.makedirs(screenshot_folder)
            except:
                self.loger.exception("创建文件夹失败")
        file_path = "{}_{}.png".format(img_doc, now)
        try:
            screen_path = os.path.join(screenshot_folder, file_path)
            self.driver.save_screenshot(screen_path)
            self.loger.info("网页截图成功。图片存储在：{}".format(screen_path))
        except:
            self.loger.exception("网页截图失败！")
    
    def save_code_screen(self, img_doc):
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        file_path = "{}_{}.png".format(img_doc, now)
        try:
            self.driver.save_screenshot(screenshot_dir +"/" + file_path)
            self.loger.info("网页截图成功, 图片存储在: {}".format(screenshot_dir +"/" + file_path))
        except:
            self.loger.exception("网页截图失败!")


    def assert_title(self, title_name):
        get_title = EC.title_contains(title_name)
        return get_title(self.driver)

    def open_url_is_true(self, url, title_name):
        self.get_url(url)
        return self.assert_title(title_name)
    
    def element_isdisplay(self, element):
        flag = element.is_displayed()
        if flag == True:
            return element


    def get_element(self, node, info, img_doc):
        '''
        获取定位元素
        @param by 定位元素
        @param value 定位的值
        return element 
        '''
        element = None
        by, value = self.read_ini(node, info)
        print('by------>', by)
        print('value------>', value)
        self.wait_eleVisible(node, info, img_doc)
        self.loger.info("查找 {} 中的元素 {}".format(img_doc, info))
        try: 
            if by == 'id':
                element = self.driver.find_element_by_id(value)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif by == 'css':
                element = self.driver.find_element_by_css_selector(value)
            elif by == 'tag':
                element = self.driver.find_element_by_tag_name(value)
            elif by == 'link':
                element = self.driver.find_element_by_link_text(value)
            elif by == 'partial_link':
                 element = self.driver.find_element_by_partial_link_text(value)
            else:
                element = self.driver.find_element_by_xpath(value)
        except:
            # 日志
            self.loger.exception("查找元素失败")
            # 截图
            img_doc = ''
            self.save_screen(img_doc)
        return self.element_isdisplay(element)
    
    def has_element(self, node, info, img_doc):
        '''
        获取定位元素
        @param by 定位元素
        @param value 定位的值
        return element 
        '''
        element = None
        by, value = self.read_ini(node, info)
        print('by------>', by)
        print('value------>', value)
        self.loger.info("查找 {} 中的元素 {}".format(img_doc, info))
        try: 
            if by == 'id':
                element = self.driver.find_element_by_id(value)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif by == 'css':
                element = self.driver.find_element_by_css_selector(value)
            elif by == 'tag':
                element = self.driver.find_element_by_tag_name(value)
            elif by == 'link':
                element = self.driver.find_element_by_link_text(value)
            elif by == 'partial_link':
                 element = self.driver.find_element_by_partial_link_text(value)
            else:
                element = self.driver.find_element_by_xpath(value)
        except:
            # 日志
            self.loger.exception("确实没没找到元素")
            return element
        return self.element_isdisplay(element)

    def find_elements(self, node, info, img_doc):
        '''
        获取定位元素列表
        @param by 定位元素
        @param value 定位的值
        return element 
        '''
        elements = None
        element_list = []
        by, value = self.read_ini(node, info)
        print('by------>', by)
        print('value------>', value)
        self.loger.info("查找 {} 中的元素 {}".format(img_doc, info))
        try:
            if by == 'id':
                elements = self.driver.find_elements_by_id(value)
            elif by == 'name':
                elements = self.driver.find_elements_by_name(value)
            elif by == 'class':
                elements = self.driver.find_elements_by_class_name(value)
            elif by == 'css':
                elements = self.driver.find_elements_by_css_selector(value)
            elif by == 'tag':
                elements = self.driver.find_elements_by_tag_name(value)
            elif by == 'link':
                elements = self.driver.find_elements_by_link_text(value)
            elif by == 'partial_link':
                elements = self.driver.find_element_by_partial_link_text(value)
            else:
                elements = self.driver.find_elements_by_xpath(value)  
        except:
            # 日志
            self.loger.exception("查找元素失败")
            # 截图          
            self.save_screen(img_doc)
        for element in elements:
            if self.element_isdisplay(element) == False:
                continue
            else:
                element_list.append(element)
        return element_list



    def find_level_element(self, node, parent_info, child_info, img_doc, parent_index = None, child_index = None):
        '''
        层级定位, 有一个父节点, 父节点找子节点
        '''
        child_by, child_value = self.read_ini(node, child_info)
        if parent_index == None:
            element = self.get_element(node, parent_info, img_doc)
        else:
            element = self.find_list_element(node, parent_info, parent_index, img_doc)
        try:
            if element != False:
                self.loger.info("查找 {} 中的元素 {}".format(img_doc, child_info))
                if child_index == None:
                    if child_by == 'id':
                        node_element = element.find_element_by_id(child_info)
                    elif child_by == 'name':
                        node_element = element.find_element_by_name(child_info)
                    elif child_by == 'class':
                        node_element = element.find_element_by_class_name(child_info)
                    elif child_by == 'css':
                        node_element = element.find_element_by_css_selector(child_info)
                    elif child_index == 'tag':
                        node_element = element.find_element_by_tag_name(child_info)
                    elif child_index == 'link':
                        node_element = element.find_element_by_link_text(child_info)
                    else: 
                        node_element = element.find_element_by_xpath(child_info)
                else:
                    if child_by == 'id':
                        node_element = element.find_elements_by_id(child_value)[child_index]
                    elif child_by == 'name':
                        node_element = element.find_elements_by_name(child_value)[child_index]
                    elif child_by == 'class':
                        node_element = element.find_elements_by_class_name(child_value)[child_index]
                    elif child_by == 'css':
                        node_element = element.find_elements_by_css_selector(child_value)[child_index]
                    elif child_index == 'tag':
                        node_element = element.find_elements_by_tag_name(child_value)[child_index]
                    elif child_index == 'partial_link':
                        node_element = element.find_element_by_partial_link_text(child_value)[child_index]
                    elif child_index == 'link':
                        node_element = element.find_elements_by_link_text(child_value)[child_index]
                    else: 
                        node_element = element.find_elements_by_xpath(child_value)[child_index]
                return self.element_isdisplay(node_element)
        except:
            self.loger.exception("查找元素失败")
            self.save_screen(img_doc)
    
    def find_list_element(self, node, info, index, img_doc):
        '''
        通过列表来进行获取
        '''
        # 等待元素出现
        self.loger.info("查找 {} 中的第 {} 个元素 {}".format(img_doc, index ,info))
        self.wait_eleVisible(node, info, img_doc) # 等待元素出现
        try:
            elements = self.find_elements(node, info, img_doc)
            if elements != False:
                if len(elements) < index:
                    self.loger.error ("元素个数小于index")
                    return None
                return elements[index]
        except:
            # 日志
            self.loger.exception("查找元素失败")
            # 截图
            self.save_screen(img_doc)


    def send_value(self, node, info, key, img_doc):
        
        if isinstance(info, str): 
            element = self.get_element(node, info, img_doc)
        else:
            self.loger.info("在 {} 值为 {}".format(img_doc, key))
            element = info
        if element != False:
            if (element != None):
                return element.send_keys(key)
            else:
                self.loger.exception("元素定位失败")
        else:
            self.loger.exception("元素隐藏")

    def set_node(self, node):
        self.node = node

    def click_element(self, node, info, img_doc):
        element = self.get_element(node, info, img_doc)
        self.loger.info('点击 {}  中的元素 {}'.format(img_doc, info))
        if element != False:
            if element != None:
                element.click()
            else:
                self.loger.exception('元素无法定位，所以无法点击')
        else:
            self.loger.exception('元素不可见，所以无法点击')


    def set_cookies(self):
        
        cookies = handle_json.get_data()
        self.driver.delete_all_cookies
        for item in cookies:
            if item['name'] == "SESSION":
                self.loger.info("本次登录的cookie： {} ".format(item))
                cookie = item
                break
        
        time.sleep(1)
        self.driver.add_cookie(cookie)
        time.sleep(2)
        self.loger.info("确认是否保存cookies {}".format(handle_json.get_data()))

    def get_cookies(self):
        # 接口
        # 依赖
        cookie = self.driver.get_cookies()
        # 清空json 里面的内容
        handle_json.write_data(cookie)

    def check_box_isseleted(self, info, img_doc, check=None):
        '''
            如果已经选中的话，并且要求选中，不进行任何操作，否则取消选中
            如果没有选中的话，并且不要求选中，不进行任何操作，否则点击选中
        '''
        element = self.get_element(info, img_doc)
        if element != False:
            flag = element.is_selected()
            if flag == True:
                if check == 'check':
                    pass
                else:
                    self.click_element(info)
            else:
                if check == 'check':
                    self.click_element(info)
        else:
            print('元素不可见，没法选中')

    def read_ini(self, node, info):
        '''
        根据info 来获取 by vlaue
        '''
        data = read_ini.get_value(node, info)
        data_list = data.split('^')
        return data_list

    def get_selected_element(self, info, key, index=None):
        '''
        先获取selected 对象
        再获取对应的项
        '''
        select_element = None
        if index == None:
            select_element = self.get_element(info)
        else:
            select_element = self.find_list_element(info, index)
        Select(select_element).select_by_value(str(key))

    def upload_file(self, file_name):
        '''
        非input 类型上传文件
        @param filename
        '''
        # pyKey = PyKeyboard()
        # pyKey.type_string(file_name)
        # time.sleep(2)
        # pyKey.tap_key(pyKey.enter_key)
        pass

    def move_to_element(self, element, img_doc):
        '''
        鼠标移动到某个元素上
        '''
        # element = self.get_element(info, img_doc)
        
        self.loger.info("鼠标移动到上方")
        ActionChains(self.driver).move_to_element(element).perform()

    def keyboard(self, node, info, key, img_doc):
        element = self.get_element(node, info, img_doc)
        self.loger.info("在 {} 元素 {} ".format(info, img_doc))
        try:
            if key == 'enter':
                element.send_keys(Keys.ENTER)
            elif key == 'tab':
                element.send_keys(Keys.TAB)
            elif key == 'c':
                element.send_keys(Keys.CONTROL,'c')
            elif key == 'a':
                element.send_keys(Keys.CONTROL,'a')
            elif key == 'x':
                element.send_keys(Keys.CONTROL, 'x')
            elif key == 'v':
                element.send_keys(Keys.CONTROL, 'v')
            elif key == 'space':
                element.send_keys(Keys.SPACE)
            elif key == 'tab':
                element.send_keys(Keys.TAB)
            else:
                self.loger.error("无效按键")
        except:
            self.loger.exception("按键失效")

    def refresh_h5(self):
        '''
        强制刷新
        '''
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL)

    def switch_frame(self, info=None):
        if info != None:
            self.driver.switch_to.frame(info)
        else:
            self.driver.switch_to_default_content()

    def switch_alert(slef, info, value=None):
        self.loger.info('切换到警告弹窗')
        windows_alert = self.driver.switch_to.alert
        if info == 'accept':
            if value == None:
                windows_alert.accept()
            else:
                windows_alert.send_keys(value)
                windows_alert.accept()
        else:
            windows_alert.dismiss()

    def close_driver(self):
        self.driver.quit() # 会关闭所有关联的窗口，close只会关闭焦点所在的窗口

if __name__ == "__main__":
    selfnium_driver = SeleniumDriver('chrome', "element")
    selfnium_driver.open_url_is_true('http://www.imooc.com/wenda/save', '慕课网')
    selfnium_driver.handle_window("max")
    # 登录
    selfnium_driver.get_element('username', "登录_查找用户名")
    selfnium_driver.send_value('username', '2399548030@qq.com', '登录_输入用户名')
    selfnium_driver.get_element('password', '登录_查找密码')
    selfnium_driver.send_value('password', '6329017abc', '登录_输入密码')
    selfnium_driver.click_element('login_button', '登录_点击按钮')
    time.sleep(1)
    
    # 移动到某个元素上
    # eleement = selfnium_driver.find_level_element(parent_info="sidebar", child_info="sidebar_selection", img_doc="首页_侧边选择", parent_index=0, child_index=-1)
    # selfnium_driver.move_to_element(eleement)

    # 切换到不同的iframe 上进行操作
    # selfnium_driver.switch_frame("ueditor_0")
    # selfnium_driver.temp('text_box', '问答_填写')
    # selfnium_driver.switch_frame()
    # selfnium_driver.find_elements('tag', '问答_选择标签')[0].click()

    # 弹窗测试
    time.sleep(2)
    selfnium_driver.close_driver()

