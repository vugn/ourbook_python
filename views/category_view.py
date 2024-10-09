import PySimpleGUI as sg

from controllers.category_controller import CategoryController


class CategoryView:
    def __init__(self):
        self.category_controller = CategoryController()

    def show_categories(self):
        self.refresh_categories()

    def refresh_categories(self):
        categories = self.category_controller.get_categories()
        headings = ['Kode Kategori', 'Nama Kategori']
        data = [[cat['kode_kategori'], cat['nama_kategori']] for cat in categories]

        layout = [
            [sg.Table(values=data, headings=headings, key='CAT_TABLE', auto_size_columns=False,
                      col_widths=[15, 30], enable_events=True)],
            [sg.Button('Add Category'), sg.Button('Edit Category'), sg.Button('Delete Category')],
            [sg.Button('Back to Book Management'), sg.Button('Exit')]
        ]

        window = sg.Window('Manage Categories', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Add Category':
                self.add_category()
                window.close()
                self.refresh_categories()
            elif event == 'Edit Category':
                selected = values['CAT_TABLE']
                if selected:
                    self.edit_category(data[selected[0]][0], data[selected[0]][1])
                    window.close()
                    self.refresh_categories()
            elif event == 'Delete Category':
                selected = values['CAT_TABLE']
                if selected:
                    self.delete_category(data[selected[0]][0])
                    window.close()
                    self.refresh_categories()
            elif event == 'Back to Book Management':
                window.close()
                return 'book'  # Signal to switch to Book Management

        window.close()

    def add_category(self):
        layout = [
            [sg.Text('Kode Kategori'), sg.Input(key='KODE')],
            [sg.Text('Nama Kategori'), sg.Input(key='NAMA')],
            [sg.Button('Submit'), sg.Button('Cancel')]
        ]

        window = sg.Window('Add Category', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            elif event == 'Submit':
                kode = values['KODE']
                nama = values['NAMA']
                self.category_controller.add_category(kode, nama)
                sg.popup('Category added successfully!')
                break
        window.close()

    # Similarly, implement edit_category and delete_category
