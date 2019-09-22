#/usr/bin/python
#-*-coding:utf-8-*-

import pymysql
import xlwt
user_1 = pymysql.connect(
                 host='127.0.0.1',
                  port=3306,
                  user='root',
                  password='123456',
                  charset='utf8',
                  database='Friday'
   )
d = user_1.cursor()
sql1='select * from  day;'
k=d.execute(sql1)
a=d.fetchall()
x=[]
for i in a:
     s=list(i)
     x.append(s)
# # print(x)
d =xlwt.Workbook()
table =d.add_sheet("表一")
for i in range(len(x)):
     for j in range(len(x[i])):
          table.write( i,j,x[i][j])
d.save('www.xls')
