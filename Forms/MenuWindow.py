import tkinter as tk
from tkinter import ttk
from DB import DataBase
from Forms.CompetitionsWindow import CompetitionsWindow
from Reports.CompetitionReport import CompetitionReport
from Reports.TeamsReport import TeamReport
from Reports.SportTypeReport import SportTypeReport


class MenuWindow(tk.Tk):
    w, h = 300, 200
    db = DataBase()

    @staticmethod
    def open_competitions_window():
        _ = CompetitionsWindow().mainloop()

    def make_comp_report(self):
        _ = CompetitionReport()
        self.status['text'] = 'Competitions report created in HTML_reports/'

    def make_teams_report(self):
        _ = TeamReport()
        self.status['text'] = 'Teams report created in HTML_reports/'

    def make_sport_type_report(self):
        try:
            _ = SportTypeReport(self.types[self.type_cmbx.get()], self.type_cmbx.get())
            self.status['text'] = f'SportType report for {self.type_cmbx.get()}\n created in HTML_reports/'
        except KeyError:
            self.status['text'] = 'Choose sport type'
            pass

    def __init__(self):
        super().__init__()
        self.title(f"Menu")
        self.geometry("300x200")
        self.minsize(self.w, self.h)
        self.maxsize(self.w, self.h)

        comps_types = self.db.get_comps_types_and_type_ids()
        self.types = dict()
        for i in comps_types:
            self.types[i[1]] = i[0]

        cmp_btn = tk.Button(self, text = 'Competitions', anchor = tk.CENTER)
        cmp_btn.pack(side = tk.TOP)
        cmp_btn.config(command = self.open_competitions_window)

        cmp_report_btn = tk.Button(self, text = 'Competitions Report', anchor = tk.CENTER)
        cmp_report_btn.pack(side = tk.TOP)
        cmp_report_btn.config(command = self.make_comp_report)

        teams_report = tk.Button(self, text = 'Teams Report', anchor = tk.CENTER)
        teams_report.pack(side = tk.TOP)
        teams_report.config(command = self.make_teams_report)

        self.type_cmbx = ttk.Combobox(self, values = [i for i in self.types.keys()])
        self.type_cmbx.pack(side = tk.TOP)

        type_report_btn = tk.Button(self, text = 'Type Report', anchor = tk.CENTER)
        type_report_btn.pack(side = tk.TOP)
        type_report_btn.config(command = self.make_sport_type_report)

        self.status = tk.Label(self)
        self.status.pack(side = tk.TOP)
