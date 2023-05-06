# 对称加密：加密和解密的密钥是一样的。
# 非对称加密：加密和解密的密钥是不一样的。
# 一组密钥：公钥+私钥
# 公钥：公开的密钥，对数据进行加密
# 私钥：私密的密钥，对数据进行解密

# 非对称加密的逻辑：
# 1. 先在服务器端，生成一组密钥{公钥+私钥}
# 2. 把公钥放出去
# 3. 客户端拿到公钥之后，可以使用公钥对数据进行加密
# 4. 把数据传输给服务器
# 5. 服务器需要对数据进行解密，私钥能够解密

"""
不论哪种RSA加密，最终都是同一堆数学公式
"""
import base64

from Crypto.Cipher import PKCS1_v1_5  # RSA加密器
from Crypto.PublicKey import RSA  # 用来生成密钥

# 使用RSA之前，必须想办法搞到公钥或者私钥
# 1. 生成公钥私钥
rsa_key = RSA.generate(1024)
print(rsa_key.exportKey().decode())  # 默认只生成私钥
# PEM格式（Base64）
# -----BEGIN RSA PRIVATE KEY-----
# MIICXgIBAAKBgQDNcmv3T/vjL/bKbU3h0hAiu8ziHQRpHbLJEEbnxXiMyJoRp9ux
# Na+inJqVEclfjlJzVroFM1RzWSAba0vOnla+V0RH8p8jSrcOeO8p4Qdjwzqx9ED7
# V52D0nhsEdK0ifS2IGYJb813osstlkP8AtvbD78Mydbf8lFYs7VQxKqI5wIDAQAB
# ...
# -----END RSA PRIVATE KEY-----
# print(rsa_key.exportKey(format='DER'))  # 生成字节编码
# print(base64.b64encode(rsa_key.exportKey(format='DER')))  # 转化为base64对比发现和上面生成的一样

pub_key = rsa_key.public_key().exportKey()  # 使用私钥生成公钥
print(pub_key.decode())  # 可以直观看到私钥比公钥长
