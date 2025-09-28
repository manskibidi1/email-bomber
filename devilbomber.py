#  Python file for EMAIL SPAMMER:

```import smtplib
import time
from email.mime.text import MIMEText
from datetime import datetime

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "recipient_email@gmail.com"

email_count = 0
max_emails = 10

subjects = [
    "Auto Email: Update",
    "Python Bot Says Hi",
    "This was sent at {time}",
]

def send_email(count):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subject = subjects[count % len(subjects)].format(time=now)

    body = f"This is automatic email #{count + 1} sent at {now}."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"[+] Email #{count + 1} sent at {now}")

        with open("email_log.txt", "a") as log:
            log.write(f"[{now}] Email #{count + 1} sent to {TO_EMAIL}\n")

    except Exception as e:
        print(f"[!] Failed to send email #{count + 1}: {e}")

while email_count < max_emails:
    send_email(email_count)
    email_count += 1
    time.sleep(30)
```
