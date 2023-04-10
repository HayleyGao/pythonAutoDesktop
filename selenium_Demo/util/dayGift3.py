import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 发送带附件的邮件

# Every day is a good day.

user = "xx@qq.com"
auth_code = "xx"  # 授权码
to = "xx@163.com"


mail_message = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Email_Demo</title>
    <h1>Every day is a good day!</h1>
</head>
<body>

<p>Enjoy your everyday!</p>

<a href="https://baike.baidu.com/item/%E6%97%A5%E6%97%A5%E6%98%AF%E5%A5%BD%E6%97%A5/20106462?fr=aladdin">日日是好日，时时是好时。</a>


</body>
</html>

"""
message = MIMEMultipart()  # 发送带附件的邮件的实例对象
message.attach(MIMEText(mail_message, 'html', 'utf-8'))
attachment1 = MIMEText(open("pic01.jpg", 'rb').read(), 'base64', 'utf-8')
attachment1['Content-Type'] = "application/octet-stream"
attachment1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', 'pic0001.jpg'))
message.attach(attachment1)

message['Subject'] = "邮件主题"
message['From'] = user
message['To'] = to

server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.login(user, auth_code)
server.send_message(message)
server.quit()
print("邮件发送成功")
