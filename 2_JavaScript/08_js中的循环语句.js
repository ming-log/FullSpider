// while 循环
var a = 0
while (a < 10) {
    if (a == 5) break
    console.log(a++);
}
console.log('------------------------')
// do ... while ... 循环，相比于while无论条件是否成立都会执行一次
a = 0
do {
    console.log(a)
} while (a++ < 10)

console.log('------------------------')
// for ... 循环
var arr = [11, 22, 33, 44]
for (var x in arr) {
    console.log(x)  // 获取的是索引
}
var arr = [11, 22, 33, 44]
for (var x in arr) {
    console.log(arr[x])  // 使用索引获取数据
}
console.log('------------------------')
// 经典for循环
for (var i = 0; i < 10; i++) {
    console.log('for' + i)
}
