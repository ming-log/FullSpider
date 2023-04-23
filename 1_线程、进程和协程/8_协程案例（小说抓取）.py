# 目标, 明朝那些事儿 http://www.mingchaonaxieshier.com/

import asyncio
import aiohttp
import aiofiles
import requests
from lxml import etree
import os


def get_chapter_info(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    page_source = resp.text
    resp.close()

    result = []

    # 解析page_soruce
    tree = etree.HTML(page_source)
    mulus = tree.xpath("//div[@class='main']/div[@class='bg']/div[@class='mulu']")
    for mulu in mulus:
        trs = mulu.xpath("./center/table/tr")
        title = trs[0].xpath(".//text()")
        chapter_name = "".join(title).strip()

        chapter_hrefs = []
        for tr in trs[1:]:  # 循环内容
            hrefs = tr.xpath("./td/a/@href")
            chapter_hrefs.extend(hrefs)

        result.append(
            {"chapter_name": chapter_name, "chapter_hrefs": chapter_hrefs}
        )

    return result


async def download_one(name, href):
    async with aiohttp.ClientSession() as session:
        async with session.get(href) as resp:
            hm = await resp.text(encoding="utf-8", errors="ignore")
            # 处理hm
            tree = etree.HTML(hm)
            title = tree.xpath("//div[@class='main']/h1/text()")[0].strip()
            content_list = tree.xpath("//div[@class='main']/div[@class='content']/p/text()")
            content = "\n".join(content_list).strip()
            async with aiofiles.open(f"../download_files/{name}/{title}.txt", mode="w", encoding="utf-8") as f:
                await f.write(content)

    print(title)


# 方案一
async def download_chapter(chapter):
    chapter_name = '../download_files/' + chapter['chapter_name']

    if not os.path.exists(chapter_name):
        os.makedirs(chapter_name)
    tasks = []
    for href in chapter['chapter_hrefs']:
        tasks.append(asyncio.create_task(download_one(chapter_name, href)))
    await asyncio.wait(tasks)


# 方案二
async def download_all(chapter_info):
    tasks = []
    for chapter in chapter_info:
        name = '../download_files/' + chapter['chapter_name']
        if not os.path.exists(name):
            os.makedirs(name)
        for url in chapter['chapter_hrefs']:
            task = asyncio.create_task(download_one(name, url))
            tasks.append(task)

    await asyncio.wait(tasks)


def main():
    url = "http://www.mingchaonaxieshier.com/"
    # 获取每一篇文章的名称和url地址
    chapter_info = get_chapter_info(url)

    # 可以分开写. 也可以合起来写.
    # 方案一，分开写:
    # for chapter in chapter_info:
    #     asyncio.run(download_chapter(chapter))

    # 方案e，合起来下载:
    asyncio.run(download_all(chapter_info))


if __name__ == '__main__':
    main()
