from functools import partial  # 这个函数可以锁定一个函数的参数
import subprocess

# 固定subprocess.Popen的encoding参数为UTF-8
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

print(execjs.get().name)  # Node.js (V8)

# 调用JS文件
with open("01_Test.js", 'r', encoding="utf-8") as f:
    js_code = f.read()

# 编译JS代码
js_obj = execjs.compile(js_code)

# 运行JS中的函数
print(js_obj.call("a", 1, 2))

# ['锟斤拷锟斤拷', '锟斤拷锟斤拷', 'wangwu', '锟斤拷锟斤拷', '钱锟斤拷']
# 刚开始出现了报错，原因是因为，在这里运行JS代码默认的情况下是在控制台中执行node xxx.js代码，输出编码为GBK
# 所以我们需要把输出的编码固定为'UTF-8'，故在文件开头输入以下代码，将Popen类的encoding参数固定为UTF-8
# 注意：一定要在import execjs之前导入进来，放在最开头最好
# from functools import partial  # 这个函数可以锁定一个函数的参数
# import subprocess
#
# subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

