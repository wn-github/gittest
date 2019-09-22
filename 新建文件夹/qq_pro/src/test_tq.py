#/usr/bin/python
#-*-coding:utf-8-*-
import pytest
import allure


# @allure.severity('')#定义用力的严重等级
# @allure.story('')#描述用例
# @allure.feature('')#定义所属模块
# @allure.attach('')#添加附件
# @allure.step('')#
#
#
#
# def setUp():
#     #每个测试用例之前执行
#     pass
#
# def tearDown():
#     #m每个测试用例执行之后执行
#     pass
#
# def setUp_class():
#     #执行测试用例之前只执行一次
#     pass
#
# def tearDown_class():
#     # 执行测试用例之后只执行一次
#     pass
#
# class qwe():
#     def setUp_method(self):
#         # 每个测试用例之前执行
#         pass
#
#     def tearDown_method(self):
#         # 每个测试用例执行之后执行
#         pass

def test_1(tianqi):
    assert tianqi['reason'] == 'successed!'

def test_2(tianqi):
    assert tianqi['reason'] == '查询不到该城市的信息'

def test_3(tianqi):
    assert tianqi['resultcode'] == '200'

