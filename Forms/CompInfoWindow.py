import tkinter as tk
from tkinter import ttk
from DB import DataBase
from Forms.AddSportsmanToComp import AddSportsmanToComp


class CompInfoWindow(tk.Tk):
    w, h = 600, 300
    db = DataBase()

    def add_sportsman(self):
        _ = AddSportsmanToComp(self.comp_name).mainloop()

    def reload_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for line in self.db.get_competition_info(self.compId):
            post = (line[0] + ' ' + line[1] + ' ' + line[2],
                    line[3], line[4], line[5], line[6])
            self.tree.insert("", tk.END, values=list(post))

    def __init__(self, title, compId):
        super().__init__()
        self.comp_name = title
        self.compId = compId
        self.data = self.db.get_competition_info(compId)
        self.title(f"Состязания - {title}")
        self.geometry("600x300")
        self.minsize(self.w, self.h)
        self.maxsize(self.w, self.h)

        columns = ("#1", "#2", "#3", '#4', '#5')
        self.tree = ttk.Treeview(self, show="headings", columns=columns)
        self.tree.heading("#1", text="ФИО спортсмена")
        self.tree.column("#1", width=200)
        self.tree.heading("#2", text="Место")
        self.tree.column("#2", width=30, anchor=tk.CENTER)
        self.tree.heading("#3", text="Балл")
        self.tree.column("#3", width=50, anchor=tk.CENTER)
        self.tree.heading("#4", text="Название команды")
        self.tree.column("#4", width=120, anchor=tk.CENTER)
        self.tree.heading("#5", text="Страна")
        self.tree.column("#5", width=120, anchor=tk.CENTER)

        self.tree.grid(row=0, column=0)
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=1)
        for line in self.data:
            post = (line[0] + ' ' + line[1] + ' ' + line[2],
                    line[3], line[4], line[5], line[6])
            self.tree.insert("", tk.END, values=list(post))

        new_sportsman_btn = tk.Button(
            self, text='Новый участник соревнований', anchor=tk.CENTER)
        new_sportsman_btn.grid(row=1, column=0)
        new_sportsman_btn.config(command=self.add_sportsman)

        reload_data_but = tk.Button(self, text="Обновить")
        reload_data_but.grid(row=2, column=0)
        reload_data_but.config(command=self.reload_data)
