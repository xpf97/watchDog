import requests
import re

# "proxy":"124.77.82.32:9000",

HEADERS = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    # 'Referer': 'http://www.mzitu.com'
}

DIR_PATH = "temp"

url = "https://ddrk.me"
res=requests.get(url,headers=HEADERS,timeout=10)


print(res.text)
