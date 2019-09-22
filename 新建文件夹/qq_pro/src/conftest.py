#/usr/bin/python
#-*-coding:utf-8-*-

import pytest
import requests
from until.tq_tqsj import tqsj as g

@pytest.fixture(params=g())
def tianqi(request):
    url = "http://v.juhe.cn/weather/index"
    headers = {
        'User-Agent': "PostmanRuntime/7.17.1"
    }
    querystring = {"key": "f2e737ca1358a3c75e0b4d8e66b52adc", "cityname": f"{request.param}"}
    response = requests.get(url=url, headers=headers, params=querystring)
    return response.json()

def tianqi_2(request):
    url = "http://v.juhe.cn/weather/uni"
    headers = {
        'User-Agent': "PostmanRuntime/7.17.1"
    }
    querystring = {"key": "f2e737ca1358a3c75e0b4d8e66b52adc"}
    res = requests.get(url=url, headers=headers, params=querystring)
    return res.json()