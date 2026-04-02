#!/bin/bash

cd "$(dirname "$0")"
if ! pgrep -f "polytech_bab_bot_ID_collector.py" > /dev/null
then
	nohup python3 ./polytech_bab_bot_ID_collector.py &
	echo "봇이 꺼져 있어서 다시 실행했습니다: $(date)" >> ./polytech_bab_bot_ID_collector.log
fi	
