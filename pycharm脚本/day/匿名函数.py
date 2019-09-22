#/usr/bin/python
#-*-coding:utf-8-*-


# 匿名函数
"""
lambda 参数：代码
代码块只能写一行，不能中断
不支持判断，不支持循环
"""
# def a(x):
#     return x + 1
# a(2)
#
# f = lambda x:x + 1
# print(f(2))


# f = lambda  x,y:(x + 1) - y
# print(f(2,3))

"""
面向对象  ---> 多态
1.子类的方法名与父类的方法名一致
2.如果想使用父类的方法：
    在子类中定义一个方法
    在函数里写super().父类的方法名字
3.子类对象在使用父类方法时，只需要通过对象.子类中定义的方法名
"""
# class C(object):
#     def foo(self):
#         print('这是C类里的实例方法')
#
# class D(C):
#     def foo(self):
#         print('这是D类里的实例方法')
#
#     #super()类
#     def k(self):
#         super().foo()


# d1 = D()
# #使用D类里的实例方法
# d1.foo()
#
# #d2使用c类的实例方法
# d2 = D()
# d2.k()

# 导入oymysql模块
# import  pymysql
# # 与mysql通过connect建立连接
# pymysql.connect(host = '127.0.0.1' ,  # 连接的虚拟机的ip地址
#                 port = 3306 ,  # mysql的端口号
#                 user = 'root' ,     # mysql的主机名
#                 password = '123456' ,   # mysql的密码或者授权密码
#                 charset = 'utf8')    # mysql的数据编码方式
#                 # database="库名",  # 指定数据库，不写这个参数，默认使用所有的数据库

# 第二步：创建一个游标类似于mysql进入命令行模式
# e = d.cursor()

# 第三步：写sql语句
# sql = 'show databases '

# 第四步：执行sql语句 execute(放入需要执行的sql语句)：作用就是执行sql
# data = e.execute(sql)
# print(data)

# 查询具体结果
# e.fetchall() #获取执行sql之后的所有结果
# e.fetchone() #获取执行sql之后的第一个结果
# e.fetchmany()  #获取执行sql之后的指定条结果
# print(e.fetchall())


# 图书管理系统类
# 1.查询图书
# 2.增加图书
# 3.借阅图书
# 4.归还图书
# 5.退出系统.
# 书:书名，作者，状态

# class  xitong(object):
#
#     def __init__(self,shuming,zuozhe,zhuangtai,weizhi):
#         self.shuming = shuming
#         self.zuozhe = zuozhe
#         self.zhuangtai = zhuangtai
#         self.weizhi = weizhi
#     #魔法方法，自动调用，将对象属性的值，以字符串的形式输出
#     def __str__(self):
#         return f"《{self.shuming}》 ,{self.zuozhe} ,{self.zhuangtai} ,{self.weizhi}"
#
#
#     def print_shuming(self):
#         print(f'书名：《{self.shuming}》')
#
#     def print_zuozhe(self):
#         print(f'作者：{self.zuozhe}')
#
#     def print_zhuangtai(self):
#
#             if self.zhuangtai:
#                 print('未借出')
#             else:
#                 print('已借出')
#
#     def print_weizhi(self):
#         print(f'位置：{self.weizhi}')
#
# # a = xitong('python','guido',True,'二楼计算机区48号')
# # a.print_shuming()
# # a.print_zuozhe()
# # a.print_zhuangtai()
# # a.print_weizhi()
# class guanli(object):
#     books = []
#     def start(self):
#         self.books.append(xitong('python', 'guido', True, '二楼计算机区56号'))
#         self.books.append(xitong('c', '谭浩强', True, '二楼计算机区24号'))
#         self.books.append(xitong('java', 'westos', True, '二楼计算机区108号'))
#
#     def Menu(self):
#         self.start()
#         while True:
#             print("""
#             图书管理系统
#             1.查询图书
#             2.增加图书
#             3.借阅图书
#             4.归还图书
#             5.退出系统
#             """)
#
#             choice = input('请选择：')
#
#             if choice == '1':
#                 self.print_chaxun()
#             elif choice == '2':
#                 self.print_zengjia()
#             elif choice == '3':
#                 self.print_jieyue()
#             elif choice == '4':
#                 self.print_guihuan()
#             elif choice == '5':
#                 print('欢迎下次使用...')
#                 exit()
#             else:
#                 print('请输入正确选择')
#                 continue
#
#
#     def print_chaxun(self):
#         for xitong in self.books:
#             print(xitong)
#
#
#     def print_zengjia(self):
#         shuming = input('图书名称:')
#         self.books.append(xitong(shuming, input('作者:'), True, input('存储位置:')))
#         print('图书《{self.shuming}》增加成功' )
#
#
#     def jiancha(self, shuming):
#         for xitong in self.books:
#             if xitong.shuming == shuming:
#                 return xitong
#         else:
#             return None
#
#
#     def print_jieyue(self):
#         shuming = input('借阅图书名称: ')
#         ret = self.jiancha(shuming)
#         print(ret)
#
#         if ret != None:
#             if ret.zhuangtai:
#                 print('书籍《{self.shuming}》已经借出' )
#             else:
#                 print('书籍《{self.shuming}》借阅成功')
#
#
#     def print_guihuan(self):
#         shuming = input('归还图书名称:')
#         ret = self.jiancha(shuming)
#
#         if ret != None:
#             if ret.zhuangtai:
#                 print('书籍《{self.shuming}》归还成功')
#                 print(ret)
#             else:
#                 print('书籍《{self.shuming}》未借出' )
#
# manager = guanli()
# manager.Menu()