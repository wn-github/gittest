#/usr/bin/python
#-*-coding:utf-8-*-

import yaml
import pytest
from time import sleep
from appium import webdriver

# @pytest.fixture(params=d)

with open(file='E:\新建文件夹\qq项目\element\qqqq.yaml',mode='r',encoding='utf-8')as fb:
    s = yaml.load(fb, Loader=yaml.FullLoader)
    # print(s)

# 手机app连接appium是所需要的信息
d = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "emulator-5554",
  "appPackage": "com.tencent.mobileqq",
  "appActivity": ".activity.SplashActivity",
  "noReset": "true"
}

# 与手机建立连接
dr = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                 desired_capabilities= d)

# # 导入休眠，目的是等待app完全启动
sleep(10)

# # 实现登录
# 第一步：点击登录按钮
dr.find_element_by_id(s['l'][0]).click()
sleep(5)
# sleep(8)
# # 第二步：向账号输入框输入账号
dr.find_element_by_id(s['k'][0]).find_element_by_class_name(s['k'][1]).click()
dr.find_element_by_id(s['k'][0]).find_element_by_class_name(s['k'][1]).send_keys('3303953035')
# # 第三步：向密码输入框输入密码
dr.find_element_by_id(s['k'][2]).send_keys('yysr19980614')
#
# # 第四部：点击登录按钮
dr.find_element_by_id(s['k'][3]).click()
sleep(10)


# 点击头像按钮
dr.find_element_by_class_name('android.widget.Button').click()
sleep(15)

# 点击设置按钮
dr.find_element_by_id('com.tencent.mobileqq:id/settings').click()
sleep(15)

dr.find_element_by_id('com.tencent.mobileqq:id/account_switch').click()
sleep(15)

dr.find_element_by_id('com.tencent.mobileqq:id/logoutBtn').click()
sleep(15)

dr.find_element_by_id('com.tencent.mobileqq:id/dialogRightBtn').click()
sleep(15)

# 测试数据的保存
# """
# 1.txt文本
# 2.excel
# 3.mysql
# 4.Jason数据【最方便】
# """
#
# t = dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.TextView')
# for i in t:
#     print(i.text)
# # 第五步：关闭app
# dr.quit()

# 先写一个退出登录的代码
# 实现参数化
# 断言  第一种：登陆成功  第二种：登陆失败
# 测试数据的保存





