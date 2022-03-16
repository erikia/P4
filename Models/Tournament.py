from tinydb import TinyDB
from Models import Player, Round
from tinydb import TinyDB
db = TinyDB('jtournament.json')


class Tournament:
    """Classe qui permet de sauvegarder les informations des tournois dans un fichier au format json"""

    def __init__(self, name="", location="", date="", num_of_rounds=4, rounds=None, players=None,
                 time_control="", description=""):
        self.t_table = db.table('tournaments')
        self.name = name
        self.location = location
        self.date = date
        self.num_of_rounds = num_of_rounds
        self.rounds = rounds
        self.players = players
        self.time_control = time_control
        self.description = description
        self.id = ''

    def create_tournament(self):
        self.rounds_ids = self.generate_rounds()
        tournament_id = self.t_table.insert(
            {"Nom/ID du tournois": self.name,
             "Adresse du tournois": self.location,
             "Les dates du tournois": self.date,
             "Nombre total de rounds": self.num_of_rounds,
             "Rounds": self.rounds_ids,
             "Players": self.players,
             "Contrôle du temps": self.time_control,
             "Commentaire": self.description
             })
        return self.t_table.update(
            {'id': tournament_id}, doc_ids=[tournament_id])[0]

    def generate_rounds(self):
        rounds_ids = []
        for i in range(self.num_of_rounds):
            r = Round.Round()
            r.generate_matches()
            round_id = r.create_round(i+1)
            rounds_ids.append(round_id)
        return rounds_ids

    def add_tournament_and_players(self, tournament_dict, players_list):
        """Combine les informations sur les tournois et les joueurs"""
        self.total_tournament = tournament_dict
        self.total_tournament["Players"] = players_list
        return self.total_tournament

    def save_format_json(self, tournament_dict):
        """Sauvegarde les informations sur le tournoi et les joueurs en json"""
        jtournament = TinyDB("jtournament.json",
                             ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_table.insert(tournament_dict)
        return tournament_table

    def get_round_number(self, tournament_number):
        """Retourne le numéro du round actuel d'un tournoi avec le numéro d'entrée en json(id du tournoi)"""
        jtournament = TinyDB("jtournament.json",
                             ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_id = None

        if tournament_number == 0:
            tournament_id = len(tournament_table)
        else:
            tournament_id = tournament_number

        round_number = tournament_table.get(doc_id=tournament_id)[
            "Nombre du round en cours"]
        return round_number

    def get_length_db(self):
        """Retourne le numéro d'entrée dans la base de données json"""
        jtournament = TinyDB("jtournament.json",
                             ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        database_length = len(tournament_table)
        return database_length

    def get_players(self, tournament_number):
        """Retourne tous les joueurs d'un tournoi par son identifiant"""
        jtournament = TinyDB("jtournament.json",
                             ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_id = None

        if tournament_number == 0:
            tournament_id = len(tournament_table)
        else:
            tournament_id = tournament_number

        players = tournament_table.get(doc_id=tournament_id)["Players"]
        return players

    def get_total_tournaments(self):
        """Récupére tous les tournois enregistrés dans la base de données json"""
        jtournament = TinyDB("jtournament.json",
                             ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        total_table = tournament_table.all()
        all_tournaments = []

        for tournament in total_table:
            one_tournament = {}
            one_tournament["ID"] = tournament.doc_id
            one_tournament["Nom"] = tournament["Nom/ID du tournois"]
            one_tournament["Date"] = tournament["Les dates du tournois"]
            one_tournament["Adresse"] = tournament["Adresse du tournois"]
            all_tournaments.append(one_tournament)

        return all_tournaments
