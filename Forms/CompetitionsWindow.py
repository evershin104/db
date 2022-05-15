import tkinter as tk
from tkinter import ttk
from DB import DataBase
from Forms.AddCompWindow import AddCompWindow
from Forms.CompInfoWindow import CompInfoWindow


def add_competition():
    _ = AddCompWindow().mainloop()


class CompetitionsWindow(tk.Tk):
    w, h = 600, 300
    db = DataBase()

    def reload_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for line in self.db.get_competitions():
            self.tree.insert("", tk.END, values=list(line))

    def __init__(self):
        super().__init__()
        self.title("Соревнования")
        self.geometry("600x300")
        self.minsize(self.w, self.h)
        self.maxsize(self.w, self.h)

        columns = ("#1", "#2", "#3", "#4")
        self.tree = ttk.Treeview(self, show="headings", columns=columns)
        self.tree.heading("#1", text="Соревнование")
        self.tree.column("#1", width=120)
        self.tree.heading("#2", text="Дата")
        self.tree.column("#2", width=80, anchor=tk.CENTER)
        self.tree.heading("#3", text="Наименование вида")
        self.tree.column("#3", width=120, anchor=tk.CENTER)
        self.tree.heading("#4", text="Место")
        self.tree.column("#4", width=120, anchor=tk.CENTER)

        self.tree.grid(row=0, column=0)
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=1)
        for line in self.db.get_competitions():
            self.tree.insert("", tk.END, values=list(line))
        self.tree.bind("<Double-1>", self.onDoubleClick)

        add_new_comp_button = tk.Button(self, text="Добавить соревнование")
        add_new_comp_button.grid(row=1, column=0)
        add_new_comp_button.config(command=add_competition)

        reload_data_but = tk.Button(self, text="Обновить")
        reload_data_but.grid(row=2, column=0)
        reload_data_but.config(command=self.reload_data)

    def onDoubleClick(self, event):
        selected = self.tree.item(self.tree.selection()[0], "values")[0]
        comp_id = self.db.get_compId_by_name(selected)[0]
        _ = CompInfoWindow(selected, comp_id)
        _.mainloop()
