// setTimeout(任务, 时间)  过多长时间去执行某个任务
function fn(){
    console.log('hello world!')
}

setTimeout(fn, 5000)  // 表示过5s去执行函数fn，时间单位为ms

setTimeout(function (){
    console.log('你好，匿名函数延时运行。')
}, 2000)

// setInterval(任务, 时间)  每隔一定时间自动运行任务
n = 1
let s = setInterval(function (){
    console.log('输出'+n);
    n++;
}, 1000)

window=global;
// 想要停止一个setInterval定时器，可以使用window.clearInterval()
window.clearInterval(s);
