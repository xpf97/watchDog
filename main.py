import requests
# import re
import time
import telegram
# from telegram.ext import Updater
# from telegram.ext import CallbackContext
import logging
import json
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

with open("./config.json") as f:
    conf= json.load(f)
TOKEN = conf['telegram']['TOKEN']
chat_id= conf['telegram']['chat_id']

bot = telegram.Bot(token=TOKEN)
updates = bot.get_updates()

proxies = {
        "124.77.82.32:9000",
        }

HEADERS = {
        # 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        # 'Referer': 'http://www.baidu.com'
        # 'cookie'
        }

DIR_PATH = "temp"


# formdata = {}
# r = requests.post(url,data=formdata)
# jar = requests.cookies.RequestsCookieJar()
# for item in r.cookies:
# jar.set(item.name,item.value)

url= "https://www.ddrk.me"

# params = {"s":"wd=baidu"}
# cookies = response.cookies;

history = ""

bot.send_message(text='start watching...',chat_id=chat_id)
while 1:
    response=requests.get(url,headers=HEADERS,timeout=10)
    if response.status_code == 200:
        if response.text == history:
            time.sleep(10)
        else:
            history = response.text
            text = 'web changed at ' + datetime.now().strftime("%y-%m-%d %H:%M:%S")
            bot.send_message(text=text,chat_id=chat_id)
            print(text)
    time.sleep(60*60*2)
