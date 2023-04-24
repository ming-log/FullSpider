import requests


res = requests.get('http://127.0.0.1:5000/haha')
print(res.text)  # get out!  UA没有通过返回的是get out!

# 添加UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}
res2 = requests.get('http://127.0.0.1:5000/haha', headers=headers)
print(res2.text)  # hello  添加完UA后请求正常
