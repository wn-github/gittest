#/usr/bin/python
#-*-coding:utf-8-*-

def tqsj():
    with open(file=r'E:\新建文件夹\qq_pro\data\a.txt', mode='r', encoding='utf-8') as d:
        b = d.read()
        c = b.split(',')
    return c
#         print(c)
# tqsj()