#/usr/bin/python
#-*-coding:utf-8-*-

# os:内置模块 ,作用：python与计算机系统进行交互
import os

# 获取当前目录的路径
# print(os.getcwd())

# chdir（路径的名字） 切换目录/路径   报错，前面加小r
# os.chdir(r'E:\Projects\untitled\day')
# print(os.getcwd())

# .    当前目录 == os.curdir
# print(os.curdir)

# ..  上一级目录  ==  os.pardir
# print(os.pardir)

# os.chdir('..')
# print(os.getcwd())
#
# os.chdir(os.pardir)
# print(os.getcwd())

# os.name ：获取操作系统的类型  Windows，Mac，Unix，Linux
# print(os.name)

# 创建多级目录 ：os.makedirs('多级目录')  a/b/c/d
# os.makedirs('day/b/c')

# 创建一个目录：os.mkdir('目录名')
# os.mkdir('444')

# 删除多个目录：（目录必须是空的） os.removedirs('目录名')
# os.removedirs('day/b/c')

# 删除单个目录：（目录必须是空的） os.rmdir('目录名')
# os.rmdir('444')

# 查看当前路径下所有的文件、目录  os.listdir('路径名')   ---->  返回的是一个列表
# a = os.listdir(r'E:\Projects\untitled\day')
# print(a)

# 对文件、目录重命名  os.rename（'老名字','新名字'）
# os.rename(r'E:\Projects\untitled\day\a.txt',r'E:\Projects\untitled\day\abc.txt')

# 删除文件：os.remove('绝对路径')
# os.remove(r'E:\Projects\untitled\day\b.txt')

# 执行系统命令：os.popen ('需要执行的命令')
# b = os.popen('dir')
# print(b.read)



# os.path 类  对文件的操作  返回文件的路径、例如绝对路径、相对路径、判断文件、目录

# 1.返回文件的绝对路径
# abspath('文件名')

# c = os.path.abspath('qqq.py')
# print(c)

# 返回上一级路径 dirname('路径')  /a/b/c/d.txt  ---->  /a/b/c
# d = os.path.dirname(r'E:\Projects\untitled\day\qqq.py')
# print(d)

# 返回当前文件/目录名 basename（'路径'）
# e = os.path.basename(r'E:\Projects\untitled\day')
# print(e)

# 判断文件/目录是否存在  ---->   True  False  exists('路径')
# f = os.path.exists('qqq.py')
# print(f)

# 判断是否是目录  ---->  True  False  isdir('路径')
# g = os.path.isdir(r'E:\Projects\untitled\day')
# print(g)

# 判断是否是文件  ---->  True  False  isfile('路径')
# h = os.path.isfile(r'E:\Projects\untitled\day')
# print(h)

# 判断是否是链接文件  ---->  True  False  islink('路径')
# j = os.path.islink(r'E:\Projects\untitled\day')
# print(j)

# 路径拼接  join（'路径1','路径2'）  A  B  ---->  /A/B
# a = '_'
# b = '123'
# print(a.join(b))

# print(os.path.join('/A/','B'))


# 路径分离:将最后一个文件或目录分离  split（'路径名'）
# k = os.path.split(r'E:\Projects\untitled\day')
# print(k)

# 分割文件的后缀名   ---->  返回一个元组  splitext（'文件名'）
# l = os.path.splitext('qqq.py')
# print(l)



# 统计顶级目录下有多少个目录，文件的个数

A = []
a = os.listdir(r'E:\Projects\untitled')
for i in a:
    A.append(i)

b = os.listdir(r'E:\Projects\untitled\day')
for i in b:
    if os.path.isdir(i) == False:
        A.append(i)

c = os.listdir(r'E:\Projects\untitled\Tuesday')
for i in c:
    if os.path.isdir(i) == False:
        A.append(i)
d = os.listdir(r'E:\Projects\untitled\.idea')
for i in d:
    if os.path.isdir(i) == False:
        A.append(i)
print(A)
print(len(A))






