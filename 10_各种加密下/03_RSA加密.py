from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

# 1. 定义待加密文字
data = '今天天气不好，下了大雨。'
# 2. 获取公钥进行加密
# 2.1 读取公钥
with open('rsa_public.pem', 'rb') as f:
    public_key_bytes = f.read()
# 2.2 将公钥进行加载，加载成rsakey类型
public_key = RSA.import_key(public_key_bytes)
# 2.3 创建一个加密器
rsa_ = PKCS1_v1_5.new(key=public_key)  # 使用公钥创建加密器
# 2.4 使用加密器进行加密
mi_bytes = rsa_.encrypt(data.encode('UTF-8'))
print(mi_bytes)

print('----------------- 解密开始 ------------------')

# 3. 获取私钥进行解密
# 3.1 读取私钥
with open('rsa_private.pem', 'rb') as f:
    private_key_bytes = f.read()
# 3.2 将私钥进行加载，加载成rsakey类型
private_key = RSA.import_key(private_key_bytes)
# 3.3 创建一个解密器
rsa_2 = PKCS1_v1_5.new(key=private_key)
# 3.4 使用解密器进行解密
ming_bytes = rsa_2.decrypt(mi_bytes, None).decode('utf-8')
print(ming_bytes)
