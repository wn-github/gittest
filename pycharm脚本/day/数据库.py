#/usr/bin/python
#-*-coding:utf-8-*-

# 导入oymysql模块
import  pymysql
# 与mysql通过connect建立连接
d = pymysql.connect(host = '127.0.0.1' ,  # 连接的虚拟机的ip地址
                port = 3306 ,  # mysql的端口号
                user = 'root' ,     # mysql的主机名
                password = '123456' ,   # mysql的密码或者授权密码
                charset = 'utf8')    # mysql的数据编码方式
                # database="库名",  # 指定数据库，不写这个参数，默认使用所有的数据库

# 第二步：创建一个游标类似于mysql进入命令行模式 mysql > select * from xx;
e = d.cursor()

# 第三步：写sql语句
sql = 'show databases '

# 第四步：执行sql语句 execute(放入需要执行的sql语句)：作用就是执行sql
# data = e.execute(sql)
# print(data)
# 执行多条sql语句：e.executemany(sql语句)

# 第五步：查询具体结果
"""
1.先找游标
2.再使用fetch命令
"""
# fetchall() #获取执行sql之后的所有结果
# fetchone() #获取执行sql之后的第一个结果
# fetchmany(数字)  #获取执行sql之后的前n条结果
# print(e.fetchmany(5))




# 创建一个库
# sql1 = 'create database Tuesday character set utf8 '
# e.execute(sql1)

# 创建表
# sql2 = 'use Tuesday'
# sql3 = 'create  table  day  (id  int(8), class  char(20), name char (20))'
# e.execute(sql2)
# e.execute(sql3)

# 数据插入
# sql4 = "insert into Tuesday.daybyday value ('5','1901','孙泽')"
# e.execute(sql4)

# 保存操作
"""
1.找到连接
2.通过连接保存，使用commit()  ---->   保存数据到数据库
"""
# d.commit()

# 插入多条数据
# sql5 = "insert into Tuesday.daybyday values('6','1806','秦安'), ('7','1803','万代')"
# e.execute(sql5)

# 更新操作
# sql6 =" update Tuesday.daybyday set name = '诺瓦' "
# e.execute(sql6)

# 查看表中内容
# sql5 = 'select * from daybyday '
# e.execute(sql5)
# print(e.fetchall())








# 创建一个库
sql1 = 'create database Wednesday character set utf8 '
e.execute(sql1)

# 创建表
sql2 = 'use Wednesday'
sql3 = 'create  table  day  (id  int(8), name  char(20), zhiwei char (20), URL char(200), type char (20),zhuangtai char(20), shuliang char(20), dizhichar char(20), time char(20), xuqiu char(20))'
e.execute(sql2)
e.execute(sql3)


f = open(file='a.txt',mode='r',encoding='utf-8')
g = f.read()
# print(g)
h = []
c = g.replace('(','').replace(';','').replace('\n','').split('),')
for i in c:
    h.append(i.replace("'",'').split(','))
# print(h)

    for i in h:
        sql4 = "insert into Wednesday.day value {i}"
        e.execute(sql4)
        # print(i)
        # print(j)
        #     print(h[i][j])






































































































