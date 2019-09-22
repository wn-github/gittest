#/usr/bin/python
#-*-coding:utf-8-*-

import paramiko

# paramiko  用于远程连接linux系统、文件下载、上传

# 面向过程  ssh协议进行连接、可以执行linux里的命令
# 创造一个SSH客户端，
# client = paramiko.SSHClient()

# 信任远程linux主机   paramiko.AutoAddPolicy()自动添加信任密文
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 通过客户端连接远程linux主机
# client.connect(
#     hostname='192.168.10.95',
#     port=22,
#     username='root',
#     password='123456',
# )

# 执行linux命令
# exec_command(需要执行的命令):返回的结果是一个元组
# stdin 输入 : ls -al   stdout 输出  :输出的结果  stderr：错误信息
# stdin,stdout,stderr = client.exec_command('cat install.log')

# read（） 读取
# decod（） 把xxx编译成xxx
# print(stdout.read().decode())


# 文件下载、上传
# Transport()：  作用类似于ftp服务器   参数：包含ip地址、端口号的元组
# ftp = paramiko.Transport(('192.168.10.95',22))

# 连接与远程linux服务器的连接
# ftp.connect(username='root',password='123456')

# 创建一个类似于ftp的客户端
# sftp = paramiko.SFTPClient.from_transport(ftp)

# 下载远程文件  get（参数1，参数2）
# 参数1：代表远程文件   参数2：代表本地文件
# x1 = '/home/log.txt'
# x2 = r'E:\Projects\untitled\day\log.txt'
# sftp.get(x1,x2)

# 发送远程文件  get（参数1，参数2）
# 参数1：代表本地文件   参数2：代表远程文件
# x1 = r'E:\Projects\untitled\day\a.txt'
# x2 = '/home/a.txt'
# sftp.put(x1,x2)


"""
1.可以执行命令
2.可以下载、上传文件
3.不同的对象、ip、用户名和密码不一样的时候都可以使用
"""

class yuancheng(object):
    def menu(self):
        import paramiko
        # paramiko  用于远程连接linux系统、文件下载、上传

        # 面向过程  ssh协议进行连接、可以执行linux里的命令
        # 创造一个SSH客户端，
        client = paramiko.SSHClient()

        # 信任远程linux主机   paramiko.AutoAddPolicy()自动添加信任密文
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 通过客户端连接远程linux主机
        client.connect(
            hostname = input('ip地址:') ,
            port = 22 ,
            username = input('用户名：'),
            password = input('密码：'),
        )
    # def zhixing(self):
        # exec_command(需要执行的命令):返回的结果是一个元组
        # stdin 输入 : ls -al   stdout 输出  :输出的结果  stderr：错误信息
        stdin,stdout,stderr = client.exec_command(input('命令：'))

        # read（） 读取
        # decod（） 把xxx编译成xxx
        print(stdout.read().decode())

        # 文件下载、上传
        # Transport()：  作用类似于ftp服务器   参数：包含ip地址、端口号的元组
        ftp = paramiko.Transport(('192.168.10.95',22))

        # 连接与远程linux服务器的连接
        ftp.connect(username='root',password='123456')

        # 创建一个类似于ftp的客户端
        sftp = paramiko.SFTPClient.from_transport(ftp)

        # 下载远程文件  get（参数1，参数2）
        # 参数1：代表远程文件   参数2：代表本地文件
        print('下载')
        x1 = input('远程文件路径：')
        x2 = input('本地文件路径：')
        sftp.get(x1,x2)

        # 发送远程文件  get（参数1，参数2）
        # 参数1：代表本地文件   参数2：代表远程文件
        # print('上传')
        x1 = input(r'本地文件路径：')
        x2 = input('远程文件路径：')
        sftp.put(x1,x2)
manager = yuancheng()
manager.menu()






















































































