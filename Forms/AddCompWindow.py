import tkinter as tk
from tkinter import ttk
from DB import DataBase
from datetime import datetime


class AddCompWindow(tk.Tk):
    w, h = 350, 130

    db = DataBase()

    def add_new_comp(self):
        name = self.name_area.get()
        date = self.date_area.get()
        typeId = self.comp_types[self.type_combobox.get()]
        place = self.place_area.get()
        self.db.add_new_competition(
            name, datetime.strptime(date, '%Y-%m-%d'), typeId, place)
        self.destroy()

    def __init__(self):
        super().__init__()
        self.name_area = None
        self.title("Добавить соревнование")
        self.geometry("300x200")
        self.minsize(self.w, self.h)
        self.maxsize(self.w, self.h)

        name_label = tk.Label(self, text='Название соревнований: ')
        name_label.grid(row=0, column=0)
        self.name_area = tk.Entry(self)
        self.name_area.grid(row=0, column=1)

        date_label = tk.Label(self, text='Дата проведения (гггг-мм-дд)')
        date_label.grid(row=1, column=0)
        self.date_area = tk.Entry(self)
        self.date_area.grid(row=1, column=1)

        self.comp_types = dict()
        for i in self.db.get_comps_type_and_id():
            self.comp_types[i[1]] = i[0]

        type_label = tk.Label(self, text='Тип соревнований')
        type_label.grid(row=2, column=0)
        self.type_combobox = ttk.Combobox(
            self, values=[i for i in self.comp_types.keys()])

        self.type_combobox.grid(row=2, column=1)

        place_label = tk.Label(self, text='Место проведения')
        place_label.grid(row=3, column=0)
        self.place_area = tk.Entry(self)
        self.place_area.grid(row=3, column=1)

        add_button = tk.Button(self, text='Добавить соревнование')
        add_button.grid(row=4, column=0, columnspan=2)
        add_button.config(command=self.add_new_comp)
