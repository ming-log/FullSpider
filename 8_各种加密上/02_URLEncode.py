from urllib.parse import urljoin, urlencode, quote, unquote
# urljoin：将两个路径进行拼接，解决相对路径和绝对路径

# % + 两个16进制组成的数字，例如以下网站
# 做法具体是把url中的参数部分转化成字节，没字节的再转化成2个16进制的数组，前面补%
url = 'https://www.baidu.com/s?tn=44004473_16_oem_dg&ie=utf-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'

dict = {
    'name': 'luoming',
    'age': 18,
    'sex': '男'
}

r = urlencode(dict)  # name=luoming&age=18  在使用时，如果需要对字典进行处理，urlencode处理即可
print(r)

# quote必会，把字符串直接进行urlencode处理的方法
string = '今天天气真好'
quote_string = quote(string)
print(quote_string)  # %E4%BB%8A%E5%A4%A9%E5%A4%A9%E6%B0%94%E7%9C%9F%E5%A5%BD

# 在平时逆向的时候，url一般不用手工处理，参数也不用手工处理（dict）
# 但是，在cookie的处理的时候，需要手工处理

# cookie的值我已经拿到了，但是里面有可能会有一些必须要处理的字符（=, 空格, 冒号）
cook = {
    "name": "浏览器复制",  # 不用管，浏览器已经处理完了
    "token": quote("计算出来的")  # 计算出来的内容可能包含（=, 空格, 冒号），必须手工处理才不会报错
}

# 那么如何还原呢？
# 1. 写代码还原
print(unquote(quote_string))

# 2. 网页在线解析  # 例如：http://www.jsons.cn/urlencode/
