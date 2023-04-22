var arr = ['张三', '李四', "王五", "王六"];
console.log(arr);
console.log(typeof arr);  // 数组是一个对象数据类型
console.log('---------------------');

var arr2 = new Array();  // 创建对象
// 在前端被new出来的东西都是对象object
console.log(typeof arr2);
console.log('---------------------');
var arr3 = new Array;  // 在前端创建对象时可以不写()
console.log(arr3)
console.log(typeof arr3)
console.log('---------------------');

// 定义空数组，然后往数组中追加元素
var arr4 = new Array();
arr4.push('a1');
arr4.push('a2');
arr4.push('a3');
arr4.push('a4');
arr4.push('a5');  // 类似于Python中append
console.log(arr4);  // [ 'a1', 'a2', 'a3', 'a4', 'a5' ]
console.log('---------------------');
// pop 弹出数组末尾元素
console.log(arr4.pop());  // a5
console.log(arr4);  // [ 'a1', 'a2', 'a3', 'a4' ]
// 数据结构中的栈结构  先进后出
console.log('---------------------');
var arr5 = [11, 22, 33, 44];
arr5.shift();  // 删除数组第一个元素
arr5.unshift(123);  // 数组第一个位置增加一个元素
console.log(arr5);
console.log('---------------------');
// 将嵌套数组修改为单层数组
var arr6 = [11, 22, [33, 44, 55, 66], 77, 88, [99, 100]];
arr6 = arr6.flat();
console.log(arr6);
// 切片
console.log('---------------------');
console.log(arr6);
var arr6_sp = arr6.slice(1, 4)
console.log(arr6_sp)
// 数组遍历
console.log('---------------------');
for (var i = 0; i < arr6_sp.length; i++) {
    console.log(arr6_sp[i])
}
console.log('---------------------');
for (var i in arr6_sp) {
    console.log(arr6_sp[i])
}
console.log('---------------------');
// 循环arr，拿到arr中的每一项，传递给function让其运行
// function可以有三个参数
// 1. 元素本身
// 2. 元素下标
// 3. 数组本身
arr6_sp.forEach(function (a, b, c) {
    console.log(a, b, c)
})
console.log('---------------------');
// 使用某个字符串连接数组中所有元素
var arr7 = [123, 456, 789]
console.log(arr7.join('|_|'))  // 等价于Python中'_'.join(arr7)
