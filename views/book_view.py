import PySimpleGUI as sg

from controllers.book_controller import BookController


class BookView:
    def __init__(self):
        self.book_controller = BookController()

    def show_books(self):
        books = self.book_controller.get_all_books()
        book_data = [[book['kode_buku'], book['judul_buku'], book['harga']] for book in books]

        layout = [
            [sg.Table(values=book_data, headings=["Kode Buku", "Judul Buku", "Harga"], key="BOOK_TABLE")],
            [sg.Button("Add Book"), sg.Button("Delete Book"), sg.Button("Exit")]
        ]
        
        window = sg.Window("Book Management", layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Add Book':
                self.add_book_window()
            elif event == 'Delete Book':
                selected_row = values['BOOK_TABLE']
                if selected_row:
                    kode_buku = book_data[selected_row[0]][0]
                    self.book_controller.delete_book(kode_buku)
                    sg.popup("Book Deleted!")
                    window.close()
                    self.show_books()  # Refresh the list

        window.close()

    def add_book_window(self):
        layout = [
            [sg.Text("Kode Buku"), sg.Input(key="KODE_BUKU")],
            [sg.Text("Judul Buku"), sg.Input(key="JUDUL_BUKU")],
            [sg.Text("Harga"), sg.Input(key="HARGA")],
            [sg.Button("Save"), sg.Button("Cancel")]
        ]
        window = sg.Window("Add Book", layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            elif event == 'Save':
                book_data = (
                    values["KODE_BUKU"], 
                    values["JUDUL_BUKU"], 
                    "1", "1", "1", "2024", "Description", int(values["HARGA"])
                )
                self.book_controller.add_book(book_data)
                sg.popup("Book Added!")
                window.close()
        window.close()
