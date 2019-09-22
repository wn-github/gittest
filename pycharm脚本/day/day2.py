#!/usr/bin/python
#-*-coding:utf-8-*-
# a='Hello'
# b='python'
# print('a + b 输出结果：',a + b)
# print('a * 2 输出结果：',a * 2)
# print('a[1] 输出结果：',a[1])
# print('a[1:4] 输出结果：',a[1:4])
#
# if ("H" in a):
#     print("H 在变量 a 中")
# else:
#     print("H 不在变量 a 中")
#
# if ("M" not in a):
#     print("M 不在变量 a 中")
# else:
#     print("M 在变量 a 中")

# print('我叫 %s 今年 %d 岁!' % ('小明',10))



# a=int(input('账号:'))
# b=int(input('密码:'))
# if a==12345:
#     print()
#     if b==54321:
#         print('登陆成功')
#     else:
#         print('密码错误')
# else:
#     print('账号错误')




# python 的算术运算符
# +加  -减  *乘  /除  %求余  //求整[商]  **幂（次方）
# a=100
# b=20
# d='hello python'
#加
# c = a + b
# print(c)
#print(a + d) int和str不能进行算术运算
#减
# c = a - b
# print(c)
#乘
# c = a * b
# print(c)
#除
# c = a / b  #除的结果是浮点型
# print(c)
#求整[商的整数]
# c = a // b
# print(c)
#幂运算
# c = a ** b
# print(c)
#求余数
# s1 = 100
# s2 = 3
# f = s1 % s2
# print(f)
#pytho比较运算符（两个变量之间值得比较--->结果是布尔值）
'''
== 等于  > 大于 < 小于 >=大于等于 <= 小于等于 != 不等于
'''

#判断学生成绩所属的水平
'''
1.输入一个成绩
2.判断成绩属于：优秀[90-100]、良好[80-90]、一般[60-80]、不及格[60以下]

'''

# a=int(input('成绩:'))
# if    90<=a<=100:
#     print('优秀')
# elif  80<=a<90:
#     print('良好')
# elif  60<a<80:
#     print('一般')
# elif a>100:
#     print('输入值过大')
# elif a<0:
#     print('输入值过小')
# else:
#     print('不及格')



#python--->赋值运算符
'''
=  赋值  -=累加  +=累减  *=累乘  /=累除  %=累计求余  //=累计求整  **=累计求幂
'''
# a1=100
# a1+=1
# #a1=a1+1
# print(a1)
#
# a2=0
# for i in  range(1,10):
#     print()
#     a2+=i
#     print(a2)

#成员运算符   返回的是布尔值
'''
in  在...里面
not in  不在...里面
'''


#逻辑运算符
'''
and  与   两个条件同时为True，那么结果才为True
or   或   有一个条件为True，结果就是True
not  非   一个条件，True变为False，False变为True
'''

#数值0，空字符串，空列表，空元组，空集合，空字典   默认代表False
#None  空的  --->  函数里的返回值的一种

# if []:
#     print('hello')

#pytho  for 循环
'''
for i in  xx:
    代码语句
'''
#xx 代表的是可迭代的对象，i 变量  代表xx 里某一个具体的值

# str_1 = 'hello'
# for i in  str_1:
#     print(i)
# set_1 = {'1','2','3','4'}
# for i in  set_1:
#     print(i)
# dict_1 = {'name':'mark','sex':'man'}
# for i in  dict_1:
#     print(i)
#循环一个字典的时候，拿到的是键

# a=[1,1,1,2,4,4,5,5]
# b=[]
# for a in  a:
#     if a not in b:
#         b.append(a)
# print(b)

# for x in  range(1,10):
#     for y in  range(1,x+1):
#         print('{} * {}={}\t'.format(x,y,x*y) ,end="")
#     print() #默认换行

d = {
    "data": {
        "msg":
        [
            {
                "s_1": ["Jim", "男",  19, "175cm"],
                "country": "美国"
            },
            {
                "s_2": ["Kity", "女",  17, "165cm"],
                "country": "法国"
            },
            {
                "s_3": ["Tom", "男",  19, "173cm"],
                "country": "美国"
            },
            {
                "s_4": ["拖拉斯基", "男",  18, "180cm"],
                "country": "俄罗斯"
            },
            {
                "s_5": ["阿卡丽", "女",  17, "175cm"],
                "country": "乌克兰"
            },
            {
                "s_6": ["牙买稻子", "女",  18, "161cm"],
                "country": "日本"
            },
            {
                "s_7": ["龟田一郎", "男",  19, "175cm"],
                "country": "日本"
            },
            {
                "s_8": ["张三", "男",  20, "180cm"],
                "country": "中国"
            },
            {
                "s_9": ["李秀琴", "女",  19, "175cm"],
                "country": "中国"
            },
            {
                "s_10": ["宋仲基", "女",  19, "175cm"],
                "country": "韩国"
            },
            {
                "s_11": ["金正鞋", "男",  19, "168cm"],
                "country": "朝鲜"
            },
            {
                "s_12": ["卡列夫斯基", "男",  21, "190cm"],
                "country": "俄罗斯"
            },
        ]
    },
}
# print(d)

# 求国家个数
# 求所有学生的身高范围
# 求统计男女比例
# 求平均身高
# 查询身高在170到180之间的学生名字



# a = []
# b = []
# c = []
# for i in d["data"]["msg"][0:12]:
#     # print(i)
#     a.append(i)
# # print(a)
# for g in range(0,12):
#     # print(a[g]["country"])
#     f = a[g]["country"]
#     b.append(f)
# # print(b)
# for k in b :
#     if k not in c:
#         c.append(k)
# # print(c)
# print(len(c))

# country=[]
# name=[]
# sex=[]
# age=[]
# height=[]
# d1=d['data']['msg']
# for i in d1:
#     for j in  i.values():
#         if type(j) == list:
#             name.append(j[0])
#             sex.append(j[1])
#             age.append(j[2])
#             height.append(j[3])
#         else :
#             country.append(j)
# print(len(set(country)))
# print(name)
# print('男生个数为{}，女生个数为{}，男女比例为{}'.format(sex.count('男'),sex.count('女'),sex.count('男')/sex.count('女')))
#
# print('平均身高为{}'.format(sum(height)/len(height)))
# print('身高范围在{}和{}之间'.format(max(height),min(height)))

text = "Early in the day it was whispered that we should sail in a boat, only thou and I, and never a soul in the world would know of this our pilgrimage to no country and to no end"
# 1、将text中每个首字符大写的英文单词添加到一个列表中
# 2、将首字符小写的单词转换为首字符大写
# 3、将text中所有的包含a的字符替换成博文两个字
# 4、删除包含小t字符的单词后，组成一个新的字符串

# a=text.split( )
# b=[]
# print(a)
# for i in  a:
#     if a==a.title():
#         b.append(a)
# print(b)


# print(text.title())


# c=text.replace('a','博文')
#   print(c)

#     if 't' in i:
#          a.remove(i)
# print(a)
# d=','.join(a)
# print(d)


# s = input("输入：")
# rs = list(reversed(s))
# if list(s) == rs:
#     print(True)
# else:
#     print(False)

# a=[3,25,2,27,36,16]
# b=len(a)
# for i in range(b):#循环次数
#   for j in range(b-1):
#      if a[j] > a[j+1]:
#        a[j], a[j+1] = a[j+1], a[j]
# print(a)

# a=['a','a','1','2','3']
# b=a.count('b')
# print(b)

#选择排序
#100以内质数之和
#水仙花数
#任意阶乘之和


# a=[3,25,2,27,36,16]
# b=len(a)
# for i in range(b):#循环次数
#   for j in range(i+1,b):
#      if a[i] > a[j]:
#          a[i], a[j] = a[j], a[i]
# print(a)

#质数之和100以内
# a = 0
# for i in range(2,101):
#     # print(i)
#     for j in range(2,i+1):
#         # print(j)
#         if i % j == 0:
#             break
#     if i == j:
#         a=a+j
# print(a)



# a=[]
# for i in  range(10):
#     for j in  range(10):
#         for l in  range(10):
#             b1=(i*100+j*10+l)
#             b2=(i**3+j**3+l**3)
#             if b1 == b2:
#                 a.append(b2)
# for i in  a:
#     if i > 100:
#         print(i)

#
# a=int(input('请输入一个整数：'))
# b=1
# if a.isdigit():
#     if a<0:
#         print("负数没有阶乘")
#     elif a == 0:
#         print('零的阶乘是1')
#     else:
#         for i in range(1,a+1):
#             b = b*i
#         print('%d的阶乘为%d'%(a,b))

#
a=input('请输入一个正整数:')
b=0
c=1
for i in range(1,int(a)+1):
	c=c*i
	b=b+c
print(b)
# print(c)


