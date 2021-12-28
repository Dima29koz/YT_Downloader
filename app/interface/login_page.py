import tkinter as tk

from app.db_interaction import DBHandler
from functools import partial
from app.interface.state import State


class LoginPage:
    def __init__(self, canvas, db_h: DBHandler, set_state):
        self.canvas = canvas
        self.db_h = db_h
        self.set_state = set_state
        self.email: str = ''

    def draw(self):
        header_name = tk.Label(self.canvas, text="Вход:", font="Calibri 18")

        f1 = tk.Frame(self.canvas)
        login_lab = tk.Label(f1, text="Логин/email:")
        login = tk.Entry(f1)
        pass_lab = tk.Label(f1, text="Пароль:")
        password = tk.Entry(f1, show='*')
        error_message = tk.Label(f1, text="Wrong email or password", fg='Red')

        f2 = tk.Frame(self.canvas)
        enter_button = tk.Button(f2, text="Войти", command=partial(self._enter_btn, login, password, error_message))
        registration_button = tk.Button(f2, text="Регистрация", command=self._reg_btn)

        login_lab.grid(row=0, column=0, sticky='w')
        login.grid(row=0, column=1, columnspan=2)
        pass_lab.grid(row=1, column=0, sticky='w')
        password.grid(row=1, column=1, columnspan=2)
        error_message.grid(row=2, column=0, columnspan=3)
        error_message.grid_remove()

        enter_button.grid(row=0, column=1, padx=5, pady=5)
        registration_button.grid(row=0, column=0, padx=5, pady=5)

        header_name.pack()
        f1.pack()
        f2.pack()

    def get_active_user(self):
        return self.email

    def _enter_btn(self, login_e: tk.Entry, password_e: tk.Entry, error_message: tk.Label):
        email = login_e.get()
        if self.db_h.validate_user(email, password_e.get()):
            self.email = email
            self.set_state(State.interaction_page, email)
        else:
            error_message.grid()

    def _reg_btn(self):
        self.set_state(State.registration_page)

