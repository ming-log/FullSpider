(function (w){
    var key = 'MD5MD5MD5MD5MD5'  // 加上变量生命的关键字,限制其作用域为本函数
    // 例如这里写MD5加密算法
    function MD5_jiami(data){
        console.log('MD5:KEY-' + key + '加密' + data);
    }
    w['MD5_jiami_bb'] = MD5_jiami
})(window)