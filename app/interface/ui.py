import tkinter as tk

from app.run import DBHandler
from app.interface.login_page import LoginPage
from app.interface.registration_page import RegistrationPage
from app.interface.interaction_page import InteractionPage
from app.interface.start_page import StartPage
from app.interface.state import State


class UI:
    def __init__(self, db_h: DBHandler):
        self.db_h = db_h
        self.window = tk.Tk()
        self.window.title('Music analyzer')
        self.window.geometry('600x400+200+100')
        self.state = State.start_page

        self.tmp_frame = tk.Frame(self.window)
        self.login_frame = tk.Frame(self.window)
        self.registration_page = tk.Frame(self.window)
        self.interaction_page = tk.Frame(self.window)

        self.user_email: str = ''
        self.main()
        self.window.mainloop()

    def main(self):

        StartPage(self.tmp_frame, self.set_state).draw()

        self.tmp_frame.pack(expand=1)

        LoginPage(self.login_frame, self.db_h, self.set_state).draw()
        RegistrationPage(self.registration_page, self.db_h, self.set_state).draw()
        InteractionPage(self.interaction_page, self.db_h).draw(self.get_favorite)

    @staticmethod
    def draw_page(canvas_old, canvas_new):
        canvas_old.pack_forget()
        canvas_new.pack(expand=1)

    def set_state(self, state: State, email=None):
        if email:
            self.user_email = email
        page_to_state = {
            State.start_page: self.tmp_frame,
            State.registration_page: self.registration_page,
            State.login_page: self.login_frame,
            State.interaction_page: self.interaction_page
        }
        old_state = self.state
        self.state = state
        self.draw_page(page_to_state[old_state], page_to_state[self.state])

    def get_favorite(self):
        return self.db_h.get_favorite(self.user_email)



