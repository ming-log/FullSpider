"""
由于网吧电影网站已经关闭，经过查询将案例目标修改为6v电影  https://www.66s.cc/
1. 获取m3u8文件地址
2. 根据m3u8文件，获取所有分段视频
3. 观察视频是否经过加密，如果经过加密则需要进行解密
4. 合并所有解密视频
"""
import asyncio

import aiofiles
import aiohttp
import requests
from lxml import etree
import re
import os

from Crypto.Cipher import AES  # pip install pycryptodome

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

def get_m3u8_url(url: str):
    """
    这里m3u8地址有多种情况
    1. iframe直接链接到m3u8文件
    2. 通过一个中间包
    3. 通过两个中间包
    """
    res = requests.get(url, headers=headers)
    res_html = etree.HTML(res.text)
    # 获取电影名称
    video_name = res_html.xpath('//title/text()')[0].split('-')[0].strip()
    # 获取iframe地址
    iframe_url = str(res_html.xpath('//iframe/@src')[0])
    # iframe直接链接到m3u8文件
    if iframe_url.endswith('m3u8'):
        return iframe_url, video_name
    # 通过一个中间包，获取m3u8文件地址
    iframe_res = requests.get(iframe_url, headers=headers)
    m3u8_url = re.findall("url: '(.*?)',", iframe_res.text, re.S)
    if len(m3u8_url) == 0:
        m3u8_url = iframe_url.rsplit('/', maxsplit=2)[0] + re.findall('"url":"(.*?)"', iframe_res.text, re.S)[0]
    else:
        m3u8_url = m3u8_url[0]
    # print(m3u8_url)
    return m3u8_url, video_name


def makedir_video(video_name: str):
    if not os.path.exists(video_name):
        os.mkdir(video_name)


def get_videos_url(video_name, m3u8_url: str):
    res = requests.get(m3u8_url, headers=headers)
    # 保存m3u8文件
    m3u8_filename = m3u8_url.split(r'/')[-1]
    with open(os.path.join(video_name, m3u8_filename), 'w', encoding='GBK') as f:
        f.write(res.text)
    all_videos_url = []
    for i in res.text.strip().split('\n'):
        # 判断视频是否加密，如果加密则将秘钥存储下来文件名为：enc.key，如果未加密则不存储任何文件
        if 'AES' in i and 'KEY' in i:
            key_uri = re.findall('URI="(.*?)"', i)[0]
            if "http" not in key_uri:
                key_uri = r'/'.join(m3u8_url.split(r'/')[:-1]) + '/' + key_uri
            key = requests.get(key_uri, headers=headers).content
            with open(os.path.join(video_name, 'enc.key'), 'wb') as f:
                f.write(key)
        if i.startswith('#') or len(i) == 0:
            continue
        all_videos_url.append(i)
        # print(all_videos_url)
    return all_videos_url


async def download_video(filepath, video_url, sem):
    async with sem:  # 使用信号量控制访问频率
        for i in range(10):
            try:
                video_name = video_url.split(r'/')[-1]
                async with aiohttp.ClientSession() as session:
                    async with session.get(video_url, headers=headers, timeout=10) as res:
                        content = await res.content.read()
                        async with aiofiles.open(os.path.join(filepath, video_name), 'wb') as f:
                            await f.write(content)
                break
            except Exception as e:
                if i == 9:
                    with open(filepath+'_Error.txt', 'a', encoding='utf-8') as f:
                        f.write(video_url+'\n')
                        print(f'----- {video_name}下载失败，请求次数达到上限（{i+1}次），已写入文件{filepath+"_Error.txt"} -----')
                    break
                print(f'----- {video_name}下载失败，正在重试{i} -----')
                print(e)

async def download_all_videos(sem_num, filepath, all_videos_url):
    # 信号量, 用来控制协程的并发量
    sem = asyncio.Semaphore(sem_num)  # 极个别电影需要控制在5左右
    tasks = []
    for video_url in all_videos_url:
        tasks.append(asyncio.create_task(download_video(filepath, video_url, sem)))
    await asyncio.wait(tasks)

async def parse_video(video_file, video_name, new_video_name, key):
    print(os.path.join(video_name, video_file))
    print(os.path.join(new_video_name, video_file))
    async with aiofiles.open(os.path.join(video_name, video_file), 'rb') as f1, aiofiles.open(os.path.join(new_video_name, video_file), 'wb') as f2:
        content = await f1.read()
        aes = AES.new(key=key, mode=AES.MODE_CBC, IV=b'0000000000000000')
        new_content = aes.decrypt(content)
        await f2.write(new_content)
        print(f'------ {video_file}解密成功 ------')

async def parse_all_videos(video_name):
    all_file = os.listdir(video_name)
    new_video_name = video_name + '_parse'
    if 'enc.key' in all_file:
        video_files = [i for i in all_file if i.endswith('ts')]
        makedir_video(new_video_name)
        print('------ 开始解密视频 ------')
        # 读取秘钥
        with open(os.path.join(video_name, 'enc.key'), 'rb') as f:
            key = f.read()
        # 创建协程任务
        tasks = []
        for video_file in video_files:
            tasks.append(asyncio.create_task(parse_video(video_file, video_name, new_video_name, key)))
        await asyncio.wait(tasks)
        print('------ 视频解密完成 ------')
    else:
        os.rename(video_name, new_video_name)
        print('------ 视频无加密 ------')

def merge(video_name):
    new_video_name = video_name + '_parse'
    # 读取m3u8文件，获取文件正确顺序
    m3u8_file = [i for i in os.listdir(video_name) if i.endswith('m3u8')][0]
    with open(os.path.join(video_name, m3u8_file)) as f:
        video_sort = [i.split('/')[-1].strip() for i in f.readlines() if not i.startswith("#") and len(i) > 0]
    n = 1
    # 切换工作目录
    os.chdir(new_video_name)
    tmp = []
    for i in range(len(video_sort)):
        tmp.append(video_sort[i])
        if i != 0 and i % 20 == 0:
            # 每20个视频合并一次
            cmd = f"copy /b {'+'.join(tmp)} {n}_copy.ts"
            os.system(cmd)
            tmp = []  # 新列表
            n = n + 1
    # 有剩余时将剩下的也合并完
    cmd = f"copy /b {'+'.join(tmp)} {n}_copy.ts"
    os.system(cmd)
    n = n + 1

    # 第二次大合并  1_copy.ts + 2_copy.ts + 3_copy.ts xxx.mp4
    last_temp = []
    for i in range(1, n):
        last_temp.append(f"{i}_copy.ts")
    # 最后一次合并
    cmd = f"copy /b {'+'.join(last_temp)} {video_name}.mp4"
    os.system(cmd)

if __name__ == '__main__':
    url = 'https://www.66s.cc/e/DownSys/play/?classid=4&id=20778&pathid1=0&bf=0'  # 66v电影网视频地址
    # 获取m3u8地址和电影名称
    # get_m3u8_url(url)
    m3u8_url, video_name = get_m3u8_url(url)
    # 创建电影名称文件夹
    makedir_video(video_name)
    # 根据m3u8地址，获取所有的视频地址，并判断是否加密
    all_videos = get_videos_url(video_name, m3u8_url)
    # 根据视频地址下载视频
    sem_num = 1000  # 用于控制并发量
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(download_all_videos(sem_num, video_name, all_videos))
    # 解密所有视频
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(parse_all_videos(video_name))
    # 合并视频
    # windows 自带合成命令: copy /b a.ts+b.ts full.mp4
    # linux/mac 命令: cat a.ts b.ts c.ts > xxx.mp4
    merge(video_name)
