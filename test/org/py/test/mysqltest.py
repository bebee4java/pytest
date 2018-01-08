# -*- coding: UTF-8 -*-

# 先安装mysql模块：
# pip install pymysql

import pymysql.cursors

config = {
    'host': '10.8.132.227',
    'port': 3306,
    'user': 'root',
    'password': 'eastcom',
    'db': 'mysql',
    'charset': 'utf8'   # 注意是utf8不是utf-8
}
connection = pymysql.connect(**config)
try:
    with connection.cursor() as cursor:
        sql = 'select * from user'
        count = cursor.execute(sql)
        print("用户数量:"+str(count))
        print('{0:12}{1:10s}'.format('Host', 'User'))
        for row in cursor.fetchall():
            print('{0:12}{1:10s}'.format(str(row[0]), str(row[1])))
finally:
    connection.close()
