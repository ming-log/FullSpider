// 三元运算符
// x ? y : z  x是条件表达式，如果成立返回y，不成立返回z

let a1 = 3
let b1 = 6
let c1 = a1 > b1 ? a1 : b1;
console.log(c1)


console.log('----------------------')
let a = 10;
let b = 20;
let c = 5
let d = 17

let e, m;

e = (e = a > 3 ? b : c, m = e < b++ ? c-- : a % 3 > b % d ? 27 : 37, m++);
console.log(e)
console.log(c)
console.log(m)

