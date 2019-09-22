#/usr/bin/python
#-*-coding:utf-8-*-


# 爬虫：通过python代码获取网络中存放的数据资源（文件、图片、MP3）
# 反爬虫：防止资源被爬虫代码获取
# 反爬机制：属于反爬虫的一种技术手段之一
# 最常见的反爬机制：
# 1.封ip地址
# 2.封物理网卡的MAC地址
# 3.验证码
# 4.服务器传输给浏览器的数据通过异步加载

"""
re模块
requests   python发送http/https请求，接收响应数据的一个第三方库

"""

#
import re
import requests

"""
User-Agent: 代表浏览器
"""


x = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#
# #get请求  获取资源
#
# #第一步：发送请求
# r = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/17125664.html',headers= x)
# #第二步：获取响应的结果、数据
#
# """
# content  获取请求之后的响应数据
# """
#
# data = r.content.decode(encoding='gbk')
# # print(data)
#
#
# a = re.compile(r'<h2>(.*?)</h2>')
# # '<h2>(.*?)</h2>'
# b = re.findall(a,data)
# print(b)
#
# c = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /><br />')
# f = re.findall(c,data)
# print(f)

# y=open(file='www.txt',mode='w',encoding='utf-8')
# for i in f:
#     y.write(f'{i}\n')

# <href>  超链接


r = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/',headers=x)
data = r.content.decode(encoding='gbk')
# print(data)

a = re.compile(r'<dd><a href="(.*?)">(.*?)</a></dd>')
b = re.findall(a,data)
# print(b)

ff = []
for i in b :
    b = requests.get(url='https://www.fpzw.com/xiaoshuo/87/87590/{}'.format(i[0]) )
    q = b.content.decode(encoding='gbk')
    r2 = re.compile(r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />')
    f1 = re.findall(r2,q)
    for j in range(len(f1)):
        u = open(r'E:\Projects\untitled\day\ccc.txt', 'a')
        u.writelines(j)
        # u.close()






































