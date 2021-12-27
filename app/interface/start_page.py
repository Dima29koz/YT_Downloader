import tkinter as tk
from PIL import Image, ImageTk
from functools import partial

from app.interface.state import State


class StartPage:
    def __init__(self, canvas, set_state):
        self.canvas = canvas
        self.set_state = set_state

    def draw(self):
        back = tk.Label(self.canvas, text="нажмите чтобы продолжить", font='Calibri 18')
        back.pack()
        back.bind("<Button-1>", self._click)

    def _click(self, event):
        self.set_state(State.login_page)
