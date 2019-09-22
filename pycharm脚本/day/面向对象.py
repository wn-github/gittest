#/usr/bin/python
#-*-coding:utf-8-*-



# 使用面向对象的思想编写一段代码

# 创建一个狗类，将狗的行为定义成方法，狗的行为有吃、喝、跑、叫;
# 将狗的特征定义成属性，
# 狗的特征有毛色、品种、几条腿、狗的身高、体重
# 定义方法输出狗的特征(可以是一个或多个)
# 思考:狗的几条腿是定义成类属性合适还是对象属性合适?
# 要求:
# 1、定义类
# 2、定义属性[类属性、对象属性]
# 3、定义方法
# 4、不同的对象对应不同的狗。
# 例如:藏獒作为狗对象:4条腿、灰色、140cm、50kg、遇到生人会叫、饿了会吃、渴了会喝水、挨打会跑作为狗对象

# class   dog(object):
#
#     def __init__(self,maose,pinzhong,shengao,tizhong,jiao,chi,he,pao):
#         self.maose = maose
#         self.pinzhong = pinzhong
#         self.shengao = shengao
#         self.tizhong = tizhong
#         self.jiao = jiao
#         self.chi = chi
#         self.he = he
#         self.pao = pao
#
#     def print_pinzhong(self):
#         print(f'狗的品种是：{self.pinzhong}')
#     def print_maose(self):
#         print(f'狗的毛色是：{self.maose}')
#     def print_shengao(self):
#         print(f'狗的身高是：{self.shengao}cm')
#     def print_tizhong(self):
#         print(f'狗的体重是：{self.tizhong}kg')
#     def print_jiao(self):
#         if self.jiao:
#             print("遇见生人会叫，这狗不傻")
#         else:
#             print("遇见生人不会叫，这是个傻狗")
#     def print_chi(self):
#         if self.chi:
#             print("饿了会吃，这狗不傻")
#         else:
#             print("饿了不会吃，这是个傻狗")
#
#     def print_he(self):
#         if self.he:
#             print("渴了会喝水，这狗不傻")
#         else:
#             print("渴了不会喝水，这是个傻狗")
#
#     def print_pao(self):
#         if self.pao:
#             print("这狗不傻知道挨打就跑")
#         else:
#             print("这狗傻挨打不知道跑")
#
#
# a = dog('藏獒','灰色','140','50',True,True,False,False)
# a.print_pinzhong()
# a.print_maose()
# a.print_shengao()
# a.print_tizhong()
# a.print_jiao()
# a.print_chi()
# a.print_he()
# a.print_pao()



# 面向对象三个特点
"""
1.封装
封装指的是：对对数据和代码逻辑的处理

2.继承
单继承：B类继承A类
多继承：B类继承A类，C类
3.多态

"""

# 定义一个A类
class A(object):
    #类属性
    name = 'abc'
    age = 18

    def __init__(self,a):
        #对象属性
        self.a = a

    #实例方法
    def b(self):
        print('这是A类的实例方法b')

# 定义一个B类
class B(A):
    pass
    def c(self):
        print(f'父类的类属性有name：{self.name}，age：{self.age}')
        #在B类里直接使用A类的方法
        self.b()


# 子类拥有父类的全部属性以及方法
# 创建一个对象
b = B('wwww')
# 子类能否使用父类的属性、方法
print(b.name)
print(b.a)
b.c()











