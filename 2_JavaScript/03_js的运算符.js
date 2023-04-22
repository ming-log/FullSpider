// 且: &&
// 或: ||
// 非: !

var a = 3, b = 5, c = -3
console.log(a > b && b > c)  // false
console.log(a < b && b > c)  // true
console.log(!(a < b))  // false
console.log(!a < b)  // true

console.log("--------------------")  // true

var str1 = '123'
var str2 = 123

console.log(str1 == str2)  // true  在JS中==，比较的是两个变量里面的吧值是否一样
console.log(str1 === str2)  // false 同时判断值和数据类型
