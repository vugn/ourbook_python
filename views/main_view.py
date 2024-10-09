import PySimpleGUI as sg

from views.book_view import BookView


class MainView:
    def __init__(self):
        self.book_view = BookView()

    def show_main_menu(self):
        layout = [
            [sg.Button("Manage Books"), sg.Button("Exit")]
        ]

        window = sg.Window("Library Management System", layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == "Manage Books":
                window.close()
                self.book_view.show_books()
        window.close()
