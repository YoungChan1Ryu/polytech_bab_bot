#!/bin/bash
cd "$(dirname "$0")"
. ./.polytech_bab_bot/bin/activate
python ./polytech_bab_bot.py
