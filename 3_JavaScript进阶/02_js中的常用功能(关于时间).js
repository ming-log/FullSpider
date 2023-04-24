// 前端格式化时间
function get_fmt_datetime(t) {

    let year = t.getFullYear()
    // console.log(year)

    let month = t.getMonth() + 1
    // console.log(month)  // 默认月份从0开始

    let day = t.getDate()
    // console.log(day)

    let hour = t.getHours()
    // console.log(hour)

    let minute = t.getMinutes()
    // console.log(minute)

    let second = t.getSeconds()
    // console.log(second)

    let fmt_time = year + '-' + month + '-' + day + ' ' + hour + ':' + minute + ':' + second
    return fmt_time
}

// setInterval(get_fmt_datetime, 1000)

// 时间戳
// http://www.baidu.com/s?t=1682218629406
// 在编程的世界里，可以用一个数字来描述时间点
// 从1970-01-01 00:00:00开始，每过1秒，计数1000
let d = new Date()
console.log(d.getTime())  // 1682218629406 这里的时间单位为毫秒，Python中的时间戳为秒
console.log(get_fmt_datetime(d))
console.log(d.setTime(1682218629406))  // 设置时间
console.log(get_fmt_datetime(d))
