# 我们目前使用的是HTTP协议
# http协议传输的数据包：
# 请求行(url, 请求方式, http版本)
# 请求头(UA,cookie,referer,host...)
# 请求体(如果是GET就没有请求体，如果是POST，请求体中会存放数据)

# HTTP协议，发送数据的时候，字符串是最好处理的
# HTTP处理字符串是非常容易的，传输的时候效率也是高的
# 在发送和处理字节的时候是很麻烦的

# 网站如果先要对自己的数据进行保护，很有可能对数据进行加密
# "今天天气真好"  => 加密后变成一堆无法辨认的字节（用眼睛一定看不出来长啥样）
# 这就导致，加密后的数据和服务器之间进行交互就很难受
# 就需要想一个办法，把字节处理成HTTP容易处理的字符串
# 这个时候BASE64就产生了。有大写字母，小写字母，数字0-9，以及/和+组成  一共64个符号
# BASE64用来把字节变成字符串，把字符串还可以还原成字节    这个操作是可逆的
# BASE64处理的时候，三个字节一起处理，处理成4的字符
# 并且处理完成后一般会比原来大一点
import base64

s = "你好啊，兄弟！"
bs = s.encode('UTF-8')
print(bs)

# 把字节转化成base64的字符串
b64_str = base64.b64encode(bs).decode()
print(b64_str)  # 5L2g5aW95ZWK77yM5YWE5byf77yB

# 把base64字符串还原成字节
bs_bytes = base64.b64decode(b64_str)
print(bs_bytes)

# 图片 => 字节
img_s = 'iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAqNJREFUaN7tWMtu1DAULeL1B2XBCgRL3j8APwBLxIblsCqbfkAH/qAJsROGne2CsuiyXY5gTVsJluUfAIlHRRkN9ySdiTMMtZ3JJIzqK1mKZnJ9z/E9vnbu0pI3b968Lbxxnl4MIvV4PRJd0wi5WsO78PkvwK/H6kHAxE8CN3Qb8kfIxP12wTN1h4AcuoMfkzh8kYjbrYBPkvdng0h+GIE5eu5aDSY+6n5pmp5rnEDA5DNtNb8xpi7b+uJd+BT+6nmz4OM3N0j3v8YAmFxxl59c0aUU8Ne3agfa7/fPQKOk9Y4ugSAS+2MJMPluOByecp0bPgT8bTGP+FSWGcWkPQYMlcAztnGdAuyZKkkcq6tVFyh6lV4h4N8NMfaAxRk8rfLBcRPT5vtK2r03a5ZDLu7mcx0XSxxYk0DKJlb+M1WNpHQQxeIR55vL9R2Em8uYE3NrlSrJYmuZsJJTXtsL8GEvveQKqNfbuBBG8mHA5SoGnvGbc3YodokEYbMh0CkcROJUnaiSULq3yXcwRQoD/Be9VDfdqlWWiVxKXDwxO+QpHAXt2oNXT6ki/TadvngH71oTcMVThQAA/QUykjvZ6tHA8yQ5WxJzJ5DJRgOHq8G0QymXl3b1yDJhPrzmTyDXfAF+a+v8P9+l/8r3J7HdKgFUltGGtV3RiYwNTNVprgRQHrXV37He8NgfR36YozUCqPFVSm65NMpVT+DESmjhN/HCl9FZDzKbe5G/SpyIy5zLddr1471RAnV/0LRGoNbunzOBGb7I5tO+LE5tYDM6ZH2gYsN9cem41W2IDQwjPFZ91DRNTwdM7Ook9K5EYwPlVwMPTMBm1w1I5DVTX6jJASzA5NbSAAktE62BJwzO4HU5TeuNNiMh1UFsa9l48+bNm7cq9gfmr6wmxprr4wAAAABJRU5ErkJggg=='
img = base64.b64decode(img_s)  # Base64解密
# 存储字节编码为图片
with open('base64.jpg', 'wb') as f:
    f.write(img)

# base64的字符串本质是什么？字节
# 所有的高级加密逻辑里99%都会用到BASE64

