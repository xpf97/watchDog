import requests
import re
import time
import telegram
from telegram.ext import Updater
from telegram.ext import CallbackContext
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = '1778566006:AAFykoqBUXzZCYxeyB-ZGyVxe10S98NfmSM'
REQUEST_KWARGS={
    'proxy_url': 'socks5://127.0.0.1:2080/',
}

# updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
bot = telegram.Bot(token=TOKEN)
updates = bot.get_updates()
chat_id = 681868099
bot.send_message(text='web changed',chat_id=chat_id)
exit()

proxies = {
        "124.77.82.32:9000",
        }

HEADERS = {
    # 'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    # 'Referer': 'http://www.mzitu.com'
    # 'cookie'
}

DIR_PATH = "temp"


# formdata = {}
# r = requests.post(url,data=formdata)
# jar = requests.cookies.RequestsCookieJar()
# for item in r.cookies:
#     jar.set(item.name,item.value)

url = "https://www.ddrk.me"

# params = {"s":"wd=meizu"}
# cookies = response.cookies;

history = ""

while 1:
    response=requests.get(url,headers=HEADERS,timeout=10)
    if response.status_code == 200:
        if response.text == history:
            time.sleep(10)
        else:
            history = response.text
            print("web changed")
    time.sleep(10)

