#/usr/bin/python
#-*-coding:utf-8-*-

#
import re
import requests

x = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}
r = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/',headers = x )
data = r.content.decode(encoding='gbk')
d = re.compile(r"""<dd><a href="(.*?)">(.*?)</a></dd>""")
f = re.findall(d,data)
ff = []
for i in f :
    b = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/{}'.format(i[0]) )
    q = b.content.decode(encoding='gbk')
    r2 = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
    f1 = re.findall(r2,q)
    for j in f1:
        u = open(r'E:\Projects\untitled\day\ccc.txt', 'a')
        u.writelines(j)
        u.close()
