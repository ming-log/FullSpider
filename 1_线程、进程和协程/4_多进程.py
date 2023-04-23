from multiprocessing import Process


# 一个公司能创造的价值毕竟是有限的. 怎么办?
# 开分公司啊. 此所谓多进程. python实现多进程的方案和多线程几乎一样. 非常的简单
def func():
    for i in range(1000):
        print("func", i)


if __name__ == '__main__':
    p = Process(target=func)
    p.start()

    for i in range(1000):
        print("main", i)
