// 常规定义
let a = 10
let b = 3, c = 5, d = 7, x, y, z = 110

// 在函数中使用时，有一定的变化
function fn(){
    return a = 10, b = 111, c = b - a, c
}

// 与下面的函数等价
hn = () => {
    a = 10;
    b = 111;
    c = b - a;
    return c
}

console.log(fn());
console.log(hn())
