#!/bin/bash

cd "$(dirname "$0")/.."
if ! pgrep -f "collector.py" > /dev/null
then
	nohup ./venv/bin/python3 ./collector.py &
	echo "봇이 꺼져 있어서 다시 실행했습니다: $(date)" >> ./bot.log
fi	
