import smtplib
from email.mime.text import MIMEText

# Every day is a good day.


user = "xx@qq.com"
auth_code = "xx"  # 授权码
to = "xx@163.com"

message = MIMEText("邮件正文内容demo，日日是好日！")   #  发送文本文件
message['Subject'] = "邮件主题"
message['From'] = user
message['To'] = to

server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.login(user, auth_code)
server.send_message(message)
server.quit()
print("邮件发送成功")
