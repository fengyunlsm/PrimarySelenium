import json
import requests
from selenium import webdriver
import time, os, sys
base_path = os.getcwd()
sys.path.append(base_path)

class HandleJson:
    def load_json(self):
        with open("D:\\pyProject\\PrimarySelenium\\config\\cookie.json") as f:
            data = json.load(f)
        return data

    def get_data(self):
        return self.load_json()

    def write_data(self, data):
        with open("D:\\pyProject\\PrimarySelenium\\config\\cookie.json", "w") as f:
            f.write(json.dumps(data))


if __name__ == "__main__":
    hand = HandleJson()
    #hand.write_data({"item":1})
    # 获取cookies
    data = json.dumps({
        "loginPassword":"123456", 
        "mobile": "13710646151", 
        "type": 0
    })
    headers = {"Content-Type":"application/json"}
    r = requests.post('http://eshop.tslj.cn/issec/auth/session/', data=data, headers = headers)
    r_dict = json.loads(r.text)
    print (r_dict["userInfo"])
    hand.write_data(r_dict["userInfo"])
    # 提取出来存放到sessionStorage里面
    # c = requests.utils.dict_from_cookiejar(r.cookies)    
    # hand.write_data(c)
    # driver.add_cookie(cookies)
    session = hand.get_data()
    print ('session is {}'.format(session))

    driver = webdriver.Chrome()
  
    js = '''sessionStorage.setItem('userInfo', {})'''.format(session)
    print ("js is  {}".format(js))
    time.sleep(2)
    driver.get("http://eshop.tslj.cn/#/pd/141779030714187776")
    driver.execute_script('''sessionStorage.setItem('userInfo', " {'loginName': null, 'nickName': '未命名', 'mobile': '13710646151', 'memberId': '143581314679918592', 'sex': 0, 'headPortrait': 'http://tslycc.test.upcdn.net/uploads/images/1548223000317.jpg!56', 'memberStatus': null, 'employeeId': null}")''')
    h = driver.execute_script("return sessionStorage.getItem('userInfo')")
    print ("h: {}".format(h))
    cookies = hand.get_data()
    ele = driver.find_element_by_css_selector(".cart > button:nth-child(1)")
    time.sleep(2)
    ele.click()
    print ("cookies", cookies)
    time.sleep(3)
    driver.quit()


    # 到时候 跟风 
    print(hand.get_data())

handle_json = HandleJson()