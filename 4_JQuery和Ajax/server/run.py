from flask import Flask
from flask import render_template, request, make_response

server = Flask("lm")


@server.route('/')
def index():
    a = {
        'name': '骆明',
        'sex': "男"
    }
    return render_template('index.html', a=a)  # 给HTML传输参数

@server.route('/haha')
def haha():
    # p = request.args.get('p')  # 获取url中对应的参数
    # return p

    # # 判断UA，这种方式可以校验请求头中的任何内容，例如加密参数token等等。
    # UA = request.headers['User-Agent']
    # if 'python' in UA.lower():
    #     return 'get out!'
    # return 'hello'

    # 校验cookie，如果想要返回cookie，用make_response创建一个返回对象
    s = make_response("i love you")
    s.set_cookie('lm', 'ddddddd')  # 在响应头中会自动加上'Set-Cookie: lm=ddddddd; Path=/'，下次请求浏览器就会自动加上cookie
    return s

@server.route('/hahahahaha', methods=['GET', 'POST'])  # 让该路由既接收GET请求又接收POST请求
def hahahaha():
    if request.method == 'POST':
        # print(request.form.get('dsg'))
        print(request.json.get('dsg'))
        return request.json.get('dsg')
    return "Jint adsadcsad"


if __name__ == '__main__':
    server.run(debug=True)
