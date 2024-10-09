from models.book_model import BookModel


class BookController:
    def __init__(self):
        self.book_model = BookModel()

    def get_all_books(self):
        return self.book_model.get_books()

    def add_book(self, book_data):
        self.book_model.add_book(book_data)

    def delete_book(self, kode_buku):
        self.book_model.delete_book(kode_buku)
