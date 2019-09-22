#/usr/bin/python
#-*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
mail_host='smtp.163.com'
mail_port = 465
mail_user='t075762@163.com'
mail_pass='wn12345'
sender ="t075762@163.com"
receivers=['18317822978@163.com']
subject = "2019.8.18"
message=MIMEMultipart()
message['From']=Header(sender)
message['To']=Header(str(";".join(receivers)))
message['Subject']=Header(subject)
with open(file='邮件.html',mode='r',encoding='utf-8')as f:
    content =f.read()
p1 = MIMEText(content, 'html', 'utf-8')
with open(file='a.txt',mode='r',encoding='utf-8')as f:
    d=f.read()
p2 = MIMEText(d, 'plain', 'utf-8')
p2['Content-Type']='application/octet-stream'
p2['Content-Disposition'] = 'attachment;filename="hello.txt"'
with open (file='0.jpg',mode='rb')as f:
    p3 = MIMEImage(f.read())
p3['Content-Type'] = 'application/octet-stream'
p3['Content-Disposition'] = 'attachment;filename="0.jpg"'
message.attach(p1)
message.attach(p2)
message.attach(p3)
s=smtplib.SMTP_SSL(host=mail_host,port=mail_port)
s.login(mail_user,mail_pass)
s.sendmail(sender,receivers,message.as_string())
print('邮件发送成功')
