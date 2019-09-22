#/usr/bin/python
#-*-coding:utf-8-*-

import re
import requests
class P(object):
    def g(self):
        x = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        d=requests.get(url='https://www.qiushibaike.com/text/',headers=x)
        t=d.content.decode("utf-8")
        c=re.compile('<div class="content">(.*?)</span>',re.S)
        e=c.findall(t)
        for i in range(len(e)):
            f = open("a.txt","a",encoding="utf-8")
            f.write(e[i])

a=P()
a.g()

