#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
subscriberListFile = "./subscriberList.txt"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = str(update.effective_chat.id)

    # 기존 명단 읽기
    with open(subscriberListFile, 'r') as f:
        ids = [line.strip() for line in f if line.strip()]

    # 중복 체크 후 저장
    if chat_id not in ids:
        with open(subscriberListFile, 'a') as f:
            f.write(chat_id + '\n')

        print(f"새로운 구독자 추가: {chat_id}")
        await update.message.reply_text("등록되었습니다.")
    else:
        print(f"기존 구독자: {chat_id}")
        await update.message.reply_text("이미 등록된 사용자입니다.")

if __name__ == '__main__':
    # 봇 실행
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("수집기 가동 중")
    app.run_polling()

