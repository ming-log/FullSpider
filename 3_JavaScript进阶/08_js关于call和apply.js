// JS中所有的函数名字（对象）都有call和apply

window = global;

function play_with(name) {
    // 在函数中this默认指的是window
    console.log(this.name + "在和" + name + '玩耍!')
}

window.name = '张三'
play_with('李四')  // 张三在和李四玩耍!
console.log('-------------------------')


//  call
function Persion(name, age) {
    // 给对象赋予一个初始化的值
    // this表示当前对象，类似于Python中的self
    this.name = name
    this.age = age

    // 给对象设置方法
    this.eat = function (food) {
        console.log(this.name + this.age + '岁，正在吃' + food + '！')
    }
}

let p1 = new Persion('lm', 18)

play_with.call(p1, '王麻子')  // lm在和王麻子玩耍!   p1.happy_with('王麻子'),这个时候函数中的this就是p1


console.log('-------------------------')
// 例如还可以这么用
let arr = [11, 22, 33]
Array.prototype.push.call(arr, 44)  // ==> arr.push(44)
arr.push.call(arr, 55)  // ==> arr.push(55)
console.log(arr)


//   apply
// 函数.call(对象, 参数1, 参数2, 参数3, 参数4)
// 对象.函数(参数1, 参数2, 参数3, 参数4)

// apply和call功能上一模一样
// 函数.apply(对象, [参数1, 参数2, 参数3, 参数4])
// 对象.函数(参数1, 参数2, 参数3, 参数4)
console.log('-------------------------')
arr.push.apply(arr, [66, 77, 88])
console.log(arr)

