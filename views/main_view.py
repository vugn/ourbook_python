import PySimpleGUI as sg

from views.book_view import BookView
from views.category_view import CategoryView
from views.login_view import LoginView


class MainView:
    def __init__(self):
        self.book_view = BookView()
        self.category_view = CategoryView()
        self.login_view = LoginView()

    def show_main_menu(self):
        if self.login_view.login_window():
            layout = [
                [sg.Button("Manage Books"), sg.Button("Manage Categories"), sg.Button("Exit")]
            ]
            window = sg.Window("Library Management System", layout)
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    break
                elif event == "Manage Books":
                    window.close()
                    self.book_view.show_books()
                elif event == "Manage Categories":
                    window.close()
                    self.category_view.show_categories()
            window.close()
