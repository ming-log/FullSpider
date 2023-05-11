import binascii
# 字符串加密为十六进制编码
string = '如果你的眉眼，肯为我停留半分，又怎会不知我情比海深。'
string_hex = binascii.b2a_hex(string.encode('utf-8')).decode()
print(string_hex)

# 还原
string = binascii.a2b_hex(string_hex).decode('utf-8')
print(string)

import base64
# 字符串加密为Base64编码
string = '如果你的眉眼，肯为我停留半分，又怎会不知我情比海深。'
string_b64= base64.b64encode(string.encode('utf-8')).decode()
print(string_b64)
# 解码
string = base64.b64decode(string_b64).decode('utf-8')
print(string)

# 数值转化为二进制后取反进行加密
num = 5201314
bin_num = format(num, 'b')
min_bin_num = ''.join([str(int(i) ^ 1) for i in bin_num])
print(min_bin_num)  # 01100001010001001011101

# 解密
bin_num = ''.join([str(int(i) ^ 1) for i in min_bin_num])
num = int(bin_num, base=2)
print(num)

