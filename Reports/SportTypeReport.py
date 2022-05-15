from DB import DataBase
from datetime import datetime


class SportTypeReport:
    db = DataBase()

    def __init__(self, typeId, name):
        self.typeId = typeId
        self.report = open(f"HTML_reports/sport_type_{name}_report.html", "w+")
        self.report.writelines(self.header)
        self.make_report()
        self.report.writelines('</body>\n</html>')
        self.report.close()
        del self

    def make_report(self):
        name, desc = self.db.get_comp_type_name_and_decs_by_id(self.typeId)
        self.report.writelines(f'<h1>Sport type: {name}</h1>\n')
        self.report.writelines(f'<p>Description: {desc}</p>\n')
        self.report.writelines('<ol>\n')
        for comp in self.db.get_comp_info_for_team_report(self.typeId):
            self.report.writelines(f'\t<li>{comp[0]} '
                                   f'- {datetime.strftime(comp[1], "%Y-%m-%d")}\n')
            self.report.writelines(self.table_start)
            for sp in self.db.get_sps_by_comp_id(comp[2]):
                self.report.writelines(f'\t\t\t\t<tr>\n\t\t\t\t\t<td>{sp[0] + " " + sp[1] + " " + sp[2]}'
                                       f'</td>\n\t\t\t\t\t<td>{datetime.strftime(sp[3], "%Y-%m-%d")}'
                                       f'</td>\n\t\t\t\t\t<td>{sp[4]}</td>\n\t\t\t\t</tr>\n')
            self.report.writelines('\t\t\t</tbody>\n\t\t</table>\n')
            self.report.writelines('\t</li>\n\t<hr>\n')
        self.report.writelines('</ol>\n')

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
<body>\n"""

    table_start = """\t\t<table align="center" border="1" cellpadding="1" cellspacing="1" style="width:500px">
			<tbody>
				<tr>
					<td>Name</td>
					<td>Date</td>
					<td>Place</td>
				</tr>\n"""
