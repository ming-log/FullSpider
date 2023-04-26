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

word = '今天星期几？'

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
print(response.text)
result = response.content

key_obj = md5()
key = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
key_obj.update(key.encode('utf-8'))
md5_key = key_obj.digest()

iv_obj = md5()
iv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
iv_obj.update(iv.encode('utf-8'))
iv_key = iv_obj.digest()

aes = AES.new(key=md5_key, mode=AES.MODE_CBC, IV=iv_key)

base64_result = base64.b64decode(result)
i = 1
print(aes.decrypt(base64_result[16 * 0:16 * 1])
      + aes.decrypt(base64_result[16 * 1:16 * 2])
      + aes.decrypt(base64_result[16 * 2:16 * 3])
      + aes.decrypt(base64_result[16 * 3:16 * 4])
      + aes.decrypt(base64_result[16 * 4:16 * 5])
      + aes.decrypt(base64_result[16 * 5:16 * 6])
      + aes.decrypt(base64_result[16 * 6:16 * 7])
      + aes.decrypt(base64_result[16 * 7:16 * 8])
      )

#
# max_num = len(base64_result) // 16
# all_res = b''
# for i in range(max_num):
#     all_res += aes.decrypt(base64_result[16*i:16*(i+1)])
# all_res += aes.decrypt(Padding.pad(base64_result[16*(i+1):], 16))
# print(all_res)


print(aes.decrypt(Padding.pad(base64_result, 16)))
