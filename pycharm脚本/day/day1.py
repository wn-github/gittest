#/user/bin/python
#-*-coding:utf-8-*-
# 单行注释
# 多行注释
# 1)ctrl+?
# 2)单引号注释
'''
a=input('>>>')
print(a)
'''
# 3)双引号注释

"""
a = input('>>>')
print(a)
"""

# a='abcd'
# b=a.upper()
# #小写变大写
# print(b)
# print(b.lower())
# 大写变小写

# a='weining'
# b='wei'.title()+'ning'.title()
# print(b)
# 首字母大写

# a = 'AbCd'
# b = a.swapcase()
# print(b)
# print(b.swapcase())
# 数据反转，大写变小写，小写变大写

# a='151617'
# b=a.replace('1','q',2)
# print(b)
# 将字符串中的字符更改为其他数据：replace('内容','替换内容','替换数量')

# a='bigcbigc'
# b=a.split('c')
# print(b)
# b=a.split('c', 1 )
# print(b)
# 以括号中的数据为分隔符，将字符串分割成列表，split('分隔符')


# a='beginhead'
# b=a.startswith('begin')
# print(b)
# 判断字符串是否以括号中的元素开头，startswith('开头')

# a='beginhead'
# b=a.endswith('head')
# print(b)
# 判断字符串是否以括号中的元素结尾，endswith('结尾')

# a=['a,b,c,d']
# b=','.join(a)
# print(b)
# a='{} nihao {}'
# 以某个数据将列表连接起来形成新的字符串：分隔符.join(元素序列)两个字符串中间加一个数据

# a='hello  {}'
# c=a.format('bye')
# print(c)
# 格式化字符串{}占位 a.format(b),对字段的显示进行格式化

# a='i'
# b='%s love you' %(a)
# print(b)
# %占位:%s能填充所有，%d填充数字

# a='  abcc '
# print(a)
# b=a.strip()
# print(b)
# 去除字符串左右的空格strip(),lstrip()去除左边的空格，rstrip()去除右边的空格

# 元组
# a=('123','nihao','hello',1341,(12,'sdfg'))
# type(数据)，查看数据类型
#print（type(a)）
# print(a[4])

# a=(12,12,23,12,34)
# b=a.count(12)
# print(b)
# 统计括号中的数据在元组中有多少个：count(数据)

# a=(12,13,14,12)
# b=a.index(12)
# print(b)
# c=a.index(12,2)
# print(c)
# 查询括号中的数据在元组中的下标位置：index（数据），如果有重复元素，默认显示匹配的第一个元素，找不到报错
# rindex（） 从右往左


# a=['123','122','121']
# print(type(a))
# a.append('56')
# print(a)
# 添加数据，默认添加在列表的最后，一次只能添加一个数据

# a=[11,12,13]
# a.insert(3,14)
# print(a)
# 添加在指定位置，第一个是下标号，第二是要添加的数据：insert（x，数据）

# a=[12,23,12,34,12]
# a.remove(12)
# print(a)
# a.remove(12)
# print(a)
# 删除括号中的数据，如果有重复的元素，默认删除匹配的第一个元素

# a=[12,23,12,2,1]
# a.pop(1)
# print(a)
# 根据下标位置删除数据：pop（下标位置）

# a=[123,12,89,67]
# a.sort()
# print(a)
# a.reverse()
# print(a)
# 排序，同一个数据类型:sort
# 数据反转：reverse，如果再执行一次，数据会再次反转回来

# a=[12,1,54,3]
# # b=['qwe','asdf']
# # a.extend(b)
# # print(a)
# # 将b列表中的数据更新到a列表：a.extend(b)

# a=[12,23,34,12]
# b=a.count(12)
# print(b)
# 统计括号中原宿在列表中有多少个：count（元素）

# a=[12,24,23,35]
# b=a.index(23)
# print(b)
# 查询括号中的元素在列表中的下标位置：index（元素）

# a=[123,321,231,213]
# a.clear()
# print(a)
# b=('asdfg',)
# 如果元组里面只有一个元素的话，后面要加逗号才是元组
# print(type(b))
# c=[123]
# print(type(c))
# 清空列表

# a=[12,23,34]
# b=a.copy()
# print(b)
# 复制列表,复制分为两种，浅复制和深复制
# 浅复制：只复制外面一层，没有复制里面一层
# a=['123',['qwer'],'2345']
# b=a.copy()
# a[2].append(13)
# print(a)
# print(b)
# 深复制：全部复制
# import copy
# a=['123',['qwer'],'2345']
# c=copy.deepcopy(a)
# a[1].append(67)
# print(a)
# print(c)

# a={'qwer','asdf','123','321','123'}
# print(a)
# a.add(12)
# print(a)
# 添加数据，只能添加一个数据：add（数据）

# a={'qwer','asdf','123','321'}
# a.remove('123')
# print(a)
# a.pop()
# print(a)
# 删除数据:remove   随即删除：pop

# a={'name':'mark', 'sex' :'man'}
# print(a.keys())
# 获取所有的键

# a={'name':'mark', 'sex' :'man'}
# print(a.values())
# 获取所有的值

# a={'name':'mark', 'sex' :'man'}
# print(a.items())
# 获取所有的键值对

# a={'name':'mark', 'sex' :'man'}
# a['age']='12'
# print(a)
# 添加键值/更改数据(没有数据就添加，有就更改)

# a={'name':'mark', 'sex' :'man','age':'20'}
# a.pop('sex')
# print(a)
# 删除数据

# a={'name':'mark', 'sex' :'man','age':'20'}
# a.popitem()
# print(a)
# 默认删除最后一个

# a={'name':'mark', 'sex' :'man','age':'20'}
# b={'say':'hello'}
# a.update(b)
# print(a)
# 更新数据，将字典b中的数据更新到字典a（必须是同一数据类型）

# 命名一个空集合的方式
# a=set()
# print(type(a))
# a.add('123')
# print(a)
# 命名一个大括号时，默认是字典的数据类型

# a=['12','23','34','12','34']
# b=set(a)
# print(b)
# 去重

# a={'12345','123','qwer'}
# b=len(a)
# print(b)
# 统计元素个数：len(元组，字符串，集合)

# print(type(123))
# print(type(True))
# 查看数据类型：type（变量和数据）

# a=hex(192)
# print(a)
# a=oct(192)
# print(a)
# a=bin(192)
# print(a)
# a=int(0b11000000)
# print(a)
# 将十进制转换为十六进制：hex（）
# 将十进制转换为八进制：oct（）
# 将十进制转换为二进制：bin（）
# 将任何进制转换为十进制：int（）

# a=ord('a')
# print(a)
# a=chr(97)
# print(a)
# 将数字转换为ascll表中的字符：chr（）
# 将ascll表中的字符转换为数字：ord（）

# a=sum((12,23,34,45))
# print(a)
# 数字求和：sum（1，2，3，4）

# a,b=divmod(14,3)
# print(a)
# print(b)
# 整数求余，a是整除的结果，b是求余的结果

# find():查找字符串中的子字符串，如果找到，返回子字符串的第一个字符的索引值，找不到返回-1
# print("hello".find('e'))
# rfind():从右往左查询

# max（）：求字符串中的最大值，返回asscii码最大值对应的字符
# print(max('hello'))
# min（）：求字符串中的最小值，返回asscii码最大值对应的字符

# 格式化
# x="Tom 猫"
# print(f"你好{x}")

# isdigit()判断字符串的字符全部是数字，是的话返回True，不是返回False
# s='123a'
# print(s.isdigit())

# istitle()判断字符串是否为标题（首字符大写），如果是的话返回True，不是返回False
# s='hello World'
# print(s.istitle())

# isupper()判断字符串中的字母全是大写，是的话返回True，不是返回False
# islower()判断字符串中的字母全是小写，是的话返回True，不是返回False

# isalnum()判断字符串中的字符由数字或字母组成，是的话返回True，不是返回False
# a='123abc'
# print(a.isalnum())

# \t  相当于tab  横向制表符
# isalpha()判断字符串中的字符全是字母，是的话返回True，不是返回False
# a='123abc'
# print(a.isalpha())

# isspace()判断字符串中只包含空白字符，是的话返回True，不是返回False
# 空白字符包括：空格、\n、\t、\r、回车
# a=' '
# print(a.isspace())

# isdecimal()判断字符串中是否只包含十进制的数字，是的话返回True，不是返回False

# 反转
# s='hello'
# print(s[::-1])

# 更新
# a=['123','qwe']
# b=('asd','321')
# a.extend(b)
# print(a)

# 查找
# a=['1','2','3','4','5']
# print(a.index('1'))

# insert:添加（根据索引值）
# a=['1','2','3','4','5']
# a.insert(4,'123')
# print(a)

# pop：删除（根据索引值）,不写索引值默认删除最后一个
# a=['1','2','3','4','5']
# print(a.pop(3))
# print(a)

# remove：删除（指定删除的元素），不存在就报错
# a=['1','2','3','4','5']
# a.remove('1')
# print(a)

# reverse：反转
# a=['1','2','3','4','5']
# a.reverse()
# print(a)

# sort:排序（根据asscii码），默认升序
# reverse=True 降序
# a=[11,32,13,4,75]
# a.sort(reverse=True
#        )
# print(a)

# clear：清空
# a=['1','2','3','4','5']
# a.clear()
# print(a)

# copy:复制
# a=['1','2','3','4','5']
# b=a.copy()
# print(b)
# a[0]='123'
# b=a.copy()
# print(b)

# list：转换成列表
# a={'12q','qwe','321'}
# b=list(a)
# print(b)

# 生成编号
# a=['1','2','3','4','5']
# for x,y in enumerate(a):
#     print(x)
#     print(y)

# #商品  购买数量10
# a=["香蕉","菠萝","提子","芒果"]
# #单价
# b=[7,8,6,10]
# #超市结账的
# member = {'1001':'2001','1002':'2002'}
#
# """
# 1.根据每个商品的编号，选择商品
# 2.购买数量
# 3.结账的时候，会员结账优惠95折，非会员全额付款
# """
#
# print("商品编号\t\t\t商品名\t\t\t价格")
# for x,y in  enumerate(a):
#     print("\t{}\t\t\t{}\t\t\t\t{}".format(x,y,b[x]))
# while 1:
#
#     d=input('购买输入Y，退出输入Q')
#     if d == 'Y':
#         bianhao=int(input('购买商品编号:'))
#         num=int(input('输入购买数量：'))
#         zhangdan=b[bianhao] * num
#         print(f'您购买的商品名是{a[bianhao]},购买数量{num},消费金额{zhangdan}')
#         mem = input("您是不是会员（Y是会员，N不是会员）：")
#         if mem == 'Y':
#             huiyuan=input('会员卡卡号：')
#             if huiyuan in member.keys():
#                 ps = input('会员卡密码:')
#                 if ps == member[huiyuan]:
#                     zhangdan *=0.95
#                     print("您要支付{}".format(zhangdan))
#                 else:
#                     print('请重新确认')
#         else:
#             print('您不是会员')
#             print("您要支付{}".format(zhangdan))
#
#     elif d == 'Q':
#         print('欢迎下次再来！')
#         break
#     else:
#         print('输入错误，请重新输入！')



# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if (x!=y) and (y!=z) and (z!=x):
#                 print("%d %d %d" % (x, y, z))

# discard（指定删除的元素）
# a1={1,2,3,4,5,6,7,8}
# a2={1,2,3,4,5}
# difference（'集合B'）：求集合B相对于集合A的差集
# print(a1.difference(a2))

# difference_update（'集合B'）：删除集合中相同的元素，操作是在集合A上执行的
# a1.difference_update(a2)
# print(a1)

# intersection（'集合B'）：求集合A，B的交集，没有交集返回空集
# print(a1.intersection(a2))

# intersection_update（'集合B'）：删除不是交集的部分，返回删除后的集合A
# a1.intersection_update(a2)
# print(a1)

# isdisjoint（'集合B'）:判断集合A，B是否存在交集，不存在返回True，存在返回False
# print(a1.isdisjoint(a2))

# issubset('集合B')：判断集合B是否是集合A的子集，是返回True，不是返回False
# print(a2.issubset(a1))

# issupperset


# symmetric_difference():找出两个集合中不相同的元素集合，返回一个新集合
# print(a1.symmetric_difference(a2))

# symmetric_difference_update('集合B')：对集合A操作，先清空集合A,在将集合A、B不同的元素放入集合A
# a1.symmetric_difference_update(a2)
# print(a1)

# union（'集合B'）：求集合A、B的并集，返回一个新集合、重复的元素只出现一次
# print(a1.union(a2))

# 导入随机数库（内置库）
# import random
# a=random.randint(1,99)
# print(a)
#
# c=[]
# for i in range(10):
#     c.append(i)
# print(c)

# 列表推导式
# print([i for i in range(10)])

"""
1.先写一个空列表[]
2.写一个变量
3.写循环
4.有条件写入条件
"""

# 100以内的偶数
# print([j for j in range(100) if  (j % 2 == 0)])

# 一张纸，厚度0.08mm，珠穆朗玛峰高8848m，求折叠多少次能超过珠穆朗玛峰，假设纸无限长
# n=0.00008
# m=1
# while n <= 8848:
#     n += n * 2 ** x
#     x += 1
#     print(x)

a = ["ads", "dafdsa", " jjajs", "dfdsdas"]
p = ["fdsfd", "fdsfdsaffdsa", "", "jjja", '213232']

"""
账号长度在6～8之间为合法的账号
密码的长度在5～7之间为合法的密码
账号和密码都符合上述要求，将账号密码以键值对的形式保存
"""

# 字典
# 1.以键值对的形式保存数据
# 2.键必须是唯一的，键不可以被更改，不可变的包含字符串，元组，数值
# 3.值可以是一个或者多个
# 4.值可以是数据类型，字符串类型，元组类型，集合类型，列表类型，字典类型

# 定义字典的格式
# 1.使用英文的{}包裹元素
# 2.key[键]：value[值]每个字典元素之间是用英文的逗号分隔

# 向子典内添加元素
# 第一种方法，传入一个键，再给键赋值
# 当字典中的键存在，再对键赋值的时候，会更改原来的键对应的值
# 获取字典中键对应的值，通过键取值
# 字典的方法
# get（'字典键'）：获取字典中键对应的值，一次只能传入一个值
# keys（）：获取字典中所有的键，用于循环
# values（）：获取字典中所有的值，用于循环
# clear（）：清空字典中所有的元素，还剩一个空字典
# copy（）：复制字典
# pop（‘要删除的键’）：删除字典中给定键值，返回的是键对应的值，如果删除的键不存在就会报错
# popitem（）：默认删除字典最后一个键值对
# len（）：求字典的键值对个数
# fromkeys（seq，values）：新建字典，设置默认值 seq：传入一个有序的对象，列表，元组字符串
# values：设置字典键对应的值，可以不写，None代表空
# s='abc'
# v=[1,2,3]
# d=dict.fromkeys(s,v)
# print(d)
# items():将字典中的键值对转换为元组，可以被循环【for】使用
# d={
#     'key1':1000,
#     'key2':['我是列表'],
#     'key3':{1 : 2000 , 3 : ['a','b','c']}
# }
# for i,j  in d.items():
#     print(i)
#     print(j)

# update('需要添加字典的变量名'):将多个字典组合成一个字典
# 将B字典中的元素添加到A字典
# d1={1:'hello','a':'字典1'}
# d2={2:'world','b':'字典2'}
# d1.update(d2)
# print(d1)

# setdefault(键，默认值）：向字典中添加键值对，并设置默认值
# key：需要新增的字典键
# 默认值：符合基本数据类型的都行，还可以不写，不写默认None
# k={1:100,2:2000}
# 添加不存在的key，设置默认值
# k.setdefault('key1')
# print(k)
# 设置的key已经存在，不更改键值对
# k.setdefault('key1')
# print(k)

# 当直接使用for循环的时候，输出的是字典的键
# for i in k:
#     print(i)
# print(list(k))
# print(str(k))
