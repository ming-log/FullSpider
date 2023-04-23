function Persion(name, age){
    // 给对象赋予一个初始化的值
    // this表示当前对象，类似于Python中的self
    this.name = name
    this.age = age

    // 给对象设置方法
    this.eat = function (food){
        console.log(this.name + this.age + '岁，正在吃' + food + '！')
    }
}

// 给Person的对象，增加一个新的功能，但是无法覆写属性和方法
// 例如给Persion对象增加一个睡觉功能
Persion.prototype.sleep = function (){
    console.log(this.name + '正在睡觉!')
}

// 类和函数的最本质区别，在使用上类需要先初始化才能够使用类中的方法
let p1 = new Persion('lm', '18')
p1.eat('大米饭')
p1.sleep()


