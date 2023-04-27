import execjs
import requests
import time
from Crypto.Cipher import AES
from Crypto.Util import Padding
from hashlib import md5
import base64

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

word = '今天的天气真好！'

data = {
    'i': word,
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

response = requests.post(trans_api, headers=headers, data=data)
# print(response.text)
result = response.text

key_obj = md5()
key = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
key_obj.update(key.encode('utf-8'))
md5_key = bytearray(key_obj.digest())

iv_obj = md5()
iv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
iv_obj.update(iv.encode('utf-8'))
iv_key = bytearray(iv_obj.digest())

base64_result = bytearray(base64.b64decode(result))
pad_result = Padding.pad(base64_result, 128)

aes = AES.new(key=md5_key, mode=AES.MODE_CBC, IV=iv_key)
aes_result = aes.decrypt(pad_result)
print(aes_result)

# max_num = len(base64_result) // 16
# all_res = b''
# for i in range(max_num):
#     all_res += aes.decrypt(base64_result[16*i:16*(i+1)])
# all_res += aes.decrypt()
# print(all_res)


# print(aes.decrypt(Padding.pad(base64_result, 128)))
