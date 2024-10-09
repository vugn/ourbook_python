import PySimpleGUI as sg

from views.book_view import BookView
from views.login_view import LoginView


class MainView:
    def __init__(self):
        self.book_view = BookView()
        self.login_view = LoginView()

    def show_main_menu(self):
        # Start with login
        if self.login_view.login_window():
            # If login is successful, show the main menu
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
