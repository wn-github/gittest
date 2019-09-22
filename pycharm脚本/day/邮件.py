#/usr/bin/python
#-*-coding:utf-8-*-

# python smtplib email 作用:用于接收、发送邮件

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage


# 服务器端的信息
# mail_host = 'smtp.163.com'

# 邮件服务器端口号
# mail_port = 465

# 用户信息
# mail_user = 't075762@163.com'

# 用户授权码
# mail_pass = 'wn12345'


# 发送信息
# 邮件发送方的地址
# sender = 't075762@163.com'

# 邮件接收方的地址
# receivers = ['3202037092@qq.com']  # 可以写多个

# 邮件正文

# # 设置邮件主题
# subject = 'python测试邮件'

# # 设置邮件正文
# content = 'hello world!'
#
# # 三个参数：第一个参数为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
# #MIMEText()类
# message = MIMEText(content,'plain','utf-8')
#
# """
# Header()类，作用：对发送的邮件添加头部信息
# """
#
# # 发送邮件的过程
# # 第一步：添加发送者头部
# message['From'] = Header(sender)
# # 第二步：添加接受者头部
# message['To'] = Header(str('；'.join(receivers)))
# # 第三步：添加右键的主题
# message['Subject'] = Header(subject)
#
# # 连接邮件服务器并发送邮件
# # 第一步：登录邮箱
# s = smtplib.SMTP_SSL(host = mail_host, port = mail_port)
# # 第二步：输入账号密码
# s.login(mail_user,mail_pass)
# # 第三步：发送邮件
# s.sendmail(sender , receivers , message.as_string())
# print('success')
# # 第四步：退出登录
# s.close()

# 带有附件的邮件发送
# 添加一个MIMEMultipart类，将正文及附件添加到邮件里
message = MIMEMultipart()



# class Email(object):
#         mail_host = 'smtp.163.com'
#         mail_port = 465
#         mail_user = '13525038273@163.com'
#         mail_pass = 'wang12345'
#         sender = "13525038273@163.com"
#         receivers = ['3202037092@qq.com']
#         def xieyoujian(self) :
#                 self.subject = "2019.8.15日报"
#                 content = "学习python—邮箱发送"
#                 self.message = MIMEText(content, 'plain', 'utf-8')
#         def fasong(self):
#                 self.message['From'] = Header(self.sender)
#                 self.message['To'] = Header(str(";".join(self.receivers)))
#                 self.message['Subject'] = Header(self.subject)
#         def lianjie(self):
#                 s = smtplib.SMTP_SSL(host=self.mail_host, port=self.mail_port)
#                 s.login(self.mail_user, self.mail_pass)
#                 s.sendmail(self.sender,self. receivers,self.message.as_string())
#                 print('邮件发送成功')
#                 s.close()
# k = Email()
# k.xieyoujian()
# k.fasong()
# k.lianjie()


# python异常处理
"""
1.python 语法错误，缩进、缺少：class
2.代码逻辑上的问题
"""
#异常处理
"""
处理  python代码中可能出现的错误、异常
"""

#try ... except 最简单的异常处理
"""
try：
    代码块1
except:
    代码块2
try语句没有错误时，不执行except语句
try语句存在错误时，执行except语句
except 执行异常的类型：
"""

# a = 1 / 0
# print(a)
# try:
#     # a = 1/0
#     # print(a)
#     print(name)
# except(ZeroDivisionError,NameError):
#     print('try语句内存在错误')

# 下面还有很多代码
# print('hello')

# try ... except ... finally
# try 语句存在错误，except、finally语句都被执行
# try 语句不存在错误，finally语句也被执行

# try:
#     a = 1 / 0
# except:
#     print('try语句内有bug')
#
# finally:
#     print('finally语句被执行了')

# 当try语句存在错误，执行except，不执行else语句
# 当try语句不存在错误，执行else语句

# try:
#     a = 1 / 0
# except:
#     print('try语句内有bug')
# else:
#     print('else语句被执行了')












