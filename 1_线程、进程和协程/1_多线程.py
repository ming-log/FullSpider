import threading


# 类似于同一个公司开设不同的部门
# 或者同一个部门有多个小组

def work():
    for i in range(1000):
        print(f"{threading.current_thread().name} Print: {i}")  # 打印当前线程名称


for i in range(10):
    t = threading.Thread(target=work, name=f"threadP{i}")  # 设置线程名称
    t.start()
