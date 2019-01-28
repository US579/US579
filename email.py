# -*- coding: utf-8 -*-
# !/usr/bin/env python
import smtplib, time
from email.mime.text import MIMEText

# 使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_host = "smtp.163.com"
# 用户名
mail_user = "us_579@163.com"
# 密码
mail_pass = "123456a"
# 邮箱的后缀，网易就是163.com
mail_postfix = "163.com"


def send_mail(to_list, sub, content):
    print 'aaaaaaaa'
    me = "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)  # 将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        # 连接服务器
        server.connect(mail_host)
        # 登录操作
        server.login(mail_user, mail_pass)
        print 'success'
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception:
        return False


'''
定时函数默认60秒
'''


def re_exe(inc=60):
    while True:
        if send_mail(['451823237@qq.com'], "大饼sasd", "大饼大饼我的大饼"):
            print "email sent!"
        else:
            print "failed!"
        time.sleep(inc)


if __name__ == '__main__':
    # 发送1封，上面的列表是几个人，这个就填几
    for i in range(1):
        # 输入定时时间
        re_exe(5)
