#/usr/bin/python
#-*-coding:utf-8-*-

import xlrd
import pymysql



d = pymysql.connect(host = '127.0.0.1' ,  # 连接的虚拟机的ip地址
                port = 3306 ,  # mysql的端口号
                user = 'root' ,     # mysql的主机名
                password = '123456' ,   # mysql的密码或者授权密码
                charset = 'utf8')#,  # mysql的数据编码方式
                # database="Friday") # 指定数据库，不写这个参数，默认使用所有的数据库


e = d.cursor()


# sql1 = 'create database Friday character set utf8 '
# e.execute(sql1)

# sql2 = 'use Friday'
# sql3 = 'create  table  day  (id  int(8), name  char(20), age char (20), sex char (20))'
# e.execute(sql2)
# print(e.execute(sql3))


# sql = "insert into Friday.day values('6','1806','秦安'), ('7','1803','万代')"
# e.execute(sql)
# sql2 = 'select * from  day'
# e.execute(sql2)
# print(e.fetchall())

# 第一步：打开Excel
c= xlrd.open_workbook(r'E:\Projects\untitled\day\222.xlsx')
table = c.sheets()[0]
for i in range(table.nrows):
    a = table.row_values(i)
    print(a)
    # sql =("insert into Friday.day values (%s,%s,%s,%s)")
    # e.execute(sql,(a[0],a[1],a[2],a[3]))






