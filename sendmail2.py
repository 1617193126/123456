import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'LGY593913038@126.com'
msg['to'] = '5593913038@qq.com'
msg['subject'] = '网易新闻'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com', '25')
smtp.login('LGY593913038@126.com', 'LGY593913038')
smtp.sendmail('LGY593913038@126.com', '593913038@qq.com', str(msg))
smtp.quit()