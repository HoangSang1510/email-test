#tự động gửi email qua smtp (chưa test)
import smtplib
from email.message import EmailMessage
import json 

# đường dẫn đến file json của khách hàng trong thư mục output_email
with open("/content/drive/MyDrive/be_email/output_emails/0.json","r") as f:
  data = json.load(f)

msg = EmailMessage()
msg.set_content(data["body"])

msg['Subject'] = data["subject"]
msg['From'] = data["from"]
msg['To'] = data["to"]

# Gửi email qua SMTP server, tắt tùy chọn quyền truy cập của ứng dụng kém an toàn trong tài khoản gg trước
server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
server.login("your_email", "your_password")
server.send_message(msg)
server.quit()