# 生产公钥和私钥的正确逻辑
# 因为不可能每个人访问都生成一个公钥和私钥，这样会严重影响服务器性能
# 一般会固定专门的时间生成公钥和私钥，并将其写入到文件中，使用时去调用文件


from Crypto.PublicKey import RSA  # 用来生成密钥

# 定义生成器
rsa_key = RSA.generate(2048)

private_key = rsa_key.export_key()   # 生成私钥
public_key = rsa_key.public_key().export_key()  # 生成公钥

# 存入文件
with open("rsa_private.pem", 'wb') as f, open('rsa_public.pem', 'wb') as g:
    f.write(private_key)
    g.write(public_key)
