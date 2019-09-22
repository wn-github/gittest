#/usr/bin/python
#-*-coding:utf-8-*-


import pytest
import allure
from selenium import webdriver
from time import sleep

class Test_blbl():

    def test_1(self,bili):
        dr = bili.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div[1]/ul/li[1]/a/text()').text
        assert dr == '主站'



    def test_2(self,bili):
        bili.find_element_by_xpath('//*[@id="header-mobile-app"]').click()
        sleep(3)
        dr = bili.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/p[1]').text

        sleep(3)

        assert dr =='关注我们'


    def test_3(self,bili):
        bili.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div[1]/ul/li[3]/a').click()
        sleep(3)
        bili.find_element_by_xpath('/ *[ @ id = "track_navigation_bar"] / ul / li[2] / a').click()
        sleep(3)
        dr = bili.find_element_by_xpath('//*[@id="track_home"]/h2').text

        assert dr == '游戏列表'



