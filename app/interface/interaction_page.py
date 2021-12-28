import re
import tkinter as tk
from tkinter.simpledialog import askstring
import tkinter.ttk as ttk
from functools import partial

from app.db_interaction import DBHandler


class InteractionPage:
    def __init__(self, canvas, db_h: DBHandler, get_active_user):
        self.canvas = canvas
        self.db_h = db_h
        self.user_email = get_active_user
        self.menu = tk.Menu(self.canvas, tearoff=0)
        self.tracks = []

    def draw(self, get_favorite):
        columns = ("#1", "#2", "#3")
        f1 = tk.Frame(self.canvas)
        tr_table = ttk.Treeview(f1, show='headings', columns=columns)
        tr_table.heading("#1", text='Название')
        tr_table.heading("#2", text='Альбом')
        tr_table.heading("#3", text='Исполнитель')
        ysb = ttk.Scrollbar(f1, orient=tk.VERTICAL, command=tr_table.yview)
        tr_table.configure(yscroll=ysb.set)

        self.menu.add_command(label="Обновить", command=partial(self.on_update, tr_table, get_favorite))
        tr_table.bind("<Button-3>", self.show_menu)
        # tr_table.bind("<<TreeviewSelect>>", partial(self.get_selection, tr_table))

        add_button = tk.Button(self.canvas, text="Добавить плейлист", command=self.on_click)

        tr_table.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        f1.rowconfigure(0, weight=1)
        f1.columnconfigure(0, weight=1)

        add_button.pack()
        f1.pack()

    # @staticmethod
    # def get_selection(event, tr_table):  # todo
    #     for selection in tr_table.selection():
    #         item = tr_table.item(selection)
    #         last_name, first_name, email = item["values"][0:3]
    #         text = "Выбор: {}, {} <{}>"
    #         print(text.format(last_name, first_name, email))

    def show_menu(self, e):
        self.menu.post(e.x_root, e.y_root)

    def on_update(self, tr_table: ttk.Treeview, get_favorite):
        tracks = get_favorite()
        if tracks:
            for track in [track for track in tracks if track not in self.tracks]:

                tr_table.insert("", tk.END, values=track)
        self.tracks = tracks

    def on_click(self):
        # todo добавить статус добавления
        url = askstring('playlist url', 'Введите ссылку на плейлист')
        playlist_id = re.split(r'list=', re.sub(r'&fea[\S]*', '', url))[1]
        if playlist_id:
            self.db_h.add_playlist_to_db(playlist_id, self.user_email())
