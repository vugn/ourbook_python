from config.db_config import get_db_connection


class AuthModel:
    def login(self, username, password):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM admin WHERE username=%s AND password=MD5(%s)"
            cursor.execute(sql, (username, password))
            return cursor.fetchone()
