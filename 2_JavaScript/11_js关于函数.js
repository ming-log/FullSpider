window = global;

// 定义函数
function fn() {
    console.log('hello world!');
};
// 调用函数
fn();
console.log('---------------------');

function add(a, b) {
    return a + b
}

var c = add(1, 3)
console.log(c)
console.log('---------------------');

// 注意$和_就是普通字符
function $() {
    console.log('我是一个$符号')
}

$()

function _() {
    console.log('我是一个_符号')
}

_()
console.log('---------------------');
// 将匿名函数定义在数组中，使用数组调用
var arr = [
    function () {
        console.log('111111111111')
    },
    function () {
        console.log('222222222222')
    },
    function () {
        console.log('333333333333')
    },
]
// 调用
arr[1]()
// 循环数组调用所有函数
for (var i in arr) {
    arr[i]()
}
console.log('---------------------');

// 定义匿名函数直接运行
(function () {
    console.log('匿名函数');
})();// 自运行函数

// 加上形参
(function (a) {
    console.log('匿名函数' + a);
})(123213);// 自运行函数

// 加上返回值
var rtn = (function (a) {
    console.log('匿名函数' + a)
    return '返回值+++' + a
})(123213);// 自运行函数
console.log(rtn);

// 使用全局作用域window,可以不定义变量名直接使用
(function () {
    window.lm_name = 'luoming';
})();// 自运行函数
console.log(window.lm_name);

// 关于对象的补充
console.log('---------------------');
wf = {
    name: 'wangfeng',
    hobbit: 'songs',
    songs: ['怒放的生命', '春天里', '次哦啊是'],
    eat: function () {
        console.log(this.name + '吃饭')
        this.drink('旺仔牛奶')
    },
    drink: function (name) {
        console.log(this.name + '喝' + name)
    }
}
wf.eat()

// JS中不存在多个返回值
console.log('---------------------');

function fn() {
    // 当出现多个返回值时，只返回最后一项
    return 'A', 'B', 'C', 'D'
}

console.log(fn())

// 如果需要全部返回则使用[]括起来
function fn2() {
    // 当出现多个返回值时，只返回最后一项
    return ['A', 'B', 'C', 'D']
}

console.log(fn2())

