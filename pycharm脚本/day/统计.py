#/usr/bin/python
#-*-coding:utf-8-*-
f=open(file='a.txt',mode='r',encoding='utf-8')
b=f.readlines()
b1=[]
for i in b:
    c=i.replace('\n','')
    if len(c) !=0 and c[0] !='#':
        b1.append(c)
print(len(b1))
