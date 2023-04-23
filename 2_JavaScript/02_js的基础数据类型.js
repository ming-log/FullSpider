// JS中的基本数据类型
// number 数字，不论是整数还是小数，数据类型都是number
// string 字符串
// boolean 布尔值，true和false
// object 对象，需要被new出来
// undefined 表示未定义


// 变量 变量名 = 值;
var name = 'luoming'
console.log(name)

// 可以先声明变量，再进行赋值
var name;
name = "luoming2"
console.log(name)
console.log(typeof name)  // 查看数据类型

// 一次声明多个变量
var name, age, sex
name = 'luoming3'
age = 18
sex = '男'
console.log('姓名:' + name, "\n年龄:" + age, "\n性别:" + sex)

console.log('---------------------------')
// JS中无解包操作
var name1, age1, sex1 = '男'  // 默认情况下只会对最后一个变量进行赋值
console.log('姓名:' + name1, "\n年龄:" + age1, "\n性别:" + sex1)
