// 在ES6之前要想写一个对象需要借助function
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

// 类和函数的最本质区别，在使用上类需要先初始化才能够使用类中的方法
let p1 = new Persion('lm', '18')
p1.eat('大米饭')


// 在ES6时是这样写，更像传统意义上的面向对象
class Student {
    // 初始化方法，类似于Python中的__init__
    constructor(name, classes) {
        this.name = name
        this.classes = classes
    }

    // 方法
    study(class_name) {
        console.log(this.classes + '的' + this.name + '，正在上《' + class_name + '》课程.')
    }
}

let s1 = new Student('zhangsan', '大数据1班')
s1.study('概率论')
