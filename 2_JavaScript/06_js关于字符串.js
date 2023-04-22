var s = 'luoming zhen shuai!中国人';

// 字符串的切分
console.log(s.split(' '));
// 字符串的街区
console.log(s.substr(5, 5));  // 从哪开始切分，切分多长
console.log(s.substring(0, 9));  // 从哪开始切分，切到哪结束
console.log(s.slice(0, 9));  // 和substring类似
// 字符串长度
console.log(s.length);  //  len(s)
// 使用位置获取字符
console.log(s.charAt(2));  // s[i]
// 根据字符获取位置
console.log('----------------');
console.log(s.indexOf('h'));  // 9  获取h出现的第一个位置
console.log(s.lastIndexOf('h'));  // 14  获取h出现的最后一个位置
// 返回对应位置的字符对应的ASCII码,如果是中文则为Unicode编码
console.log(s.charCodeAt(2));  // ord(2)  111
console.log(s.charCodeAt(s.length - 3));  // 20013
// 将Unicode编码转化为文字,有时会用在字体加密
console.log(String.fromCharCode(20013));

// 小练习
var str = "callback_jsonp({'name': 'Luoming', 'age': 18, wife:{'name': '汪峰'}})"
// 获取上方的JSON具体内容
var start_index = str.indexOf('{')
var end_idnex = str.lastIndexOf('}')
console.log(str.slice(start_index, end_idnex + 1));

// 将所有小写字母转化为大写字母
console.log(str.toUpperCase());
// 将所有大学字母转化为小写字母
console.log(str.toLowerCase());
// 判断是否以xxx开头
console.log(str.startsWith('callback'));  // true

// null 与 undefined
// null 表示空
// undefined 表示变量为空，变量是有，但是未赋值
// null 和 undefined 都表示空，转化为boll都是false
