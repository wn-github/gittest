#/usr/bin/python
#-*-coding:utf-8-*-

#flask
#flask web框架
"""
1.django
2.flask
3.bottle
4.toemdon
"""

#web页面一般分两种
"""
1.静态的，页面不会发生变动的
2.动态的，页面的数据实时刷新的
"""

#flask -- python开发web网页，数据交互的一个web框架

from flask import Flask

APP = Flask(__name__)

@APP.route('/')
def hello():
    return "hello flask"

if __name__=='__main__':
    APP.run(host='127.0.0.1',port=6000)




























