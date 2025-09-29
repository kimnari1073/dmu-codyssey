# sendmail.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# ====== 1. 계정 설정 ======
SENDER_EMAIL = "your_gmail@gmail.com"
RECEIVER_EMAIL = "receiver@example.com"
APP_PASSWORD = "your_16_char_app_password"   # 발급받은 앱 비밀번호

# ====== 2. 메일 내용 구성 ======
subject = "테스트 메일"
body = "안녕하세요. 파이썬에서 보내는 SMTP 테스트 메일입니다."

msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg['Subject'] = Header(subject, 'utf-8')
msg.attach(MIMEText(body, 'plain', 'utf-8'))

# ====== 3. SMTP 전송 ======
try:
    # Gmail TLS 포트 587
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()          # 서버와 인사
        server.starttls()      # TLS 보안 시작
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
    print("메일 전송 완료!")

except smtplib.SMTPAuthenticationError:
    print("인증 실패: 앱 비밀번호 또는 계정 설정을 확인하세요.")
except smtplib.SMTPConnectError:
    print("서버 접속 실패: 네트워크를 확인하세요.")
except Exception as e:
    print(f"기타 오류 발생: {e}")
