from concurrent.futures.thread import ThreadPoolExecutor


def work(name):
    for i in range(10000):
        print(f'{name}:{i}')


with ThreadPoolExecutor(16) as t:  # 设置线程池，大小一般为CPU核心数的2倍，这里设置的最大线程数为16
    for i in range(4):
        t.submit(work, f'线程{i}')

