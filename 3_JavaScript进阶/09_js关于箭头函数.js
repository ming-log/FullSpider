console.log('-------------------------')
let fn = function (){
    console.log('hello world!');
}
fn();

// 箭头函数
// 无参数
console.log('-------------------------')
let gn = () => {
    console.log('hello javascript！');
}
gn();

// 传入一个参数
console.log('-------------------------')
let hn = (a) => {
    console.log(a);
}
hn(123);

// 传入一个参数,参数外的括号可以省略
console.log('-------------------------')
let h1n = a => {
    console.log(a);
}
h1n(123);

// 传入多个参数，参数外的括号不可省略
console.log('-------------------------')
let h2n = (a, b) => {
    console.log(a+b);
}
h2n(123, 1);

console.log('-------------------------')
function f1(m, n){
    n(m);
}

a = 100
f1(a, p => {
    console.log(p);
})

