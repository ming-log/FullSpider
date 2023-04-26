import execjs
import requests
import time

# 利用JS获取sign值
with open('02_网络爬虫逆向（有道翻译）.js', 'r', encoding='UTF-8') as f:
    js_code = f.read()

js_compile = execjs.compile(js_code)
timestamp = int(time.time() * 1000)
sign = js_compile.call('hh', timestamp)

trans_api = 'https://dict.youdao.com/webtranslate'

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1174331413.9506707; OUTFOX_SEARCH_USER_ID=-420953441@27.18.211.154',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Referer': 'https://fanyi.youdao.com/'
}

data = {
    'i': '今天天气真好',
    'from': 'auto',
    'to':'auto' ,
    'domain': '0',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': timestamp,
    'keyfrom': 'fanyi.web'
}
print(data)
response = requests.post(trans_api, headers=headers, data=data)
print(response.text)




