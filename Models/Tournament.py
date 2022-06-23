from Controllers import ApplicationCtrl, Connection
from Models import  Round
from Views import RoundView



class Tournament:
    """Classe qui permet de sauvegarder les informations des tournois dans un fichier au format json"""

    def __init__(self, name="", location="", date="", num_of_rounds=4, rounds=None, players=None,
                 time_control="", description=""):
        self.t_table = Connection.db_tournaments
        self.name = name
        self.location = location
        self.date = date
        self.num_of_rounds = num_of_rounds
        self.rounds = rounds
        self.players = Connection.db_players
        self.time_control = time_control
        self.description = description
        self.id = ''

    def create_tournament(self):
        """Retourne un dictionnaire du tournois"""
        self.rounds_ids = self.generate_rounds()
        self.t_table = (
            {"Adresse": self.location,
             "date": self.date,
             "num_of_rounds": self.num_of_rounds,
             "rounds": id(self.rounds),
             "players": id(self.players),
             "time_control": self.time_control,
             "description": self.description
             })
        return Tournament.save_format_sqlite(self.t_table)

    def generate_rounds(self):
        """Retoune une liste des rounds"""
        rounds = []

        for i in range(self.num_of_rounds):
            RoundView.RoundView.ask_start_round()
            r = Round.Round()
            r.generate_matches(self.players)
            create_rounds = r.create_round(i+ 1, self.players)
            rounds.append(create_rounds)
            RoundView.RoundView.ask_end_round()

        return rounds
    

    def save_format_sqlite(tournament_dict):
        """Sauvegarde les informations sur le tournoi et les joueurs en sqlite"""
        save_table = Connection.cursor.executemany(
            "INSERT OR IGNORE INTO tournaments (id, Adresse, Date, Totals_Rounds, Controle_du_temps, Rounds_en_cours, Rounds_id, Joueurs_id, Commentaire) VALUES( NULL, :Adresse, :date, :num_of_rounds, :time_control, NULL, :rounds, :players,  :description)", [tournament_dict])
        tournament_table = save_table.connection.commit()
        return tournament_table
