# 目标：https://user.wangxiao.cn/login?url=https%3A%2F%2Fwww.wangxiao.cn%2F
# 模拟账号密码登录

# 为了处理不同人在进行校验时验证码不冲突，不出错。
# 一般会和cookie进行连用，用来确定某个人输入指定的验证码验证成功才生效

# 保持住cookie的方案
# 1. session，只能处理response头的cookie
# 2. js处理的cookie。session是没办法解决的（手工来处理）
# 3. 既有response头的cookie又有JS处理的cookie，综合上述两种方案。



