#coding:UTF-8
"""
--------------------------------------
   File Name：  send_email
   Description :
   Author :    admin
   Date：     2018/9/13
   E-mail: 3227456102@qq.com
   adb_activity_package：adb shell dumpsys window w |findstr \/ |findstr name=
--------------------------------------
"""
__author__ = 'admin'

import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 定义发件人和收件人
mail_from = "xxxxxxx@xx.cn"
mail_password = "xxxxxxxx"
mail_to = ["xxxxxx@qq.com"]


def email_content():
    # 邮件主题
    message = MIMEMultipart()
    message['From'] = Header(u"xxxxx" + "<" + mail_from + ">", 'utf-8')
    message['To'] = ";".join(mail_to)
    message['Subject'] = Header(u"Appium 自动化测试报告", 'utf-8')
    # 邮件内容1
    emailContent1 = MIMEText('这是测试报告，详情请查看附件', 'plain', 'utf-8')
    message.attach(emailContent1)
    # 获取最新的html报告
    # result_dir = ".\\report"
    result_dir = os.path.join(os.getcwd(), 'report/')
    lists = os.listdir(result_dir)
    # lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not
    # os.path.isdir(result_dir + "\\" + fn) else 0)
    print("最新的文件为：" + lists[-1])
    file = os.path.join(result_dir, lists[-1])

    # 邮件内容2：report.html中内容
    emailContent2 = MIMEText(open(file, 'rb').read(), 'html', 'utf-8')
    message.attach(emailContent2)

    # 添加邮件附件
    enclosure1 = MIMEText(open(file, 'rb').read(), 'html', 'utf-8')
    enclosure1["Content-Type"] = 'application/octet-stream'
    enclosure1["Content-Disposition"] = 'attachment; filename=report.html'
    message.attach(enclosure1)
    return message


def sendreport():
    # 发送邮件
    try:
        smtp = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)
        smtp.login(mail_from, mail_password)
        message = email_content()
        smtp.sendmail(mail_from, mail_to, message.as_string())
        smtp.quit()
        print("email has send out!")
    except smtplib.SMTPException:
        print("email send error!")
