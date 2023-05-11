# 字符串、十进制数值、十六进制数值、base64、字节、Unicode之间的相互转化

# 字符转化为ASCII编码
str1 = 'a'
ascii_code = ord(str1)
print(ascii_code)  # 109

# ASCII编码转化为字符
str1 = chr(ascii_code)
print(str1)  # m

# 字符串ASCII编码和解码
string = 'hello world!你好'
ascii_string = [ord(i) for i in string]
print(ascii_string)

print(''.join([chr(i) for i in ascii_string]))



# 字符串转化为Unicode编码
string = '你好，世界！'
ucode_string = string.encode('unicode_escape').decode()
print(ucode_string)
# Unicode编码转化为字符串
string = ucode_string.encode('utf-8').decode('unicode_escape')
print(string)

# 字符串转化为字节码
byte_string = string.encode()
print(byte_string)  # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'

# 字节码转化为字符串
string = byte_string.decode('utf-8')
print(string)

print("-"*50)
# 字节码转化为十六进制编码
import binascii
hex_string = binascii.b2a_hex(byte_string).decode()
print(hex_string)  # 'e4bda0e5a5bdefbc8ce4b896e7958cefbc81'
hex_string = binascii.hexlify(byte_string).decode()
print(hex_string)

# 十六进制编码转化为字节码
string = binascii.a2b_hex(hex_string)
print(string)  # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'
string = binascii.unhexlify(hex_string)
print(string)  # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c\xef\xbc\x81'

# 字节码转化为base64编码
print('*'*50)
import  base64
base64_string = base64.b64encode(byte_string).decode()
print(base64_string)
# base64编码转化为字节码
string = base64.b64decode(base64_string).decode()
print(string)

# 十进制数值转化为十六进制
num = 122
hex_num = hex(num).replace('0x', '')
print(hex_num)
hex_num = format(num, 'x')
print(hex_num)

# 十六进制转化为十进制
num = int(hex_num, base=16)
print(num)

# 十进制转化为二进制
bin_num = bin(num).replace('0b', '')
print(bin_num)  # 0b1111010
bin_num = format(num, 'b')
print(bin_num)  # 1111010

# 二进制转化为十进制
num = int(bin_num, base=2)
print(num)

# 十六进制转化为二进制
bin_num = format(int(hex_num, base=16), 'b')
print(bin_num)

# 二进制转化为十六进制
hex_num = format(int(bin_num, base=2), 'x')
print(hex_num)
