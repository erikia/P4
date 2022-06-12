from sqlite3 import connect
from Controllers import Connection
from Models import Player, Round
db = ('db.sqlite')


class Tournament:
    """Classe qui permet de sauvegarder les informations des tournois dans un fichier au format json"""

    def __init__(self, name="", location="", date="", num_of_rounds=4, rounds=None, players=None,
                 time_control="", description=""):
        # self.t_table = db('SELECT * FROM tournaments')
        self.t_table = Connection.db_tournaments
        self.name = name
        self.location = location
        self.date = date
        self.num_of_rounds = num_of_rounds
        self.rounds = rounds
        self.players = Player.Player.get_players_list()
        self.time_control = time_control
        self.description = description
        self.id = ''

    def generate_rounds(self):
        rounds = []
        for i in range(self.num_of_rounds):
            r = Round.Round()
            r.generate_matches(self.players)
            create_rounds = r.create_round(i+1, self.players)
            rounds.append(create_rounds)
        return rounds

    def add_tournament_and_players(self, tournament_dict, players_list):
        """Combine les informations sur les tournois et les joueurs"""
        self.total_tournament = tournament_dict
        self.total_tournament["Players"] = players_list
        return self.total_tournament

    def add_tournament_and_rounds(self, tournament_dict, rounds_list):
        """Combine les informations sur les tournois et les rounds"""
        self.total_tournament = tournament_dict
        self.total_tournament["Rounds"] = rounds_list
        return self.total_tournament

    def add_tournament_and_matchs(self, tournament_dict, matchs_list):
        """Combine les informations sur les tournois et les matchs"""
        self.total_tournament = tournament_dict
        self.total_tournament["Matchs"] = matchs_list
        return self.total_tournament

    def save_format_sqlite(self, tournament_dict):
        """Sauvegarde les informations sur le tournoi et les joueurs en sqlite"""
        # tournament_table = Connection.cursor.executemany("""UPDATE tournaments SET ? = :?
        #                 WHERE ?? = :?? AND ?? = :??""", tournament_dict)
        save_table = Connection.cursor.executemany(
            "INSERT OR IGNORE INTO tournaments VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?)", tournament_dict)
        tournament_table = save_table.connection.commit()
        return tournament_table

    def save_format_json(self, tournament_dict):
        """Sauvegarde les informations sur le tournoi et les joueurs en json"""
        jtournament = TinyDB("jtournament.json",
                             ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_table.insert(tournament_dict)
        return tournament_table
