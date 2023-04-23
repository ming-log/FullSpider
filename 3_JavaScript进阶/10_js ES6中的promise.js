// 异步加载  promise中的函数会给两个参数resolve和reject，分别表示请求成功运行的逻辑和请求失败的逻辑

// 发送请求的函数
// 无法确定这个请求什么时候回来
// 异步的
function send(url) {   // 发送请求的函数
    let p = new Promise(function (resolve, reject) {  // promise在创建的时候，自动运行这个function
        console.log("发送一个请求" + url);  // 模拟
        setTimeout(function () {
            let data = '从' + url + '返回的数据';
            let status = 200;
            // 处理数据
            if (status === 200) {
                resolve(data)  // 本次请求没有问题
            } else {
                reject(data)  // 本次请求有问题
            }
        }, 1000)
    });
    return p
}

// p 需要填补,resolve和reject
send('login.html').then(data => {  // 如果请求没问题，接下来要运行的逻辑写在then中
    console.log(data)
    return send('menu.html')  // 如果then中返回的东西还是promise的话，可以继续then,
}).then(data => {
    console.log("处理菜单")
    return send("用户菜单")
}).then(data => {
    console.log('展示完毕！')
})

console.log('----------------------')
send('login.html').then(data => {  // 如果请求没问题，接下来要运行的逻辑写在then中
    console.log(data)
    return data    // 如果then中返回的东西不是promise的话，也可以继续then，返回的内容会传递给下一个then
}).then(data => {
    console.log("处理菜单")
    return data
}).then(data => {
    console.log(data)
})

console.log('----------------------')


send('login.html').then(data => {  // 如果请求没问题，接下来要运行的逻辑写在then中
    console.log(data)
    return data    // 如果then中返回的东西不是promise的话，也可以继续then，返回的内容会传递给下一个then
}).then(data => {
    console.log("处理菜单")
    return data
}).then(data => {
    console.log(data)
}).catch(function (data) {
    console.log('请求失败，请刷新后重试，还是有问题请联系管理员！')  // 如果请求有问题，接下来要运行的逻辑写在catch中
})

/*
* Promise在es6后出现.
* Promise对象在创建的时候需要传递function(resolve，reject)}
* 第一个参数会在当前本次操作中，如果没有问题的情况下去调用
* 第二个参数会在当前本次操作中，如果有问题的情况下去调用
*
* Promise()对象在使用的时候，通过then给对象传递resolve的实际回调函数
* Promise()对象在使用的时候，通过catch给对象传递reject的实际回调函数
*
* 案例：
* var p = Promise(function(resolve, reject){
*       去执行一些操作.
*       根据情况来调用resolve(xxx) 或者 reject(xxx)
* })
*
* p.then(function(){
*   return new Promise();
* }).then(function(d){
*   return new Promise();
* }).catch(function(){
*   return xxxx
* })
* */
