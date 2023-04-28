from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

s = '你今天开心吗？'
key = b'\x032345670'  # \x03这是一个字节

# 加密
aes = DES.new(key=key, mode=DES.MODE_ECB)
bs = s.encode('UTF-8')
bs = pad(bs, 8)
result = aes.encrypt(bs)
print(result)
# 解密
aes = DES.new(key=key, mode=DES.MODE_ECB)
resde = aes.decrypt(result)
resde = unpad(resde, 8)  # 去除填充
print(resde.decode('utf-8'))


# CBC模式
iv = b'dascwefw'  # 偏移量
# 加密
aes = DES.new(key=key, mode=DES.MODE_CBC, IV=iv)
bs = s.encode('UTF-8')
bs = pad(bs, 8)
result = aes.encrypt(bs)
print(result)
# 解密
aes = DES.new(key=key, mode=DES.MODE_CBC, IV=iv)
resde = aes.decrypt(result)
resde = unpad(resde, 8)  # 去除填充
print(resde.decode('utf-8'))
