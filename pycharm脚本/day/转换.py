#/usr/bin/python
#-*-coding:utf-8-*-

a = '1234567'
for i, v in enumerate(a):
    for j in range(0, 10):
        if v == str(j):
            print(a)