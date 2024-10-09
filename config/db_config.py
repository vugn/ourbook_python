import pymysql


def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='bukukita',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
