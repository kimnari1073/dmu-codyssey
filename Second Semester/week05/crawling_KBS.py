# crawling_KBS.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# 1. 크롬 드라이버 자동 설치/실행
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

try:
    # 2. 네이버 메인 접속
    driver.get("https://www.naver.com")
    time.sleep(2)

    # 3. 로그인 버튼 클릭
    login_btn = driver.find_element(By.CSS_SELECTOR, "a.link_login")
    login_btn.click()
    time.sleep(2)

    # 4. ID / PW 입력
    user_id = os.environ.get("NAVER_ID") or "YOUR_ID"
    user_pw = os.environ.get("NAVER_PW") or "YOUR_PW"

    driver.find_element(By.ID, "id").send_keys(user_id)
    driver.find_element(By.ID, "pw").send_keys(user_pw)
    driver.find_element(By.ID, "log.login").click()
    time.sleep(3)

    # 5. 로그인 후 크롤링할 콘텐츠 예: 네이버페이 잔액
    #    개발자도구에서 선택자 확인 후 아래 selector 교체
    content_selector = ".my_pay_money"   # 예시
    elements = driver.find_elements(By.CSS_SELECTOR, content_selector)

    # 6. 내용 추출
    result_list = [el.text for el in elements]
    print("크롤링 결과:", result_list)

finally:
    driver.quit()
