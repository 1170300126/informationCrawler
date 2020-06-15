import pymysql
from os import path

def sqltotxt():
    conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='5539431',
        db='crawler',
        charset='utf8mb4'
    )

    # 获取游标
    cursor = conn.cursor()
    sql = 'select userLevel FROM crawlerdata'
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        fw = open(path.join(path.dirname(__file__), 'level.txt'), 'w', encoding='utf-8')
        for row in results:
            fw.write(row[0] + '\n')
            # print(row[0])
        print("level写入成功\n")
    except:
        print("Error: unable to fecth data")
    fw.close()
    sql = 'select userMessage FROM crawlerdata'
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        fm = open(path.join(path.dirname(__file__), 'message.txt'), 'w', encoding='utf-8')
        for row in results:
            fm.write(row[0] + '\n')
            # print(row[0])
        print("message写入成功\n")
    except:
        print("Error: unable to fecth data")

    # 关闭数据库连接
    conn.close()
    fm.close()