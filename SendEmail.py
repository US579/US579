from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import time




start = time.time()

for i in range(100):
    pass
end = time.time()
def sendEmail(start,end):
    host_server = u'smtp.163.com'
    sender_qq = u'us_579@163.com'
    pwd = u'123456a'
    sender_qq_mail = 'us_579@163.com'
    receiver = u'wzus579@gmail.com'
    mail_content = u'all test finish at {}, all test spend {}s '.format(time.asctime(time.localtime(time.time())),end-start)
    mail_title = u'US579'

    smtp = SMTP_SSL(host_server)
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()


sendEmail(start,end)
