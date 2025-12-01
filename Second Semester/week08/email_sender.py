import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USER = "your_email@gmail.com"         # 보내는 사람 이메일
SMTP_PASSWORD = "your_password"            # 앱 비밀번호 또는 SMTP 비밀번호


# CSV 파일 읽기
def load_mail_targets(csv_path: str):
    targets = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            targets.append({
                "name": row["이름"],
                "email": row["이메일"]
            })
    return targets


# HTML 메일 전송
def send_html_mail(to_email: str, subject: str, html_content: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    html_part = MIMEText(html_content, "html")
    msg.attach(html_part)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, to_email, msg.as_string())

    print(f"📨 Sent HTML mail to {to_email}")


# 전체에게 개별 전송
def send_bulk_mail(csv_path: str):
    targets = load_mail_targets(csv_path)

    for target in targets:
        name = target["name"]
        email = target["email"]

        # 개인화된 HTML
        html_message = f"""
        <html>
            <body>
                <h2>🚀 Dear {name},</h2>
                <p>This is <strong>Dr. Han</strong> reporting from Mars.</p>
                <p>I am alive, and continuing the mission.</p>
                <p>Thank you for supporting the rescue team.</p>
                <p>With warm regards from Mars 🪐</p>
            </body>
        </html>
        """

        send_html_mail(
            to_email=email,
            subject="Update from Mars – Dr. Han is alive!",
            html_content=html_message
        )
