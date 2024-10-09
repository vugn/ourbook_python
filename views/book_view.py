import locale
import PySimpleGUI as sg
from controllers.book_controller import BookController

# Set locale to Indonesian for currency formatting
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

class BookView:
    def __init__(self):
        self.book_controller = BookController()

    def show_books(self):
        books = self.book_controller.get_all_books()
        book_data = [[book['kode_buku'], book['judul_buku'], book['kategori'], book['pengarang'], book['penerbit'], book['tahun'], book['deskripsi'], locale.currency(book['harga'], grouping=True)] for book in books]

        sg.theme('DarkBlue3')  # Set a theme for the window

        layout = [
            [sg.Text("Book Management System", size=(30, 1), justification="center", font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
            [sg.Table(values=book_data, headings=["Kode Buku", "Judul Buku", "Kategori", "Pengarang", "Penerbit", "Tahun Terbit", "Deskripsi", "Harga"], key="BOOK_TABLE", enable_events=True, auto_size_columns=False, col_widths=[10, 20, 15, 15, 15, 10, 30, 15], justification="center", alternating_row_color='blue')],
            [sg.Button("Add Book", size=(10, 1), font=("Helvetica", 12)), sg.Button("Delete Book", size=(10, 1), font=("Helvetica", 12)), sg.Button("Exit", size=(10, 1), font=("Helvetica", 12))]
        ]
        
        window = sg.Window("Book Management", layout, finalize=True)
        
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Add Book':
                self.add_book_window(window)
            elif event == 'Delete Book':
                selected_row = values['BOOK_TABLE']
                if selected_row:
                    kode_buku = book_data[selected_row[0]][0]
                    self.book_controller.delete_book(kode_buku)
                    sg.popup("Book Deleted!", font=("Helvetica", 12))
                    self.refresh_table(window)
        
        window.close()

    def add_book_window(self, parent_window):
        sg.theme('DarkBlue3')  # Set a theme for the window

        layout = [
            [sg.Text("Add New Book", size=(30, 1), justification="center", font=("Helvetica", 20), relief=sg.RELIEF_RIDGE)],
            [sg.Text("Kode Buku", size=(15, 1)), sg.Input(key="KODE_BUKU")],
            [sg.Text("Judul Buku", size=(15, 1)), sg.Input(key="JUDUL_BUKU")],
            [sg.Text("Kategori", size=(15, 1)), sg.Input(key="KATEGORI")],
            [sg.Text("Pengarang", size=(15, 1)), sg.Input(key="PENGARANG")],
            [sg.Text("Penerbit", size=(15, 1)), sg.Input(key="PENERBIT")],
            [sg.Text("Tahun Terbit", size=(15, 1)), sg.Input(key="TAHUN_TERBIT")],
            [sg.Text("Deskripsi", size=(15, 1)), sg.Input(key="DESKRIPSI")],
            [sg.Text("Harga", size=(15, 1)), sg.Input(key="HARGA")],
            [sg.Button("Save", size=(10, 1), font=("Helvetica", 12)), sg.Button("Cancel", size=(10, 1), font=("Helvetica", 12))]
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
                    values["KATEGORI"],
                    values["PENGARANG"],
                    values["PENERBIT"],
                    values["TAHUN_TERBIT"],
                    values["DESKRIPSI"],
                    int(values["HARGA"])
                )
                self.book_controller.add_book(book_data)
                sg.popup("Book Added!", font=("Helvetica", 12))
                self.refresh_table(parent_window)
                window.close()
        window.close()

    def refresh_table(self, window):
        books = self.book_controller.get_all_books()
        book_data = [[book['kode_buku'], book['judul_buku'], book['kategori'], book['pengarang'], book['penerbit'], book['tahun'], book['deskripsi'], locale.currency(book['harga'], grouping=True)] for book in books]
        window['BOOK_TABLE'].update(values=book_data)

if __name__ == "__main__":
    view = BookView()
    view.show_books()