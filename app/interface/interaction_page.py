import re
import tkinter as tk
from tkinter.simpledialog import askstring
import tkinter.ttk as ttk
from functools import partial

from app.run import DBHandler


class InteractionPage:
    def __init__(self, canvas, db_h: DBHandler):
        self.canvas = canvas
        self.db_h = db_h
        self.menu = tk.Menu(self.canvas, tearoff=0)

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
        tr_table.bind("<<TreeviewSelect>>", partial(self.get_selection, tr_table))

        add_button = tk.Button(self.canvas, text="Добавить плейлист", command=self.on_click)

        tr_table.grid(row=0, column=0)
        ysb.grid(row=0, column=1, sticky=tk.N + tk.S)
        f1.rowconfigure(0, weight=1)
        f1.columnconfigure(0, weight=1)

        add_button.pack()
        f1.pack()

    @staticmethod
    def get_selection(event, tr_table):  # todo
        for selection in tr_table.selection():
            item = tr_table.item(selection)
            last_name, first_name, email = item["values"][0:3]
            text = "Выбор: {}, {} <{}>"
            print(text.format(last_name, first_name, email))

    def show_menu(self, e):
        self.menu.post(e.x_root, e.y_root)

    @staticmethod
    def on_update(tr_table, get_favorite):  # todo дюпает список
        tracks = get_favorite()
        if tracks:
            for track in tracks:
                tr_table.insert("", tk.END, values=track)

    def on_click(self):
        url = askstring('playlist url', 'Введите ссылку на плейлист')
        playlist_id = re.split(r'list=', re.sub(r'&fea[\S]*', '', url))[1]
        if playlist_id:
            self.db_h.add_playlist_to_db(playlist_id)
            # todo добавить добавление в избаранное
