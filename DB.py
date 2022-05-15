import pyodbc


class DataBase:

    def __init__(self):
        self.connection = pyodbc.connect('''Driver={ODBC Driver 17 for SQL Server};
                                            Server=localhost;
                                            Database=Sport;
                                            Trusted_Connection=yes;''')
        self.cursor = self.connection.cursor()

    def get_competitions(self):
        with self.connection:
            data_list = self.cursor.execute('''
            SELECT txtCompetitionName, datCompetitionDate,
            txtCompetitionTypeName, txtCompetitionPlace FROM tblCompetition, tblCompetitionType
            WHERE(tblCompetition.intCompetitionTypeId = tblCompetitionType.intCompetitionTypeId)
            ''').fetchall()
            for el in data_list:
                el[1] = el[1].strftime("%Y-%m-%d")
        return data_list

    def add_new_competition(self, name, date, typeId, place):
        with self.connection:
            self.cursor.execute('''
            INSERT INTO tblCompetition (txtCompetitionName, datCompetitionDate,
            intCompetitionTypeId, txtCompetitionPlace) VALUES (?, ?, ?, ?)
            ''', (name, date, typeId, place))

    def get_comps_type_and_id(self):
        with self.connection:
            return self.cursor.execute('''
            SELECT intCompetitionTypeId, txtCompetitionTypeName
            FROM tblCompetitionType
            ''').fetchall()

    def get_compId_by_name(self, name):
        with self.connection:
            return self.cursor.execute('''
            SELECT intCompetitionId FROM tblCompetition
            WHERE txtCompetitionName = ?
            ''', name).fetchone()

    def get_competition_info(self, compId):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtSportsmanName, txtSportsmanSurname, txtSportsmanSecondName,
            intPlace, fltMark, txtCommandName, fltCommandCiuntry
            FROM tblCommand, tblSportsman, tblParticipation
            WHERE (tblParticipation.intCompetitionId = ?) and
            (tblParticipation.intSportsmanId = tblSportsman.intSportsmanId) and
            (tblSportsman.intCommandId = tblCommand.intCommandId)
            ''', compId).fetchall()

    def get_sportsmen(self):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtSportsmanName, txtSportsmanSurname, txtSportsmanSecondName
            FROM tblSportsman
            ''').fetchall()

    def get_sportsman_id_by_name(self, name):
        with self.connection:
            return self.cursor.execute('''
            SELECT intSportsmanId FROM tblSportsman
            WHERE txtSportsmanName = ?
            ''', name).fetchone()

    def get_comp_id_by_name(self, name):
        with self.connection:
            return self.cursor.execute('''
            SELECT intCompetitionId FROM tblCompetition
            WHERE txtCompetitionName = ?
            ''', name).fetchone()

    def get_comp_type_by_name(self, name):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtCompetitionTypeName FROM tblCompetitionType, tblCompetition 
            WHERE tblCompetition.txtCompetitionName = ? and 
            tblCompetition.intCompetitionTypeId = tblCompetitionType.intCompetitionTypeId
            ''', name).fetchone()

    def add_sportsman_into_competition(self, compId, spId, place, mark):
        with self.connection:
            self.cursor.execute('''
            INSERT INTO tblParticipation (intCompetitionId, intSportsmanId, intPlace, fltMark) 
            VALUES(?, ?, ?, ?)
            ''', (compId, spId, place, mark))

    def get_comp_place_by_name(self, name):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtCompetitionPlace FROM tblCompetition  
            WHERE txtCompetitionName = ?
            ''', name).fetchone()

    def get_all_comp_names_and_ids(self):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtCompetitionName, intCompetitionId FROM tblCompetition
            ''').fetchall()

    def get_date_by_comp_id(self, compId):
        with self.connection:
            return self.cursor.execute('''
            SELECT datCompetitionDate FROM tblCompetition 
            WHERE intCompetitionId = ?
            ''', compId).fetchone()

    def get_comp_type_by_comp_id(self, compId):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtCompetitionTypeName FROM tblCompetition, tblCompetitionType
            WHERE tblCompetition.intCompetitionTypeId = tblCompetitionType.intCompetitionTypeId 
            and intCompetitionId = ?
            ''', compId).fetchone()

    def get_comp_place_by_id(self, compId):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtCompetitionPlace FROM tblCompetition  
            WHERE intCompetitionId = ?
            ''', compId).fetchone()

    def get_comp_info_for_report(self, compId):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtSportsmanName, txtSportsmanSurname, txtSportsmanSecondName, datBirthday,
            fltMark, intPlace FROM tblSportsman, tblParticipation, tblCompetition
            WHERE (tblParticipation.intCompetitionId = ?) and (tblCompetition.intCompetitionId = ?) 
            and (tblParticipation.intSportsmanId = tblSportsman.intSportsmanId)
            ''', compId, compId).fetchall()

    def get_number_of_participated_sp(self):
        with self.connection:
            return self.cursor.execute('''
            SELECT COUNT(DISTINCT intSportsmanId) FROM tblParticipation
            ''').fetchone()

    def get_average_for_comps(self):
        with self.connection:
            return self.cursor.execute('''
            SELECT AVG(fltMark) FROM tblParticipation
            ''').fetchone()

    def get_cmds_info_for_report(self):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtCommandName, fltCommandCiuntry,
            fltCommandSum, intCommandId FROM tblCommand
            ''').fetchall()

    def get_sps_by_team_id(self, t_id):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtSportsmanName, txtSportsmanSecondName,
            txtSportsmanSurname, intSportsmanNumber, datBirthday, intSportsmanId
            FROM tblCommand, tblSportsman
            WHERE tblSportsman.intCommandId = ? and 
            tblSportsman.intCommandId = tblCommand.intCommandId
            ''', t_id).fetchall()

    def get_comps_by_sp_id(self, sp_id):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtCompetitionName, datCompetitionDate, txtCompetitionTypeName
            FROM tblSportsman, tblParticipation, tblCompetition, tblCompetitionType 
            WHERE tblSportsman.intSportsmanId = tblParticipation.intSportsmanId
            and tblParticipation.intCompetitionId = tblCompetition.intCompetitionId
            and tblCompetition.intCompetitionTypeId = tblCompetitionType.intCompetitionTypeId
            and tblSportsman.intSportsmanId = ?
            ''', sp_id).fetchall()

    def get_sum_mark_for_team_by_id(self, t_id):
        with self.connection:
            return self.cursor.execute('''
            SELECT SUM(fltMark)
            FROM tblSportsman, tblParticipation 
            WHERE tblSportsman.intSportsmanId = tblParticipation.intSportsmanId and
            tblSportsman.intCommandId = ?
            ''', t_id).fetchone()

    def get_comp_type_name_and_decs_by_id(self, typeId):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtCompetitionTypeName, txtCompetitionTypeDescription
            FROM tblCompetitionType
            WHERE intCompetitionTypeId = ?
            ''', typeId).fetchone()

    def get_comp_info_for_team_report(self, typeId):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtCompetitionName, datCompetitionDate, intCompetitionId
            FROM tblCompetitionType, tblCompetition
            WHERE tblCompetitionType.intCompetitionTypeId = ? and
            tblCompetition.intCompetitionTypeId = tblCompetitionType.intCompetitionTypeId
            ''', typeId).fetchall()

    def get_sps_by_comp_id(self, compId):
        with self.connection:
            return self.cursor.execute('''
            SELECT txtSportsmanName, txtSportsmanSurname, txtSportsmanSecondName, datBirthday, intPlace
            FROM tblCompetition, tblParticipation, tblSportsman
            WHERE tblCompetition.intCompetitionId = ? and 
            tblCompetition.intCompetitionId = tblParticipation.intCompetitionId and
            tblSportsman.intSportsmanId = tblParticipation.intSportsmanId
            ORDER BY tblSportsman.datBirthday DESC
            ''', compId).fetchall()

    def get_comps_types_and_type_ids(self):
        with self.connection:
            return self.cursor.execute('''
            SELECT intCompetitionTypeId, txtCompetitionTypeName
            FROM tblCompetitionType
            ''').fetchall()
