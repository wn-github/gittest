#/usr/bin/python
#-*-coding:utf-8-*-


import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    hostname = input('127.0.0.1') ,
    port = 22 ,
    username = input('root'),
    password = input('123456'),
        )
