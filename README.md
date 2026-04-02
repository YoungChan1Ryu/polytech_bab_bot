# polytech_bab_bot

한국폴리텍대학 서울강서캠퍼스의 식단 정보를 자동으로 수집하여 매일 구독자에게 메시지를 발송하는 텔레그램 봇입니다.

## 📂 프로젝트 구조

```text
.
├── main.py              # 메인 식단 알림 로직 실행 파일
├── collector.py         # 사용자 ID 및 상태 수집기
├── scripts/             # 실행용 쉘 스크립트 (.sh)
├── notebooks/           # 개발 및 테스트용 Jupyter Notebooks
├── venv/                # 파이썬 가상환경
├── .env                 # 환경 변수 (API 토큰 등 - 보안 주의)
└── requirements.txt     # 프로젝트 의존성 패키지 목록
```

## 🛠️ 설치 및 설정 방법
1. 저장소 복제 및 이동
```bash
git clone https://github.com/YoungChan1Ryu/polytech_bab_bot
cd polytech_bab_bot
```
2. 가상환경 생성 및 패키지 설치
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. 환경 변수 설정
프로젝트 루트에 .env 파일을 생성하고 필요한 정보를 입력합니다.
```bash
TELEGRAM_TOKEN=your_bot_token_here
필요한 기타 환경 변수들...
```

## 🏃 실행 방법
메인 봇 실행
```bash
./scripts/run_bot.sh
```
ID 수집기 실행
```bash
./scripts/run_collector.sh
```
## 🚀 자동화 설정 (Cron)
이 봇은 cron을 통해 주기적으로 실행됩니다. 아래 예시를 참고하여 crontab -e에 설정을 추가하여 자동화하세요.

```bash
# 주중 오전 11시 30분(서버 시간 기준 오전 2시 30분)에 메시지 발송
30 2 * * 1-5 /home/username/project/scripts/run_bot.sh >> /home/username/project/bot.log 2>&1

# 매 5분마다 ID 수집기 실행 여부 확인 및 미실행시 재실행
*/5 * * * * /home/username/project/scripts/run_collector.sh

# 서버가 켜질 때 ID 수집기 자동 시작
@reboot nohup /home/username/project/venv/bin/python3 /home/username/project/collector.py &
```
> **Note:** /home/username/project 부분은 실제 설치된 경로에 맞게 수정하여야 합니다.
