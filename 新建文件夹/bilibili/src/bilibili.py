#/usr/bin/python
#-*-coding:utf-8-*-


import pytest
from time import sleep
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.
import  selenium.common.exceptions as ex



# 手机app连接appium是所需要的信息
d = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "tv.danmaku.bili",
  "appActivity": ".ui.splash.SplashActivity",
  "noReset": "true"
}

# 与手机建立连接
dr = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                 desired_capabilities= d)

# 导入休眠，目的是等待app完全启动
sleep(10)

# dr.find_elements_by_id('tv.danmaku.bili:id/expand_search').click()
# s = dr.get_window_size()
# x1 = s ['width'] * 0.5
# y1 = s ['height'] * 0.5
# x2 = s ['width'] * 0.75
# y2 = s ['height'] * 0.75
# dr.swipe(x1,y1,x1,y2)

d = dr.get_screenshot_as_base64()
# 二进制保存,可以作为一个附件，以邮件的形式发出去
dr.get_screenshot_as_file(filename='路径/图片名字.png')
# 保存到本机
dr.get_screenshot_as_png()
# 自动保存图片

WebDriverWait(driver=dr,timeout=10,poll_frequency=0.5).until(EC.presence_of_all_elements_located())