# 网站为了防止网络爬虫，对数据可能会进行加密操作

# 加密的过程是服务器（后台）完成。

# 解密的过程能不能看到？？？
# 能看到的

# 1. 对称加密：在加密和解密的时候，使用的是同一个密钥
# 同一把钥匙开同一个锁
# 常见的对称加密：AES,DES,3DES加密
# AES,DES两种不同的锁
# AES:
#     key: 16bit
#     iv: 16bit
#     mode:AES.ECB  AES.CBC
# DES:
#     key: 8bit
#     iv: 8bit
#     mode:AES.ECB  AES.CBC

# 2. 非对称加密：
#     RSA加密
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


