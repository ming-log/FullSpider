$(function (){

    function setCookie(name, value) {
    let Days = 30;
    let exp = new Date();
    exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
    document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
    }

    btn = $("#btn")
    btn.click(function (){
        console.log(123)
        // 访问服务器，加载数据
        // js里发送请求 -> ajax
        // $.get()   $.post()    发送get请求和post请求
        // 下面用的多
        // get请求
        // $.ajax({
        //     url: "/hahahahaha",
        //     method: 'get',
        //     // success: 访问成功之后自动回调该函数
        //     success: function (data){
        //         console.log(data)
        //     }
        // })

        // post请求
        $.ajax({
            url: "/hahahahaha",
            method: 'post',
            data: JSON.stringify({
                "dsg": "luoming"
            }),
            contentType: "application/json;charset=utf-8",  // 返回的类型设置为JSON，这个时候想要发送数据正常需要将数据作用在JSON.stringify()函数
            // success: 访问成功之后自动回调该函数
            success: function (data){
                console.log(data);
                // 把返回的内容写入cookie
                setCookie('lmlmlmlml', data)
            }
        })
    })
})
