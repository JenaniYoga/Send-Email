import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "jelax585@gmail.com"
receiver_email = "yohajenany98@gmail.com"
password = "nvvztweqlpfubpgs"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"
body = "This is a test email sent from Python."
message.attach(MIMEText(body, "plain"))


with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()  
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")
