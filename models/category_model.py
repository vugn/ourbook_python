from config.db_config import get_db_connection


class CategoryModel:
    def get_all_categories(self):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM kategori")
            return cursor.fetchall()

    def add_category(self, kode_kategori, nama_kategori):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "INSERT INTO kategori (kode_kategori, nama_kategori) VALUES (%s, %s)"
            cursor.execute(sql, (kode_kategori, nama_kategori))
            conn.commit()

    def edit_category(self, kode_kategori, nama_kategori):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "UPDATE kategori SET nama_kategori = %s WHERE kode_kategori = %s"
            cursor.execute(sql, (nama_kategori, kode_kategori))
            conn.commit()

    def delete_category(self, kode_kategori):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = "DELETE FROM kategori WHERE kode_kategori = %s"
            cursor.execute(sql, (kode_kategori,))
            conn.commit()
