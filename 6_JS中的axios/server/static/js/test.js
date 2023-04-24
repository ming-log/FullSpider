
window.onload = function (){
    // axios拦截器 -> 在请求发送给服务器之前拦截下来，执行一段代码
    // axios拦截器 -> 响应返回后，运行一段代码
    // 给所有的请求添加功能，不仅GET请求变化了，POST请求也变化了  interceptors
    // 一般用于对请求地址进行加密
    axios.interceptors.request.use(function(request){
        let url = request.url;
        // 假装加密了
        url += "?abcd"
        request.url = url
        return request  // 把请求对象向后进行传递
    }, function (error){
        return Promise.reject(error)  // reject —> 自动运行后面的catch
    })

    // 一般用于对返回数据进行解密
    axios.interceptors.response.use(function (response){
        let data = response.data  // 拿到数据
        // 对数据进行解密
        data['age'] += 'aaaaa'
        response.data = data
        return response;
    }, function (error){
        return Promise.reject(error)
    })


    let btn1 = document.getElementById("btn1")
    btn1.addEventListener('click', function (){
        axios.get("/hahahahaha").then(function (resp){
            console.log(resp)  // 这里返回的响应对象，包括响应体、响应头、状态码、数据等等
            console.log(resp.data)  // 这里才是真正的数据
        })
    })

    let btn2 = document.getElementById("btn2")
    btn2.addEventListener('click', function (){
        axios.post("/xixixixi", {'班级': '大数据1', 'num': 32}).then(function (resp){  // axios.post(url, 数据)
            console.log(resp)  // 这里返回的响应对象，包括响应体、响应头、状态码、数据等等
            console.log(resp.data)  // 这里才是真正的数据
        })
    })


}
