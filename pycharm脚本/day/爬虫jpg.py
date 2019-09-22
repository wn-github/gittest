#/usr/bin/python
#-*-coding:utf-8-*-


import requests
import re
class Price(object):
    #类属性
    u = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
    def __init__(self):
        #对象属性
        #发送请求
        r = requests.get('https://www.58pic.com/newpic/35180567.html',headers=self.u)
        self.d= r.content.decode(encoding='gbk')
    def fenxi(self):
        #先打印下源html文件
        print(self.d)
        # r1 = re.compile(r'<img src="(.*?)" class="show-area-pic"')
        #用正则匹配
        # data = re.findall(r1,self.d)
        # urls = []
        # for i in data:
        #     urls.append('https:' + i)
        # print(data)
        # return urls

    # def download(self):
    #     n = 0
    #     for i in self.fenxi():  #urls:四个图片
    #         req = requests.get(url = i, headers = self.u )
    #         接受响应结果
    #         jieguo = req.content  #  图片  二进制
            #保存图片
            # f = open(file = f'{n}.jpg',mode= 'wb')
            # f.write(jieguo)
            # n += 1



# p1=Price()
# p1.download()  # ---->  urls
