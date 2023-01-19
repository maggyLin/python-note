import pymysql.cursors
#使用pymysql指令來連接數據庫

connection=pymysql.connect(host="172.17.101.11",user="root",password="TERoot",db="nd2",charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        sql = "SELECT version()"
        cursor.execute(sql)
        #只取出一條結果
        result=cursor.fetchone()
        print(result)
#關閉連接
finally:
    print("finally")
    # connection.close()