import aiohttp
import asyncio
import aiofiles


async def download(url):
    try:
        name = url.split("/")[-1]
        # 创建session对象 -> 相当于requsts对象
        async with aiohttp.ClientSession() as session:
            # 发送请求, 这里和requests.get()几乎没区别, 除了代理换成了proxy
            async with session.get(url, ssl=False) as resp:  # 取消SSL验证
                # # resp.text(encoding='') 这可以设置字符集
                # 读取数据. 如果想要读取源代码. 直接resp.text()即可. 比原来多了个()
                content = await resp.content.read()
                # 写入文件, 用默认的open也OK. 用aiofiles能进一步提升效率
                async with aiofiles.open('../download_files/' + name, mode="wb") as f:
                    await f.write(content)
                    return "OK"
    except Exception as e:
        print(e)
        return "NO"


async def main():
    url_list = [
        "https://www.xiurenji.vip/uploadfile/202110/20/1F214426892.jpg",
        "https://www.xiurenji.vip/uploadfile/202110/20/91214426753.jpg"
    ]
    tasks = []

    for url in url_list:
        # 创建任务
        task = asyncio.create_task(download(url))
        tasks.append(task)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())  用这句话会报错RuntimeError: Event loop is closed
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
