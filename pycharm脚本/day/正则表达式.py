#/usr/bin/python
#-*-coding:utf-8-*-

# python   正则表达式   re  正则模块   （表达式只能操作字符串）
import re

"""
1.  .  在python里表示出了换行符\n以外任意一个字符
2.  *  在python里表示匹配*前面的字符0次或多次
3.  +  在python里表示匹配+前面的字符一次或多次
4.  ？ 在python里表示匹配？前面一个字符0次或1次  
5.  $  以某个字符结尾
6.  ^  以某个字符开头
7.  {m}  匹配{}前面的字符m次
8.  {m，n} 匹配{}前面的字符最少m次，最多n次
9.  [abc]  匹配[]里的任意一个字符
"""

# s = '11111123456'

# search(参数1，参数2)： 搜索
"""
参数1：已经编译好的正则表达式
参数2：要匹配的字符串
"""
# 写正则表达式的步骤
# 第一步：编译正则表达式  re.compile(r'.')这个是编译的过程，r1代表编译完成的正则表达式
# r1 = re.compile(r'.')
# r2 = re.compile(r'2+')
# r3 = re.compile(r'1*')
# r4 = re.compile(r'1?')
# r5 = re.compile(r'6$')
# r6 = re.compile(r'^1')
# r7 = re.compile(r'1{3}')
# r8 = re.compile(r'1{3,5}')
# r9 = re.compile(r'1[246]')

# 第二步：执行正则表达式

# a = re.search(r1,s)
# print(a)
# b = re.search(r2,s)
# print(b)
# c = re.search(r3,s)
# print(c)
# d = re.search(r4,s)
# print(d)
# e = re.search(r5,s)
# print(e)
# f = re.search(r6,s)
# # print(f)
# g = re.search(r7,s)
# print(g)
# h = re.search(r8,s)
# print(h)
# j = re.search(r9,s)
# print(j)
# re.findall()


# d = '13123137052125612131'
#
# q1 = re.compile(r'(^1[0-9]{10})*')
# k = re.search(q1,d)
# print(k)

# matcah与search的区别
"""
match : 一旦匹配不到立刻结束
search：匹配不到，继续匹配，直到匹配成功第一次或字符串结束为止
如果继续存在符合的字符串不输出
共同点：
匹配成功第一次之后停止
"""
# \d [0-9]
# \D 除了0-9以外的任意一个字符
# \s 表示空白字符 Unicode编码：\t \n \r \f \v
# \S 表示除了空白字符以外任意一个字符


#贪婪模式
"""
指的是尽可能的匹配更多的字符
"""


#非贪婪模式
"""
指的是匹配到符合规则的，就停止匹配
"""


# sub(参数1，参数2，参数3) 替换的意思  str.replace('旧的','新的')
"""
参数1：正则
参数2：新的字符
参数3：被更改的字符串

"""
# group（）组  作用是将我们匹配到的内容拿出来
# groups （） 多个分组


# URL = 'https://www.baidu.com'
# q2 = re.compile(r'\.(.*)\.')
# l = re.search(q2,URL).group()
# print(l)
# m = re.sub(r'\.','',l)
# print(m)


# URL = 'https://www.baidu.comhttps://www.jd.com'
# q3 = re.compile(r'\.(.*?)\.')
# n = re.search(q3,URL).group()
# print(n)
# o = re.sub(r'\.','',n)
# print(o)


#findall() ---->  结果是列表，每个元素都是字符串
#作用：找出字符串中所有符合正则规则的结果
URL = 'https://www.baidu.comhttps://www.jd.com'
q4 = re.compile(r'\.(.*?)\.')
p = re.findall(q4,URL)
print(p)



























