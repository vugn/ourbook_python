from models.category_model import CategoryModel


class CategoryController:
    def __init__(self):
        self.category_model = CategoryModel()

    def get_categories(self):
        return self.category_model.get_all_categories()

    def add_category(self, kode_kategori, nama_kategori):
        self.category_model.add_category(kode_kategori, nama_kategori)

    def edit_category(self, kode_kategori, nama_kategori):
        self.category_model.edit_category(kode_kategori, nama_kategori)

    def delete_category(self, kode_kategori):
        self.category_model.delete_category(kode_kategori)
