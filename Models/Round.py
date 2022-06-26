from Controllers import Connection
from datetime import datetime
from Models import Match


class Round:
    """Class qui instancie les rounds"""

    def __init__(self, matches=None, name="", start_time="", date_time_end=""):
        self.r_table = Connection.db_rounds
        self.matches = matches
        self.name = name
        self.start_time = start_time
        self.date_time_end = date_time_end
        self.id = ""

    def create_round(self, round_num, players):
        """Retourne un dictionnaire du round"""
        self.name = "Rounds " + (str(round_num))
        self.matches = self.generate_matches(players)
        self.start_time = self.date_time_now()
        self.date_time_end = self.date_time_now()
        self.r_table = {
            "Matches": id(self.matches),
            "Nom": self.name,
            "Debut": self.start_time,
            "Fin": self.date_time_end,
        }
        return Round.save_rounds(self.r_table)

    def save_rounds(rounds):
        """Sauvegarde les rounds dans la base de donnée sqlite"""
        save_table = Connection.cursor.executemany(
            "INSERT OR IGNORE INTO rounds"
            "(id, matches_id, nom, debut_du_match, fin_du_match)"
            "VALUES( NULL, :Matches, :Nom, :Debut, :Fin)",
            [rounds],
        )
        match_table = save_table.connection.commit()
        return match_table

    def generate_matches(self, players):
        """Retourne les matchs dans une liste"""
        matches = []
        match = self.pairing_players_and_get_result(players)
        matches.append(match)
        return matches

    def pairing_players_and_get_result(self, players):
        """Retourne les résultats des matchs pour les mettre dans une liste"""
        matchs_list = []

        match_1 = Match.Match(players[0], players[1])
        match_2 = Match.Match(players[2], players[3])
        match_3 = Match.Match(players[4], players[5])
        match_4 = Match.Match(players[6], players[7])

        # Retourn les scores pour ensuite les sauvegarder
        m1 = match_1.return_match_result()
        m2 = match_2.return_match_result()
        m3 = match_3.return_match_result()
        m4 = match_4.return_match_result()

        matchs_list.append(m1)
        matchs_list.append(m2)
        matchs_list.append(m3)
        matchs_list.append(m4)

        return matchs_list

    def date_time_now(self):
        """Retourne la date et l'heure des matchs"""
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def finish_round(self):
        """Retourne la date et l'heure de l'arrêt des rounds"""
        self.date_time_end = self.date_time_now()

    def start_round(self):
        """Retourne la date et l'heure du début des rounds"""
        self.date_time_start = self.date_time_now()
