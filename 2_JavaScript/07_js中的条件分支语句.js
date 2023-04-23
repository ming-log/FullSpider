var a = 10

// if 语句
// 通过大括号界定代码块的范围
if (a > 50) {
    console.log(123)
} else {
    console.log(456)
}


// 如果只有一句话还可以省略大括号
if (a > 50)
    console.log(123)
else
    console.log(456)


// switch语句
a = 3
switch (a) {
    case 1:
        console.log('我是1')
    case 2:
        console.log('我是2')
    case 3:
        console.log('我是3')
    case 4:
        console.log('我是4')
    case 5:
        console.log('我是5')
    default:
        console.log('我不是1-5')
}
// 我是3
// 我是4
// 我是5
// 我不是1-5
// 当case3成立后，后续的所有语句都会直接执行，switch穿透现象


console.log('---------');
// 如果不需要switch穿透则在每个case后面都要加上break语句，打断后续的case
a = 3
switch (a) {
    case 1:
        console.log('我是1')
        break
    case 2:
        console.log('我是2')
        break
    case 3:
        console.log('我是3')
        break
    case 4:
        console.log('我是4')
        break
    case 5:
        console.log('我是5')
        break
    default:
        console.log('我不是1-5')
}
// 我是3

console.log('---------');
// switch穿透是有用的，例如：通过月份判断季度
var month = 5
switch (month) {
    case 1:
    case 2:
    case 3:
        console.log('第一季度')
        break
    case 4:
    case 5:
    case 6:
        console.log('第二季度')
        break
    case 7:
    case 8:
    case 9:
        console.log('第三季度')
        break
    case 10:
    case 11:
    case 12:
        console.log('第四季度')
        break
}
