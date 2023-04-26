function fn(a, b){
    console.log(a);
    console.log(b);
    console.log(arguments);  // 打印出所有的参数
    console.log('你好啊')
}

fn()  // 虽然原始的函数定义时有形参，但是再JS中可以不填
fn(1)  // 也可以填一个
fn(1, 2)  // 也可以正常填
fn(1, 2, 3, 4, 5, 6, 7, 8, 9)  // 也可以多填