#/usr/bin/python
#-*-coding:utf-8-*-

for i in range(10):
    for j in  range(1,i+1):
        print('{}x{}={}\t'.format(j, i, i * j), end='')
    print()