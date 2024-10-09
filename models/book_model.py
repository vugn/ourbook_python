from config.db_config import get_db_connection


class BookModel:
    def get_books(self):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM master_buku")
            return cursor.fetchall()
    
    def add_book(self, book_data):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            sql = """INSERT INTO master_buku (kode_buku, judul_buku, kategori, pengarang, penerbit, tahun, deskripsi, harga) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, book_data)
        conn.commit()

    def delete_book(self, kode_buku):
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM master_buku WHERE kode_buku=%s", (kode_buku,))
        conn.commit()
