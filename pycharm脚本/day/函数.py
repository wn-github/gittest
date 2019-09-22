#/usr/bin/python
#-*-coding:utf-8-*-

# 什么是函数
# 组织好的代码，可以重复使用，具有一功能的代码

# 写函数的格式
# 第一个关键字：def ，函数名字，命名规则和变量的命名规则一样
# 函数的参数
# 返回值
#标准书写格式
#def 函数名（参数）:
#    代码
#    return  返回值

#求和
#sum（）  #python的内置函数

#无参数，无返回值
#组织函数代码
# def add():
#     n=0
#     for i in range(100):
#         n += i
#     print(n)
#
# add()

#函数的使用
#1.先写函数名
#2.如果里面有参数，则传入

#有参数，无返回值
#x 参数类型属于必填参数，使用函数的时候必须传入值
# def add(x):
#     n=0
#     for i in range(x+1):
#         n += i
#     print(n)
#TypeError: add() missing 1 required positional argument: 'x'
# add(100)





#有参数，有返回值
# def add(x):
#     n=0
#     for i in range(x+1):
#         n += i
#     print(n)
#     return n  #函数没有返回值是没有意义的
#     print('1234')

#return作用：
# 1.返回值
# 2.标识一个函数的结束
#TypeError: add() missing 1 required positional argument: 'x'
# print(add)#直接打印函数名--结果是函数在内存中的位置
# add(2)
# print(add(2))
#当函数没有返回值时，默认返回None


# #全局变量
#全局变量定义之后，在整个脚本的所有行都可用

#局部变量
#局部变量定义之后，只能在特定的范围使用

# a = 1000  #全局变量
# def cha(x1,x2):
#     #局部变量
#     b=10000
#     chazhi = b - x1 - x2
#     return chazhi
#
# print(cha(100,10))

#大于等于2以后的任意整数数字的质数之和  用函数写

# def zhishu(x):
#     a = 1
#     for i in range(2,x+1):
#     # print(i)
#         for j in range(2,i):
#         # print(j)
#             if i % j == 0:
#                 break
#             else:
#                 a += 1
#     return a
# print(zhishu(100))

#global
# def k():
#     global  a
#     a = '经过global定义的全局变量'
#     print(a)
#
# k()
#
# print(a)

#参数类型第二种，默认参数  y=100 y后面的是默认值
#在函数使用的时候，如果不对默认参数进行赋值，那么就使用默认值
#给默认参数赋值，就使用传入的值
# def f(x,y=10):
#     print( x * y )
#
# f(10)


#参数类型第三种，可变长参数 *args  **kwargs
#1.传入多个值
#2.args是元组的形式
#3.传入的多个值被转换为一个元组


#*args
# def d(*args):
#     a,b,c =args
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(type(args))
#
# d((1,),(2,),(3,))

# a=('1')
# print(type(a))

#**kwargs
#1.传入值的时候要以类似于字典的形式传入 (a1=2,a2=3,a3=4)
#2.kwargs是字典，可以使用字典的所有函数
#3.z,x,c = kwargs.values()
#
# def j(**kwargs):
#     print(kwargs)
#     z,x,c = kwargs.values()
#     print(z)
#     print(x)
#     print(c)
#
# j(a1=2,a2=3,a3=4)

# def canshu(*args):
#     print(args)
#     if len(list(args))== 0:
#         print('请为参数赋值，输入两个或四个数字，英文逗号隔开')
#     elif len(args) == 2:
#         if int(args[0]) > int(args[1]):
#             zhihe = 0
#             for i in range(args[1], int(args[0] + 1)):
#                 jiecheng = 1
#                 for j in range(args[1], i + 1):
#                     jiecheng *= j
#             zhihe +=  jiecheng
#             print(zhihe)
#     elif len(list(args))== 4:
#         s=[]
#         for q in  args:
#             for w in  args:
#                 for e in  args:
#                     for r in  args:
#                         if q != w and w != e and e!= r and q != r and w != :
#                             s.append(q *1000 + w *100 +e *10 + r)
#         print(len(s))
#     else:
#         print("该函数不执行")
#         return canshu()
# canshu(3,1)


# def kebian(**kwargs):
#     keys=kwargs.keys()
#     values=kwargs.values()
#     str_list=[]
#     list_1=[]
#     tuple_list=[]
#     set_list=[]
#     dict_list=[]
#     num_list=[]
#     for i in values:
#         if type(i) == str:
#             str_list.append(i)
#         elif type(i) == list:
#             list_1.append(i)
#         elif type(i) == tuple:
#             tuple_list.append(i)
#         elif type(i) == set:
#             set_list.append(i)
#         elif type(i) == dict:
#             dict_list.append(i)
#         elif type(i) == int or float or bool:
#             num_list.append(i)


# d = {}
# def func1(x , *args):
#     # print(x,args)
#     b = sum(args)
#     s = x + b
#     return s
#
# def func2(z):
#     return z
#
# i = func1(1,1,2)
# y = func2([1,2,3])
# e = d.fromkeys(y,i)
# print(e)


 #设计一个用户登录后生成session的函数，x为用户名，y为密码。
 #当用户密码都输入正确时，将用户名和密码组成一个新的字符串，随机取6~ 8位字符作为用户登录后的session
 #当用户名和密码组成的字符串“A”长度小于8位时，自动添加0~ 9任意数字到“A"， 再随机生成6~ 8位字符作为用户登录后的session
 #不知道session 是什么自己百度去?


# import random
# d = {'admin':'12345','abc':'123','user':'54321'}
# def session(x,y):
#     A = ''
#     for i,c in d.items():
#         if x == i and d[i] == y:
#             A = x + y
#             while True:
#                 if len(A) >= 8:
#                     a = random.randint(6,8)
#                     b = ''
#                     for j in range(a):
#                         q = random.choice(A)
#                         b += q
#                     return f'这是session：{b}'
#                 else:
#                     e = random.randint(0,9)
#                     f = str(e)
#                     A += f
#     else:
#         return '请重新输入用户名和密码'
#
# print(session('admin','12345'))
# print(session('abc','123'))
# print(session('admin',2))


# def k():
#     print('k函数内的代码')
#     for i in  range(10):
#
#         print(i)
#
#
# def f():
#     k()
#
#
# f()


#python 读写txt文本，对文件的操作
#打开文件
# f = open(file='a.txt',encoding='utf-8')
#读取数据
# print(f.read())  #read()读取全部
#读取出来的数据以列表的形式保存
# print(f.readlines())

"""
file:指的是文件名字，或者说文件在计算机中存放的路径 [必填参数]
mode:'r'表示读取 ，'w'表示写入，会自动创建一个文件[没有文件时]
     'x'创建文件并写入  'a'向文件中添加数据  'b'二进制的形式  
     'rb' 应用于读取照片、MP3、MP4  'wb'  应用于写入照片、MP3、MP4
"""
# f = open(file='b.txt',mode='a',encoding='utf-8')
# f.write('\nhello world')

#打开照片
# f = open(file=r'‪C:\Users\wn\Desktop\a.jpg',mode = 'rb')
# #保存照片
# d = open(file='hhh.jpg',mode= 'wb')
# d.write(f.read())


#写两个函数，函数1：读取电脑中任意位置的txt文件，读取文件里的所有内容
#函数2：向txt文件中写入数据，可以追加写入，保存文件位置由使用者自己选择
#打开照片
f = open(file=r'C:\Users\wn\Desktop\a.jpg', mode='rb')
#将照片里的内容读取

#打开另一照片
d = open(file='kkk.jpg', mode='wb')
#向照片里写入二进制数据
d.write(f.read())


# python --- 面向对象
#类是对客观事物的抽象，对象是类的实例
#类的书写格式
"""
class 类名（）：
    #类的代码
    #代码包括，循环、判断、函数
"""


#定义一个动物园的类
# class zoo(object):   #（继承于哪一个类）
    #属性
    # dongwu = '老虎'
    # def __init__(self,chide):
        # self.chide = chide
    #方法
    # def biaoyan(self):
    #     print(f'有一个动物园，{self.dongwu}在表演！')


#类使用
#第一步：创建对象
# a = zoo()  #a对象
#第二步：使用对象操作类的属性、方法
# print(a.dongwu)
# a.biaoyan()

"""
object #中文叫做对象
        #所有类的基类
self   #方法里第一个参数必须是self
        #指代自身、实例
对象可以使用类的属性、方法
"""


"""
类的组成：
1、属性：
    #从公有、私有的角度
    公有属性
    私有属性
    #从类、对象的角度
    类属性
    对象属性 == 实例属性
    
2、方法
"""

# #老师类
#
# class Teacher(object):
#     #类属性： 公有  私有
#     #公有属性
#     ke = ['语文','数学','外语','生物']
#     #私有属性，双英文的下划线开头
#     __banji__ = '1903'
#     def __init__(self):
#         pass #占位符
#
#     def kl(self):
#         print(f'方法访问类的公有属性：{self.ke'f'}')

#学生类
# class student(object):
    # name = '帅锅'
    # banji = '1903'
    # sex = True  # 男生：True  女生：False

    #类的属性
    # book = ['言情系列','武侠系列','都市系列']

    #初始化方法
    # def __init__(self,name,banji,sex):
        #对象的属性
        # self.name = name   #name的值叫做战三
        # self.banji = banji
        # self.sex = sex


    #打印名字的方法
    # def print_name(self):
    #     print(f'有个学生的名字叫做{self.name}')
    #打印学生的班级
    # def print_banji(self):
        # print(f'有个学生叫{self.name},在{self.banji}班级里')
    #打印学生的性别
    # def print_sex(self):
        # if self.sex:
        #     print(f'哇！靓仔！！！')
        # else :
        #     print(f'哇！靓女！！！')

    #打印学生书包里的图书
    # def print_book(self):
        # for i in  self.book:
        #     print(f'书包里的书有：{i}')

    #L类可不可以使用对象的属性
"""
    1.类不能使用对象的属性
    类名 --->  代表类
    2.类可以访问类的属性
"""
    #对象可不可以使用对象属性、类属性
"""
    1.对象可以访问对象属性
    2.对象可以访问类属性
"""

# print(student.book)
# def __init__(self):


# # 使用类的代码
# a = student('战三',12,True)
# a.print_name()
# a.print_banji()
# a.print_sex()
# a.print_book()
#
# b = student('李思',12,False)
# b.print_name()
# b.print_banji()
# b.print_sex()


# a = student('张三',12,True)
# print(a.book)


# 老师类
class thcher(object):
    #类属性：公有的 都可以拿来使用的  私有：只能在某个地方用
    # 公有属性
    ke = ["语文","数学","英语","生物"]
    # 私有属性标志 双下划线开头 __
    __grade = "1903"
    def __init__(self,a,b):
        # 公有的对象属性
        self.a = a
        # 私有的对象属性
        self.__b  =  b

        self.c = 'hello'
        # pass   # 类似于占位符

    def kl(self):
        print(f"方法访问类的公有属性：{self.ke}")
        print(f"方法访问类的私有属性：{self.__grade}")

    #实例方法
    def g(self):
        print(f"方法访问对象的公有属性：{self.a}")
        print(f"方法访问对象的私有属性：{self.__b}")

    #私有方法
    def __w(self):
        print('私有方法')
    #在类的外部通过对象，方法名来访问方法，在类的内部，self.方法名来访问方法
    #self ===> 对象，访问方法、属性通过对象来操作

    #实例方法
    # def h(cls):
        # cls.__w()

    #@在python里被称为语法糖
    @classmethod #装饰器：讲一个实例方法变成类方法
    def hello(cls):
        print('这是一个类方法')

    @staticmethod #装饰器：将一个实例方法变成一个静态方法
    def python():
        print('这是一个静态方法')
"""
私有属性定义的目的
属性一旦被定义，不希望被更改

"""

print(thcher.ke)

#更改属性对象的值
thcher.ke = (1,2,3 )
print(thcher.ke)

#更改对象属性只能通过对象来修改它
t3 = thcher(1,2)
#更改之前的
print(t3.c)
t3.c = 'python'

# t3.h()
#对象.类方法名 ---> 访问类方法
t3.hello()
#
# thcher.hello()
# thcher.h()

"""
类方法：参数是cls
cls  self  都指向对象本身
cls作为参数的方法可以通过类名.方法名访问

"""

#私有的不能在外面用
# t3.__w()

#更改之后的
print(t3.c)

t4 = thcher('122',2)
print(t4.c)

#静态方法了可以通过类名.静态方法名、对象.静态方法名来访问
thcher.python()
t3.python()

# 类的外部，类，对象都不能访问类的私有属性
# print(teacher.__grade)


# 可以访问类的私有属性和公有属性【类的内部】
# t1 = thcher()
# t1.kl()

# t2 = thcher('hello' , 'python')
#私有的对象属性不能通过对象在类的外部访问
#print(t2.__b)
#对象可以访问对象的私有属性、对象的公有属性【在类的内部】
# t2.g()

#方法：静态、类方法、实例【普通方法】、魔法方法、私有方法
#def __方法名(self,参数):





