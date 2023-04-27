from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

s = '你今天开心吗？'
key = b'\x03234567890123456'  # \x03这是一个字节

# AES加密
# 常用的模式有CBC和ECB
# ECB模式下不需要给iv，iv是偏移量的意思
# CBC模式下需要给iv， 数据加密前需要偏移量更安全。

# ECB模式

# 加密
aes = AES.new(key=key, mode=AES.MODE_ECB)
bs = s.encode('UTF-8')
# ValueError: Data must be padded to 16 byte boundary in CBC mode
# AES是一批批等进行加密，这个如果不能整除就有部分数据无法加密
# 因此需要对数据进行填充，一般与密钥的长度一致
bs = pad(bs, 16)
result = aes.encrypt(bs)
print(result)
# 解密
aes = AES.new(key=key, mode=AES.MODE_ECB)
resde = aes.decrypt(result)
resde = unpad(resde, 16)  # 去除填充
print(resde.decode('utf-8'))


# CBC模式
iv = b'dascwedrfwefsdac'
# 加密
aes = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
bs = s.encode('UTF-8')
bs = pad(bs, 16)
result = aes.encrypt(bs)
print(result)
# 解密
aes = AES.new(key=key, mode=AES.MODE_CBC, IV=iv)
resde = aes.decrypt(result)
resde = unpad(resde, 16)  # 去除填充
print(resde.decode('utf-8'))