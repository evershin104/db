from DB import DataBase
from datetime import datetime


class CompetitionReport:
    db = DataBase()

    def __init__(self):
        self.report = open("HTML_reports/comp_report.html", "w+")
        self.report.writelines(self.header)
        self.make_report()
        self.report.close()
        del self

    def make_report(self):
        for i in self.db.get_all_comp_names_and_ids():
            self.report.writelines(f'<p>Competition name: {i[0]}</p>\n')

            date = datetime.strftime(
                self.db.get_date_by_comp_id(i[1])[0], '%Y-%m-%d')
            self.report.writelines(f'<p>Date: {date}</p>\n')

            comp_type = self.db.get_comp_type_by_comp_id(i[1])[0]
            self.report.writelines(f'<p>Competition Type: {comp_type}</p>\n')

            place = self.db.get_comp_place_by_id(i[1])[0]
            self.report.writelines(f'<p>Place: {place}</p>\n')

            self.report.writelines(self.table_start)
            table_data = self.db.get_comp_info_for_report(i[1])

            if len(table_data) != 0:
                max_score = max([s[4] for s in table_data])
                min_score = min([s[4] for s in table_data])
            else:
                max_score = 0
                min_score = 0

            for j in table_data:
                if len(j) == 0:
                    continue
                self.report.writelines('\t\t<tr>\n')
                self.report.writelines(
                    f'\t\t\t<td>{j[0] + " " + j[1] + " " + j[2]}</td>\n')
                self.report.writelines(
                    f'\t\t\t<td>{datetime.strftime(j[3], "%Y-%m-%d")}</td>\n')
                self.report.writelines(f'\t\t\t<td>{j[4]}</td>\n')
                self.report.writelines(f'\t\t\t<td>{j[5]}</td>\n')
                self.report.writelines('\t\t</tr>\n')
            self.report.writelines('\t</tbody>\n</table>\n')

            self.report.writelines(
                f'<p>Number of Sportsmen: {len(table_data)}</p>\n')

            self.report.writelines(f'<p>Max score: {max_score}</p>\n')
            self.report.writelines(f'<p>Min score: {min_score}</p>\n')
            self.report.writelines('<hr>\n')
        self.report.writelines(
            f'<p>Average mark: {self.db.get_average_for_comps()[0]}</p>\n')

        self.report.writelines('<p>Overall number of participated sportsmen: '
                               f'{self.db.get_number_of_participated_sp()[0]}</p>\n')

        self.report.writelines('</body>\n</html>')

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
<h2>Competitions</h2>"""

    table_start = '''<table align="center" border="1" cellpadding="1" cellspacing="1" style="width:500px">
	<tbody>
		<tr>
			<td>Name</td>
			<td>Birthday</td>
			<td>Mark</td>
			<td>Place</td>
		</tr>'''
