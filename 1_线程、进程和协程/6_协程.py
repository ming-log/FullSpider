import time
import asyncio


# await: 当该任务被挂起后, CPU会自动切换到其他任务中
async def func1():
    print("func1, start")
    await asyncio.sleep(3)
    print("func1, end")


async def func2():
    print("func2, start")
    await asyncio.sleep(4)
    print("func2, end")


async def func3():
    print("func3, start")
    await asyncio.sleep(2)
    print("func3, end")


async def run():
    start = time.time()
    tasks = [  # 协程任务列表
        asyncio.create_task(func1()),  # create_task创建协程任务
        asyncio.create_task(func2()),
        asyncio.create_task(func3()),
    ]
    await asyncio.wait(tasks)  # 等待所有任务执行结束
    print(time.time() - start)


if __name__ == '__main__':
    asyncio.run(run())
