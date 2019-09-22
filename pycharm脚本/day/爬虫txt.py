#/usr/bin/python
#-*-coding:utf-8-*-

import re
import requests

class txt(object):
    x = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    def __init__(self):
        r = requests.get('https://www.fpzw.com/xiaoshuo/87/87590/',headers=self.x)
        self.d = r.content.decode(encoding='gbk')

    def fenxi(self):
        # 先打印下源html文件
        print(self.d)
        # 用正则匹配
        a = re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
        b = re.findall(a, self.d)
        # 写入
        ff = []
        for i in b:
            b = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/{}'.format(i[0]))
            q = b.content.decode(encoding='gbk')
            r2 = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
            f1 = re.findall(r2, q)
            for j in f1:
                u = open(r'E:\Projects\untitled\day\abc.txt', 'a')
                u.writelines(j)
                # u.close()



p1=txt()
p1.fenxi()