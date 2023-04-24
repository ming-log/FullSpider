$(function (){

    btn = $("#btn")
    btn.click(function (){

        // post请求
        $.ajax({
            url: "/hahahahaha",
            method: 'post',
            data: {
                "dsg": "luoming"
            },
            dataType: "jsonp",  // 加上这个东西，请求就变成了jsonp
            // 在抓包中能看到url的后面加上了
            // callback: jQuery1910972389350186351_1682333941137
            // 在console中没有打印内容，也就是success没有执行
            // 当响应回来之后，注意，jsonp不会自动的去执行success
            // 它会去执行callback中对应的jQuery1910972389350186351_1682333941137函数
            // 把data参数传输到了jQuery1910972389350186351_1682333941137(data)
            // jQuery1910972389350186351_1682333941137(data)函数调用的是success函数
            // 这样的一个好处是可以解决跨域问题
            success: function (data){
                console.log(data);  // 默认情况下拿不到数据
            }
        })
    })
})
