#/usr/bin/python
#-*-coding:utf-8-*-

from selenium import webdriver
from time import sleep

#qq邮箱
dr = webdriver.Chrome()

dr.get('https://mail.qq.com/cgi-bin/loginpage')
sleep(2)
dr.maximize_window()
sleep(2)

# 切换框架只能是id的值或者是name的值，要么先定位到框架再切换
# dr.switch_to.frame('login_frame')  # iframe:内嵌框架

# 退出倒上一层框架
# dr.switch_to.parent_frame()

# 退出框架(退出到开始的第一层框架)
# dr.switch_to.default_content()

# 获取当前窗口的句柄    列表
print(dr.current_window_handle)

# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(3)
#
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('3202037092')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('hnzdzjb68924293')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(5)
#
dr.quit()

#qq空间
# dr = webdriver.Chrome()
#
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.maximize_window()
# sleep(2)
# dr.switch_to.frame('login_frame')
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(3)
#
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('3202037092')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('hnzdzjb68924293')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(5)
#
# dr.quit()

