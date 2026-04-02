## 자동화 설정
이 봇은 `cron`을 통해 주기적으로 실행됩니다. 아래 예시를 참고하여  `crontab -e`에 설정을 추가하여 자동화하세요.

```bash
# 주중 오전 11시 30분(서버 시간 기준 오전 2시 30분)에 메시지 발송
30 2 * * 1-5 /home/username/project/scripts/run_bot.sh >> /home/username/project/bot.log 2>&1

# 매 5분마다 ID 수집기 실행 여부 확인 및 미실행시 재실행
*/5 * * * * /home/username/project/scripts/run_collector.sh

# 서버가 켜질 때 ID 수집기 자동 시작
@reboot nohup /home/username/project/venv/bin/python3 /home/username/project/collector.py &
```

> **Note:** `/home/username/project` 부분은 실제 설치된 경로에 맞게 수정하여야 합니다.


