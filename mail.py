#!/usr/bin/python3
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user=""    #用户名
mail_pass="sdzinyfhizvjbiaa"   #口令 
 
 
sender = ''
receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Download finished.', 'plain', 'utf-8')
message['From'] = Header("youtube-dl", 'utf-8')
message['To'] =  Header("vps", 'utf-8')
 
subject = 'Download finished.'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 587)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("Mail sent success.")
except smtplib.SMTPException:
    print ("Error: Mail error.")
