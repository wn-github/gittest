#/usr/bin/python
#-*-coding:utf-8-*-

import pymysql
user_1 = pymysql.connect(
                  host='127.0.0.1',
                  port=3306,
                  user='root',
                  password='123456',
                  charset='utf8',
                  database='Sunday'
   )
d = user_1.cursor()
x=[]
f=open(file='新建文本文档.txt',mode='r',encoding='utf-8')
k=(f.readlines())
for i in k:
    s=i.replace('\n',' ')
    g=s.split(',',)
    x.append(g)
# sql3='create table  e(qq text,ww text ,ee text,rr text)charset="utf8"'
sql4='insert into Sunday.e value(%s,%s,%s,%s)'
# d.execute(sql3),
d.execute(sql4,(x[0],x[1],x[2],x[3]))