// window = global;  // 此行在真正使用时需要删除，这里是单独的JS代码运行，所以需要定义
var aaa = 'Linux';  // 全局变量自动进入window
(function (){
    let haha = '嘻嘻嘻';
    window.name = 'name';
    sex = '男';  // window可以省略，不使用var,let,const等等关键词声明变量默认就是在window中进行创建
    console.log(window.aaa)
})()
// console.log(haha)  // ReferenceError: haha is not defined  局部变量无法在外部调用
console.log(aaa)
console.log(name)
console.log(sex)   // 没问题


// 链接跳转
// 2秒后跳转到百度
setTimeout(function (){
    window.location.href = 'https://www.baidu.com'
}, 2000)

