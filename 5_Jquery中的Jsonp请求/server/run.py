import json

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

@server.route('/hahahahaha', methods=['POST'])
def haha():
    sth = request.form.get('dsg')
    print('form data:', sth)
    # 服务器端可不可以返回一段js代码
    cb = request.args.get('callback')
    return cb + "(" + json.dumps({'name': 'lm', 'age': 18}) + ")"

if __name__ == '__main__':
    server.run(debug=True)
