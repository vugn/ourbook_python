import PySimpleGUI as sg

from controllers.auth_controller import AuthController


class LoginView:
    def __init__(self):
        self.auth_controller = AuthController()

    def login_window(self):
        layout = [
            [sg.Text('Username'), sg.Input(key='USERNAME')],
            [sg.Text('Password'), sg.Input(key='PASSWORD', password_char='*')],
            [sg.Button('Login'), sg.Button('Exit')]
        ]

        window = sg.Window('Login', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                window.close()
                return False  # Exiting the app
            elif event == 'Login':
                username = values['USERNAME']
                password = values['PASSWORD']
                
                # Authenticate
                if self.auth_controller.authenticate(username, password):
                    sg.popup('Login Successful!')
                    window.close()
                    return True  # Proceed to the main app
                else:
                    sg.popup('Login Failed. Invalid credentials!')
