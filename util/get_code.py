#coding=utf-8
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time

class GetCode:
    def __init__(self, driver):
        self.driver = driver

    def get_code_image(self, file_name):
        print ('file_name---->', file_name)
        self.driver.save_code_screen(file_name)
        code_element = self.driver.get_element("code_image", "注册页面_查找验证码图")
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width']+left
        height = code_element.size['height']+top
        im = Image.open(file_name)
        img = im.crop((left,top,right,height))
        img.save("D:/pyProject/PrimarySelenium/output/image/test002.png")
        time.sleep(2)

    #解析图片获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)  #卡在这不动啊
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addFilePara("image", "D:/pyProject/PrimarySelenium/output/image/test002.png") #文件上传时设置
        res = r.post()
        time.sleep(1)
        text = res.json()['showapi_res_body']
        print(text)
        code = text['Result']
        
        return code