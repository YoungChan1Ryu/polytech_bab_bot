#!/usr/bin/env python
# coding: utf-8

# # polytech_bab_bot
# 강서폴리텍 홈페이지에서 식단 데이터를 불러와 구독자에게 텔레그램 메시지로 식단을 보내주는 코드입니다.
# 
# - 텔레그램 봇 아이디: @polytech_bab_bot
# - 만든이: 류영찬

# ### 라이브러리 불러오기

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import datetime
import requests
import os
from dotenv import load_dotenv


# ### 리눅스 서버용 크롬 드라이버 설정하기

# In[ ]:


chrome_options = Options()
# 서버라서 화면이 없으므로 headless 사용
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# ### 식단 불러오기

# In[ ]:


try:
    # 페이지 접속하고 기다리기
    url = "https://www.kopo.ac.kr/kangseo/content.do?menu=262"
    driver.get(url)
    time.sleep(5)

    # HTML 파싱하기
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # 클래스명이 menu인 테이블의 tbody에서 각 행을 저장
    rows = soup.select('table.menu tbody tr')

    # 오늘 날짜 정보
    today = datetime.datetime.now()
    todayWeekday = today.weekday() # 0은 월, ... 4는 금
    korWeekday = ["월", "화", "수", "목", "금", "토", "일"]
    todayKorWeekday = korWeekday[todayWeekday]
    formatted_date = today.strftime(f"%Y-%m-%d({todayKorWeekday})")

    # 오늘 요일에 해당하는 행 찾기
    target_row = rows[todayWeekday]
    cells = target_row.find_all('td')

    # cells[0]은 날짜, cells[1]은 조식, cells[2]는 중식, cells[3]은 석식
    lunchRaw = cells[2].get_text(strip = True)
    lunchList = lunchRaw.split("\n, ")

    result = formatted_date
    for menu in lunchList:
        result += "\n" + menu

except Exception as e:
    print(f"식단을 불러오는 중 에러 발생: {e}")

finally:
    # 메모리 확보를 위한 브라우저 종료
    driver.quit()


# ### 텔레그램 전송하기

# In[ ]:


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
subscriberListFile = "./subscriberList.txt"

def send_telegram(text):
    # 줄바꿈과 공백을 제거하고 파일을 읽어서 구독자 ID 리스트 생성
    with open(subscriberListFile, 'r') as f:
        chat_ids = [line.strip() for line in f if line.strip()]

    # 모든 구독자에게 순차 발송
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    success_count = 0
    fail_count = 0

    for chat_id in chat_ids:
        payload = {
            "chat_id": chat_id,
            "text": text
        }

        try:
            res = requests.post(url, json=payload)

            if res.status_code == 200:
                print(f"ID {chat_id}로 메시지 발송 성공")
                success_count += 1
            else:
                print(f"ID {chat_id}로 메시지 발송 실패({res.text})")
                fail_count += 1

            # 안정성을 위한 짧은 대기 시간
            time.sleep(0.05)

        except Exception as e:
            print(f"ID {chat_id}로 메시지 발송 중 에러 발생: {e}")
            fail_count += 1

    print(f"\n메시지 발송 완료(성공: {success_count}, 실패: {fail_count})")

send_telegram(result)

