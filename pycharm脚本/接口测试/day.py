#/usr/bin/python
#-*-coding:utf-8-*-

# 接口测试：验证url是否能够正常请求和响应的过程

import requests
class tianqi():

    url = "http://v.juhe.cn/weather/index"

    headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "dd6a254b-763c-42d2-bbf1-818c7d57ca41"
        }
    def test_1(self):
        querystring = {"key": "f2e737ca1358a3c75e0b4d8e66b52adc", "cityname": "北京"}
        response = requests.get(url=self.url, headers=self.headers, params=querystring)
        # 直接转化为json
        html = response.json()
        assert html['reason'] == 'successed!'
        # 将json字符串转化成字典
        # html = json.loads(html)
        # 将字典转化成json字符串
        # aaa = json.dumps(html)
    def test_2(self):
        querystring = {"key": "f2e737ca1358a3c75e0b4d8e66b52adc", "cityname": "郭北"}
        response = requests.get(url=self.url, headers=self.headers, params=querystring)
        # 直接转化为json
        html = response.json()
        assert html['reason'] == '查询不到该城市的信息'

ex = tianqi()
ex.test_1()
ex.test_2()