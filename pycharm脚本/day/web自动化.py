#/usr/bin/python
#-*-coding:utf-8-*-

# 导入selenium中的webdriver模块
from selenium import webdriver
from time import sleep

# 打开浏览器
dr = webdriver.Chrome()

# 在地址栏中输如网址并请求
# dr.get('https://www.baidu.com')
# sleep(2)
# dr.get('https://www.jd.com')
# sleep(3)

# 获取标题
# 断言，将实际结果跟预期结果做对比
# dr.title
# assert dr.title == '百度一下,你就知道'
# 获取网址
# print(dr.current_url)
# assert dr.current_url =='https://www.baidu.com/'

# 回退到上一个界面
# dr.back()
# sleep(3)

# 前进到下一个页面
# dr.forward()

# 页面最大化
# dr.maximize_window()

# 设置窗口大小
# dr.set_window_size(1000,1000)
# sleep(3)

# 设置浏览器窗口位置
# dr.set_window_position(100,100)
# sleep(3)

# 页面最小化
# dr.minimize_window()

# selenium的核心：定位
# 提供的定位方法有8种：

# 1.id 定位  唯一的
# 动作：点击click（），输入send_keys（内容）

# dr.find_element_by_id('kw').send_keys('python')
# sleep(3)
# dr.find_element_by_id('su').click()
# sleep(2)

# 2.class 定位
# dr.find_element_by_class_name('s_ipt').send_keys('python')
# sleep(3)
# dr.find_element_by_class_name('btn self-btn bg s_btn').click()
# sleep(2)

# 3.name定位
# dr.find_element_by_name('wd').send_keys('python')
# sleep(3)
# dr.find_element_by_id('su').click()
# sleep(2)

# 4.link_text 定位  文本定位  唯一的
# dr.find_element_by_link_text('新闻').click()
# sleep(3)

# 5.partial_link_text   模糊文本
# dr.find_element_by_partial_link_text('hao').click()
# sleep(3)

# 6.tag_name  标签定位   不是唯一的
# dr.find_element_by_tag_name('')

# 7.xpath  路径定位   路径标记语言
# dr.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# sleep(3)
# dr.find_element_by_id('su').click()
# sleep(2)

# 8.css_selector  通过css定位
# dr.find_element_by_css_selector('#kw').send_keys('python')
# sleep(3)
# dr.find_element_by_id('su').click()
# sleep(2)

# 定位一组元素：一次性定位到多个某些属性相同的元素
# 层级定位：先定义到大的范围，再从大的范围里定位元素

# dr.get('https://www.ctrip.com/')
# ww = dr.find_element_by_xpath('//*[@id="J_roomCountList"]').find_elements_by_tag_name('option')
# for i in  ww:
#     i.click()
#     sleep(2)

dr.get('https://www.jd.com/')
aa = dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')
for i in aa:
    i.click()

    sleep(2)


# 关闭浏览器
dr.quit()


















