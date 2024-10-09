from models.auth_model import AuthModel


class AuthController:
    def __init__(self):
        self.auth_model = AuthModel()

    def authenticate(self, username, password):
        return self.auth_model.login(username, password)
