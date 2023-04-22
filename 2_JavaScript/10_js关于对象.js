// 和Python中的字典非常类似，不过这里的key中的""是可以省略的
var wf = {
    "name": "汪峰",
    age: 18,
    wife: {
        name: "子怡",
        age: 22,
        news: "没新闻"
    }
}
console.log(wf['wife']['news'])
// 引用也可以写成这样,省略[]
console.log(wf.wife.news)
// 也就是说.xxx <==> ['xxx']，并且可以混用
console.log(wf.wife['news'])
console.log(wf['wife'].news)


// 那么将这种写法引入数组中，数组的插入也可以修改为以下形式
console.log('---------------------');
arr1 = [1, 2, 3, 4]
arr1.push(5)
arr1['push']('你好啊！')
console.log(arr1)  // [ 1, 2, 3, 4, 5, '你好啊！' ]


// 给对象添加属性
console.log('---------------------');
wf['child'] = []
wf.child['push']('儿子')
wf.sex = '男'
console.log(wf)
console.log('---------------------');
// 对象与JSON相互转化
// 对象 ==> JSON
console.log(typeof wf)  // object
wf_json = JSON.stringify(wf)
console.log(typeof wf_json)  // string
// JSON ==> 对象
wf_json_object = JSON.parse(wf_json)
console.log(typeof wf_json_object)  // object