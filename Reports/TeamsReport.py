from DB import DataBase
from datetime import datetime


class TeamReport:
    db = DataBase()

    def __init__(self):
        self.report = open("HTML_reports/teams_report.html", "w+")
        self.report.writelines(self.header)
        self.make_report()
        self.report.writelines('</body>\n</html>')
        self.report.close()
        del self

    def make_report(self):
        for c_info in self.db.get_cmds_info_for_report():
            self.report.writelines(f'<h2>Team name: {c_info[0]}</h2>\n')
            self.report.writelines(f'<p>Country: {c_info[1]}</p>\n')
            self.report.writelines(f'<p>Sum of marks: {c_info[2]}</p>\n')

            sportsmen_data = self.db.get_sps_by_team_id(c_info[3])
            for sp in sportsmen_data:
                self.report.writelines(f'<ol>\n\t<li>{sp[0] + " " + sp[1] + " " + sp[2]};'
                                       f' N{sp[3]}; Birthday: {datetime.strftime(sp[4], "%Y-%m-%d")}\n')

                sp_comps = self.db.get_comps_by_sp_id(sp[5])
                self.report.writelines(f'\t<ul>\n')
                for comp in sp_comps:
                    self.report.writelines(f'\t\t<li>{comp[0]} - '
                                           f'{datetime.strftime(comp[1], "%Y-%m-%d")} - {comp[2]}</li>\n')
                self.report.writelines('\t</ul>\n\t</li>\n</ol>\n')

                self.report.writelines(
                    f'<p>Number of competitions: {len(sp_comps)}</p>\n')
            self.report.writelines(
                f'<p>Team mark: {self.db.get_sum_mark_for_team_by_id(c_info[3])[0]}</p>\n')
            self.report.writelines('<hr>\n')

    header = """<!DOCTYPE html>
	<html>
	<head>
		<title>be1.ru</title>
		<style>
	    hr {
	        border: none;
	        background-color: black;
	        color: black;
	        height: 2px;
	        }
	    </style>
	</head>
	<body>
	<h1>Teams</h1>"""
