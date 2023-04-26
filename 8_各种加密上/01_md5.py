from hashlib import md5  # 导入md5


# 创建一个对象
obj = md5()

# 准备你要计算的东西
name = '骆明'.encode('utf-8')  # 要使用字节,将UTF-8数据转化为字节

# 把数据丢给obj
obj.update(name)


# 导入md5值
val = obj.hexdigest()
print(val)  # bc6c8690fba70ef53c2c9309b758ac71

# 需要注意两个问题
# 1. obj是一次性的
# 2. 默认的md5是有问题的
# 有部分开发者再自己的数据库中生成上亿条MD5对应的数据用来撞库，这个时候简单的md5就容易被破解
# https://www.somd5.com/     -->  可以破解
# 解决方案：可以在使用md5的时候，撒盐用来对抗撞库问题。
# 如下所示

# 创建一个对象
salt = 'zheshisadeyan'
obj = md5(salt.encode('UTF-8'))

# 准备你要计算的东西
name = '骆明'.encode('utf-8')  # 要使用字节,将UTF-8数据转化为字节

# 把数据丢给obj
obj.update(name)


# 导入md5值
val = obj.hexdigest()
print(val)  # da205965e558f80b4a5157c493d6623a
# 这个时候就无法破解
# 要确定网页上是否撒盐了，可以生成一个md5码和未撒盐的进行对比。
