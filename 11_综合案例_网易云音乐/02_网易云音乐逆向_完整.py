import binascii

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import json
import requests
import base64

def b(a, b):
    c = b.encode('utf-8')
    d = '0102030405060708'.encode('utf-8')
    e = a.encode('utf-8')

    aes = AES.new(key=c, mode=AES.MODE_CBC, iv=d)
    e = pad(e, 16)
    return base64.b64encode(aes.encrypt(e)).decode()


def c(i, e, f):
    e = int(e, 16)  # 将e和f 16进制数据转化为10进制数值
    f = int(f, 16)
    i = i[::-1]
    bs = i.encode("utf-8")  # 将待加密参数字符串i转化为字节
    s = binascii.b2a_hex(bs).decode()  # 将字节转化为16进制
    s = int(s, 16)  # 将16进制又转化为10进制数值
    # 到这一步，e，f，s全都被转化为了10进制数值
    res = (s**e) % f  # 进行rsa加密
    return format(res, "x")


def d(d,
      e='010001',
      f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7',
      g='0CoJUm6Qyw8W8jud'):
    h = {}
    i = '1eOHSUBwXoWq3xIQ'
    h['encText'] = b(d, g)
    h['encText'] = b(h['encText'], i)
    # h['encSecKey'] = '5275ed9a42b5a4c3a056bda80986295e57d4c0afebbc5edd76d21ef6a74e9cc9c4644eefc182c2a19fc8ade0307fda204254285100c47b0ad2339e3d0c633402ba037f90f5b90c0794f887d7393706150d5d0999f9b715d7b4e9a5c19613ef5c18d68414d84f7f4ed16a179d9d6243ffaddf3c9012e14b61d615f3f32d7e554b'
    h['encSecKey'] = c(i, e, f)
    return h



def get_name(id):
    music_detial_api = 'https://music.163.com/weapi/v3/song/detail?csrf_token='

    unenc_data = {"id": str(id),
                  "c": '[{"id": "%s"}]' % str(id),
                  "csrf_token": ""}
    enc_data = d(json.dumps(unenc_data))

    data = {
            'params': enc_data['encText'],
            'encSecKey': enc_data['encSecKey']
        }

    # 定义请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
    resp = requests.post(music_detial_api, headers=headers, data=data).json()
    song_name = resp['songs'][0]['name']
    author_name = ','.join([i['name'] for i in resp['songs'][0]['ar']])
    return song_name + f'({author_name}).m4a'

def main(songs_list):
    # 定义请求api
    music163_api = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
    # 定义未加密参数
    unenc_data = {"ids": songs_list,
            "level": "standard",
            "encodeType": "aac",
            "csrf_token": ""}


    # 进行参数加密
    enc_data = d(json.dumps(unenc_data))
    print(enc_data['encSecKey'])
    # 定义表单
    data = {
        'params': enc_data['encText'],
        'encSecKey': enc_data['encSecKey']
    }
    # 定义请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        'cookie': "_ntes_nuid=99cc9368708cbd31213f1ac87b133fa3; _ntes_nnid=99cc9368708cbd31213f1ac87b133fa3,1683719885831; NMTID=00OHzKN0mriqmeTHkJ4gezSRHG_wq4AAAGIBYaRig; WEVNSM=1.0.0; WNMCID=gnrbuq.1683719886109.01.0; WM_TID=tH%2FLT6nXTBFBVBRURRaFJIa%2F3oKgjWHQ; WM_NI=FLqr1TGstCT%2FtRCqt5z5zxA4R0Gdl5eDEnXKKHJSKDHAKytaUsrKoj5Jpfl%2Fo0SNX7q6U8PxDuMC%2FbMg5gmFuOK%2FYGNlqBhAT0XxM8rao9D2CIigOaBnPQLTLyMghfqMTEM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87f93ab0eaa7afb55ea7eb8ea7c14e868a8a86c564828fa28cc6679188b789c82af0fea7c3b92a8694bf93b46085adbca4d725b88e8d92f73fbaebb699c44092f08985ef3fa79c8b8fdb41899886b4ca508c9f859af76b97adbeacee62f796c087ef25adf09dafdb3db3ea9bd9d37488ab83a4ae6a8fb9fb88f04eb79185d0dc4d8eb4bfa3eb4b98f09899d034b2bfa1dac73a8197a788ce6b82b2a0b2cf6090a78388eb6eb3939ca6d037e2a3; playerid=15187704; _iuqxldmzr_=33; JSESSIONID-WYYY=6SEmGX%5C5AbGPHgGo%5Co%2BaDqI7RGnOxBsJCFZIsJnEJMKCRtpohfmMob8C6yf0%2BljXcDJCCBI52zmW8nSHC%2F4VBtKGwixR2vE%2FXP9yd7Qsve%2FCXHXarqSgmDGUFFEVYfxe99Jhydu%2BYvIvKuq1290ye7qr3vJhMa6YysddntdgFlNVtN6r%3A1683728315239; __snaker__id=cU3ifJGTngek5SHk; gdxidpyhxdE=NQ7CfHlGSH%5CYeCOHnS8Iw%2FQTYt9tRqaMwE4sN7ErE2I5nWwozDdbT8aIzEcZ3D0tkmk%5CbCXh8PTdBavwAVRbcURa9q19Q3Qz%5CmgmA%2Bweko0H2izxGREUKHiBfjJkWaDcyo62GJ1PvgHxNtevpz%5CzS8JOofj13a1fViJTzIEV9ST3lHe7%3A1683727446578; YD00000558929251%3AWM_NI=FEeSTZ44PiCZbt%2BDF8%2FWdHAlwNdqc%2FXIUHrzjrJXAG4WERWNUQNDQG5%2BiTLxvTodvCIyFmXyPbldMYk%2FnBOIEeCScxC%2F78ScFpsT8NLV0oHfC5TgPm4b87uvjNNu05jCOTY%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee93f87ca8b0e593d041ed8e8aa6c45b979e8b82c861838ea693d34e90969faac72af0fea7c3b92a869babb4d752f8eca08ac252a2ace5a5c534ed89aca9c468b592ac92e2259c979ba9f172aaae86b9c44df8898bb3d646978f82a5d44df7f5a7b5cf74b68ca185f5498ba78a8edb7394bea485d053a9f1a2a3ce4387bb8db4e27481f1f9d9d26986b0bdb5bb46908a0090cb6e81eb9c88d367f8bef8d8f87eaa928296b33faa9d81b5dc37e2a3; YD00000558929251%3AWM_TID=V4Qbl6%2B9lmdAABVEERPQlVBn%2BaULJQJX; MUSIC_U=bb079b374eb4b03a364680e504c868445cb0a416905243eb637f10dc35ae0a93993166e004087dd314e9fef4ee690a66321b12b8f56b9932ee71090ba55cdd7518b0f89de7449423a0d2166338885bd7; __csrf=c2085817cefcd5ea1172356c083bf608"
    }
    resp = requests.post(music163_api, headers=headers, data=data).json()
    for i in range(len(resp["data"])):
        filename = get_name(resp["data"][i]["id"])
        with open(filename, 'wb') as f:
            f.write(requests.get(resp["data"][i]["url"]).content)
        print(filename + '下载成功！')


if __name__ == '__main__':
    songs_list = [1463165983]
    main(songs_list)
