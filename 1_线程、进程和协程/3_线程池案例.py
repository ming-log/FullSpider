# 1994年到2021年电影票房
# 目标网址：http://www.boxofficecn.com/boxofficecn
# 抓取目标：1994年到2022年的电影票房
# 抓取下来并存储到数据库
import threading

import requests
import pymysql
from concurrent.futures.thread import ThreadPoolExecutor
from queue import Queue
from lxml import etree
import pandas as pd

def work(q: Queue, cursor, lock):
    """
    获取并解析数据
    :param year: 指定年份
    :return: None 直接将数据存储到数据库中
    """
    try:
        while q.qsize():
            year = q.get()
            # 删除表
            delectTable_sql = f"""DROP TABLE IF EXISTS `year{year}`;"""
            with lock:
                cursor.execute(delectTable_sql)
            print(delectTable_sql)
            # 创建表
            createTable_sql = f"""
            CREATE TABLE `year{year}`  (
              `ID` int(0) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '计数变量',
              `index` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '序号',
              `year` int NULL DEFAULT NULL COMMENT '上映年份',
              `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '电影名称',
              `num`  varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '票房',
              PRIMARY KEY (`ID`) USING BTREE
            ) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;
            """
            with lock:
                cursor.execute(createTable_sql)
            print(f'CREATE TABLE `YEAR{year}`')

            # 爬取数据
            url = f"http://www.boxofficecn.com/boxoffice" + str(year)

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
            }
            # 获取数据
            response = requests.get(url, headers)
            # 解析数据
            html = etree.HTML(response.text)
            all_data = html.xpath("//table")[0]
            # 解析表格
            table = etree.tostring(all_data, encoding='utf-8').decode()
            df = pd.read_html(table, encoding='utf-8', header=0)[0]
            df.dropna(inplace=True)
            # 将票房修改为str
            results = list(df.T.to_dict().values())
            for i in results:
                values = list(i.values())
                print(f'{year}:', values)
                # 存储数据
                sql = f"insert into `year{year}` VALUES (null, '{values[0]}', {values[1]}, '{values[2]}', '{values[3]}');"
                with lock:
                    cursor.execute(sql)
                    conn.commit()
    except Exception as e:
        print(e)


def set_work():
    """
    设置任务
    :return: queue 包含任务的队列
    """
    q = Queue()
    for year in range(1994, 2024):
        q.put(year)
    print('*'*20)
    print(f"成功添加{q.qsize()}个任务")
    print('*'*20)
    return q




if __name__ == '__main__':
    # 连接数据库
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           database="boxofficecn",
                           user='root',
                           password='123456')
    q = set_work()  # 分配任务
    lock = threading.Lock()  # 创建线程锁，防止多个线程同时插入数据库
    cursor = conn.cursor()
    # 线程池
    with ThreadPoolExecutor(16) as t:  # 设置最大16线程
        for i in range(8):  # 开启8线程
            t.submit(work, q, cursor, lock)
    cursor.close()
    conn.close()
