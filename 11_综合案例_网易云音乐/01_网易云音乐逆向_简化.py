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

def d(d,
      e='010001',
      f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7',
      g='0CoJUm6Qyw8W8jud'):
    h = {}
    i = '1eOHSUBwXoWq3xIQ'
    h['encText'] = b(d, g)
    h['encText'] = b(h['encText'], i)
    h['encSecKey'] = '5275ed9a42b5a4c3a056bda80986295e57d4c0afebbc5edd76d21ef6a74e9cc9c4644eefc182c2a19fc8ade0307fda204254285100c47b0ad2339e3d0c633402ba037f90f5b90c0794f887d7393706150d5d0999f9b715d7b4e9a5c19613ef5c18d68414d84f7f4ed16a179d9d6243ffaddf3c9012e14b61d615f3f32d7e554b'
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
    # 定义表单
    data = {
        'params': enc_data['encText'],
        'encSecKey': enc_data['encSecKey']
    }
    # 定义请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    }
    resp = requests.post(music163_api, headers=headers, data=data).json()
    for i in range(len(resp["data"])):
        filename = get_name(resp["data"][i]["id"])
        with open(filename, 'wb') as f:
            f.write(requests.get(resp["data"][i]["url"]).content)
        print(filename + '下载成功！')


if __name__ == '__main__':
    songs_list = [2045090557, 1857630559]
    main(songs_list)
