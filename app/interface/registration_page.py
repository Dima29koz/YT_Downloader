import tkinter as tk

from app.run import DBHandler
from functools import partial
from app.interface.state import State


class RegistrationPage:
    def __init__(self, canvas, db_h: DBHandler, set_state):
        self.canvas = canvas
        self.db_h = db_h
        self.set_state = set_state

    def draw(self):
        header_name = tk.Label(self.canvas, text="Регистрация:", font="Calibri 18")

        f1 = tk.Frame(self.canvas)
        email_lab = tk.Label(f1, text="Email:")
        email = tk.Entry(f1)
        login_lab = tk.Label(f1, text="Логин:")
        login = tk.Entry(f1)
        pass_lab = tk.Label(f1, text="Пароль:")
        password = tk.Entry(f1, show='*')
        error_message = tk.Label(f1, text="Wrong email or password", fg='Red')

        registration_button = tk.Button(self.canvas, text="Зарегистрироваться",
                                        command=partial(self._reg_btn, email, login, password, error_message))

        email_lab.grid(row=0, column=0, sticky='w')
        email.grid(row=0, column=1, columnspan=2)
        login_lab.grid(row=1, column=0, sticky='w')
        login.grid(row=1, column=1, columnspan=2)
        pass_lab.grid(row=2, column=0, sticky='w')
        password.grid(row=2, column=1, columnspan=2)
        error_message.grid(row=3, column=0, columnspan=3)
        error_message.grid_remove()

        header_name.pack()
        f1.pack()
        registration_button.pack()

    def _reg_btn(self, email_e: tk.Entry, login_e: tk.Entry, password_e: tk.Entry, error_message: tk.Label):
        email = email_e.get()
        # todo нет проверки что email is not in DB
        login = login_e.get()
        password = password_e.get()
        if email and login and password:
            if self.db_h.create_user(email, login, password):
                self.set_state(State.login_page)
            else:
                error_message.configure(text="Введенный адрес\nне является действительным")
                error_message.grid()
        else:
            error_message.configure(text="Все поля должны быть заполнены")
            error_message.grid()
