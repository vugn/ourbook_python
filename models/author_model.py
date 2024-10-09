from config.db_config import get_db_connection


class AuthorModel:
    def get_authors(self):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM pengarang")
            return cursor.fetchall()
