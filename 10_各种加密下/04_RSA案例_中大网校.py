# 目标：https://user.wangxiao.cn/login?url=https%3A%2F%2Fwww.wangxiao.cn%2F
# 模拟账号密码登录
import json

# 为了处理不同人在进行校验时验证码不冲突，不出错。
# 一般会和cookie进行连用，用来确定某个人输入指定的验证码验证成功才生效

# 保持住cookie的方案
# 1. session，只能处理response头的cookie
# 2. js处理的cookie。session是没办法解决的（手工来处理）
# 3. 既有response头的cookie又有JS处理的cookie，综合上述两种方案。

import requests
import base64
from tujianAPI import base64_api
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


# 处理验证码识别问题
login_page_url = 'https://user.wangxiao.cn/login'
img_api = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
session = requests.session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
session.get(login_page_url)
img_resp = session.post(img_api, headers={"Content-Type": "application/json;charset=UTF-8"})
base64_img_code = img_resp.json()['data'].split(',')[-1]
base64_decode_img = base64.b64decode(base64_img_code)
with open('tu.png', 'wb') as f:
    f.write(base64_decode_img)
img_code = base64_api("minglog", "luo736704198", "tu.png", 3)
# print(img_code)

# 处理密码加密问题
get_time_api = "https://user.wangxiao.cn/apis//common/getTime"
get_time_resp = session.post(get_time_api, headers={"Content-Type": "application/json;charset=UTF-8"})
get_time_code = get_time_resp.json()['data']

# # 定义账号密码
account = '18827450450'
password = 'luo736704198'

# # 拼接待加密参数
password_concat = password + get_time_code
# print(password_concat)

public_key_bs64 = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"
public_key = RSA.import_key(base64.b64decode(public_key_bs64))  # 将bs64格式的公钥转化为加密器所需格式
rsa_ = PKCS1_v1_5.new(key=public_key)  # 使用公钥创建加密器
mi_bytes = rsa_.encrypt(password_concat.encode('UTF-8'))  # RSA加密
mi_bs64 = base64.b64encode(mi_bytes).decode()
# print(mi_bs64)

# 开始发送登录请求
login_api = 'https://user.wangxiao.cn/apis//login/passwordLogin'
data = {
    "imageCaptchaCode": img_code,
    "password": mi_bs64,
    "userName": account
}
login_resp = session.post(login_api, data=json.dumps(data), headers={"Content-Type": "application/json;charset=UTF-8"})
# print(login_resp.text)

test_url = "http://ks.wangxiao.cn/TestPaper/getPaperRuleQuestions"
test_data = {
    "id": '"21F74E2F-44FA-4550-B481-5EF80A4BA09F"'
}
test_resp = session.post(test_url, data=test_data, headers={"Content-Type": "application/json;charset=UTF-8"})
print(test_resp.text)
