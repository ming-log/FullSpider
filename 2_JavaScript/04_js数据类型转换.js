var a = '1'

console.log(a + 1)  // 11  在JS中只要左右两端有一个字符串，得到的结果就是字符串的拼接

// 要想计算数值结果，需要将其转化为数值
a = parseInt(a)
console.log(a + 1)  // 2  此时得到的结果才是正常的数学运算

// 十进制   0 1 2 3 4 5 6 7 8 9
// 十六进制  0 1 2 3 4 5 6 7 8 9 A B C D E F
// 二进制 0 1
// 十进制 10   在十六进制中为A  在二进制中为  1010

a = 'aaa';  //  十六进制数字，如何转化为十进制
var a16 = parseInt(a, 16)
console.log(a16)

var str3 = 2730;  // 如何将其转化为16进制字符串
var a10 = str3.toString(16)
console.log(a10)
