# endata，ob混淆
# https://www.endata.com.cn/BoxOffice/BO/Year/index.html

# 1. 完全手撸（选择这个）
# 2. 扣代码（补环境——> jsdom）
# 3. AST（入门难度极大）

# import binascii  # 实现16进制字符串和字节之间的相互转化
#
# binascii.a2b_hex()  # 16进制字符串转化为字节
# binascii.b2a_hex()  # 字节转化为16进制字符串
from Crypto.Cipher import DES
import binascii
import json

import requests

def func(a, b, c):
    if 0 == b:
        return a[c:]
    result = a[:b]
    result += a[(b+c):]
    return result

def shell(a):
    b = int(a[-1], 16) + 9
    c = int(a[b], 16)

    a = func(a, b, 1)
    b = a[c:c+8]
    a = func(a, c, 8)

    c = b.encode('UTF-8')
    b = b.encode('UTF-8')

    a = binascii.a2b_hex(a)  # 将16进制数据还原成字节
    # DES解密
    des = DES.new(key=c, mode=DES.MODE_ECB)
    result = des.decrypt(a).decode('utf-8')

    # 删除最右侧}后面的内容
    result = result[:result.rindex('}') + 1]
    return json.loads(result)

if __name__ == '__main__':
    url = 'https://www.endata.com.cn/API/GetData.ashx'

    data = {
        'year': 2023,
        'MethodName': 'BoxOffice_GetYearInfoData'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    res = requests.post(url, data=data, headers=headers).text
    print(shell(res))
