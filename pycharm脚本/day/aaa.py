#/usr/bin/python
#-*-coding:utf-8-*-

class mysql(object):
    e=[]
    a=open(file='a.txt',encoding='utf-8')
    b=a.readlines()
    # print(b)
    for i in b:
        c=i.replace('\n','').replace("'",'').replace('(','').replace(';','').replace(')','')
        d=c.split(',')
        e.append(d)
    f=len(e)
    e.pop(f-1)
    def biao(self):
        import pymysql
        a = pymysql.connect(host='127.0.0.1',  # 连接数据库，数据库的IP地址或主机名，一般是IP地址
        port=3306,  # 端口号
        user='root',  # 数据库用户名
        password='123456',  # 数据库密码
        charset='utf8',  # 编码方式
        database='Wednesday'  # 有就会自动切换到这个库，没有默认使用所有的库
        )
        b = a.cursor()
        # sql1 = "create table day2( id char(8),mingcheng varchar (12),zhiwei char(20),URL char (80),type char(20),zhuangtai char (20),guomo char(20),dizhi char(30),yaoqiu1 char(15),yaoqiu2 char(12))"
        # b.execute(sql1)
        for i in self.e:
            sql="insert into Wednesday.day value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            b.execute(sql,(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
a=mysql()
a.biao()
