import tkinter as tk
from tkinter import ttk
from DB import DataBase
from datetime import datetime


class AddSportsmanToComp(tk.Tk):
    w, h = 400, 220

    db = DataBase()

    def add_sportsman(self):
        sp_id = self.db.get_sportsman_id_by_name(
            self.sportsman_cmbx.get().split(' ')[0])[0]
        comp_id = self.db.get_comp_id_by_name(self.comp)[0]
        place = int(self.sportsman_place_area.get())
        mark = self.score_slider.get()
        self.db.add_sportsman_into_competition(
            comp_id, sp_id, place, int(mark))
        self.destroy()

    def __init__(self, comp):
        super().__init__()
        self.comp = comp
        self.title(f"Новый участник - {comp}")
        self.geometry("300x200")
        self.minsize(self.w, self.h)
        self.maxsize(self.w, self.h)

        # Disabled elements
        name_label = tk.Label(self, text='Наименование соревнований: ')
        name_label.grid(row=0, column=0)
        self.name_area = tk.Entry(self, state='disabled')
        self.name_area.grid(row=0, column=1)
        dis_name = tk.Label(self.name_area, text=comp)
        dis_name.grid(row=0, column=0)

        date_label = tk.Label(self, text='Дата проведения: ')
        date_label.grid(row=1, column=0)
        self.date_area = tk.Entry(self, state='disabled')
        self.date_area.grid(row=1, column=1)
        dis_date = tk.Label(self.date_area, text=datetime.strftime(
            datetime.now(), '%Y-%m-%d'))
        dis_date.grid(row=0, column=0)

        place_label = tk.Label(self, text='Место проведения: ')
        place_label.grid(row=2, column=0)
        self.place_area = tk.Entry(self, state='disabled')
        self.place_area.grid(row=2, column=1)
        dis_place = tk.Label(
            self.place_area, text=self.db.get_comp_place_by_name(comp)[0])
        dis_place.grid(row=0, column=0)

        type_label = tk.Label(self, text='Наименование вида спорта: ')
        type_label.grid(row=3, column=0)
        self.type_area = tk.Entry(self, state='disabled')
        self.type_area.grid(row=3, column=1)
        dis_type = tk.Label(
            self.type_area, text=self.db.get_comp_type_by_name(comp)[0])
        dis_type.grid(row=0, column=0)

        # Enabled elements
        sportsman_label = tk.Label(self, text='Спортсмен: ')
        sportsman_label.grid(row=4, column=0)
        sportsmen = [i[0] + ' ' + i[1] + ' ' + i[2]
                     for i in self.db.get_sportsmen()]
        self.sportsman_cmbx = ttk.Combobox(self, values=sportsmen)
        self.sportsman_cmbx.grid(row=4, column=1)

        sportsman_place_label = tk.Label(self, text='Место: ')
        sportsman_place_label.grid(row=5, column=0)
        self.sportsman_place_area = tk.Entry(self)
        self.sportsman_place_area.grid(row=5, column=1)

        score_label = tk.Label(self, text='Балл: ')
        score_label.grid(row=6, column=0)
        self.score_slider = tk.Scale(
            self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.score_slider.grid(row=6, column=1)

        add_sportsman_btn = tk.Button(
            self, text='Добавить', anchor=tk.CENTER, width=20)
        add_sportsman_btn.grid(row=7, columnspan=2)
        add_sportsman_btn.config(command=self.add_sportsman)
