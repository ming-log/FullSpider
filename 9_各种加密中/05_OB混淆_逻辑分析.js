var webDES = function () {
    var func = function (a, b, c) {
        if (0 == b)
            return a['substr'](c);
        var result;
        result = '' + a['substr'](0, b);
        result += a['substr'](b + c);
        return result
    };
    this['shell'] = function (a) {
        // 获取a的最后一个字符将其转化为10进制数值+9赋值为b
        var b = parseInt(a[a['length'] - 1], 16) + 9
        // 将a的b位置的字符转化为10进制赋值为c
        var c = parseInt(a[b], 16);

        // 运行函数获得新值赋值给a
        a = func(a, b, 1);

        // 对新值进行切片，从c位置开始切片获取8个值赋值给b
        b = a['substr'](c, 8);
        // 再次调用函数获取新值赋值给a
        a = func(a, c, 8);

        c = _grsa_JS['enc']['Utf8']['parse'](b);  // 将b转化使用UTF-8编码方式转化为字节赋值给c
        b = _grsa_JS['enc']['Utf8']['parse'](b);  // 将b转化使用UTF-8编码方式转化为字节赋值给b
        b = _grsa_JS['DES']['decrypt']({
                    'ciphertext': _grsa_JS['enc']['Hex']['parse'](a)  // 将a使用16进制编码方式转化为字节
                }, c, {
                    'iv': b,  // 解密密钥，由于是ECB编码这里b和c其实是一样的，在Python中不用写iv。
                    'mode': _grsa_JS['mode']['ECB'],  // 解密方法
                    'padding': _grsa_JS['pad']['Pkcs7']  // 填充
                })['toString'](_grsa_JS['enc']['Utf8']);  // 转化为UTF-8格式
        return b['substring'](0, b['lastIndexOf']('}') + 1);  // 删除多余的结果，将}后面的字符都删除
    };
}