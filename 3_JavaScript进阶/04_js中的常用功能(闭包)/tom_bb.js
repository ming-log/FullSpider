(function (w){
    var key = 'AESAESAESAESAES'  // 加上变量生命的关键字,限制其作用域为本函数
    // 例如这里写AES加密算法
    function AES_jiami(data){
        console.log('AES:KEY-' + key + '加密' + data);
    }
    w['AES_jiami_bb'] = AES_jiami
})(window)