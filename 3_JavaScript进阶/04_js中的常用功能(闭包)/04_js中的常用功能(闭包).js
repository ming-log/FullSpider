// jack和tom,一个写的是MD5加密,一个写的是AES加密
// 但是由于他们使用的密钥名称都叫做key,都是全局变量会被放入window.key中
// 这个时候将他们一起导入会导致前一个key把后一个key覆盖掉,导致这里调用AES加密算法时使用的是MD5的key
// 这样肯定是不对的
// AES_jiami('---我是骆明')  // AES:KEY-MD5MD5MD5MD5MD5加密---我是骆明
// 那么应该如何去保证自己的变量不被其他人冲突掉,这个就是闭包提出来的原因之一
AES_jiami_bb('---我是骆明')  // AES:AES:KEY-AESAESAESAESAES加密---我是骆明
MD5_jiami_bb('---113123123')  // MD5:KEY-MD5MD5MD5MD5MD5加密---113123123
