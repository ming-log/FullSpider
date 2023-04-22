// ****** 变量提升
function fn(){
    // var name;
    // 站在开发人员角度分析，是不合理的
    console.log(name)  // 会提前声明变量,这种现象叫做变量提升
    var name = '123'  // 正常会报错，但是在JS中返回undefined
    // 新版本的js修复了 es6
    // 使用 let声明变量就不会出现变量提升
}
fn()  // undefined


function fn2(){
    console.log(name)
    let name = '123'
}
// fn2()  // 这个时候就会报错

// ****** 常量定义
console.log('---------------------');
// 常量的声明，不希望后续的程序去修改变量的值
var BIRTH_DAY = "2000,1,1";
// 使用var声明还是可以强行修改
BIRTH_DAY = "1999,1,1"
console.log(BIRTH_DAY)

// 为了禁止变量的修改可以使用const关键词进行声明
const DATE = '2023.1.1'
// DATE = '2022.1.1'  // 这个时候强行修改就会报错 Assignment to constant variable.
console.log(DATE)
console.log('---------------------');


