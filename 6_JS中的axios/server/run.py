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

@server.route('/hahahahaha', methods=['GET'])
def haha():
    print("111111111111111111111111")
    return json.dumps({'name': 'lm', 'age': 18})

@server.route('/xixixixi', methods=['POST'])
def xixi():
    data = request.json.get('班级')  # axios请求和返回的数据均为json格式
    print("POST返回的数据：" + data)
    return json.dumps({'name': 'lm', 'age': 18})

if __name__ == '__main__':
    server.run(debug=True)
