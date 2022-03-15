from tinydb import TinyDB
from Models import Player, Round


class Tournament:
    """Classe qui permet de sauvegarder les informations des tournois dans un fichier au format json"""

    def __init__(self) -> None:
        self.first_rounds = Round.pairing_first_round()
        self.other_rounds = Round.pairing_other_round()
        self.player = Player()

    def add_tournament_and_players(self, tournament_dict, players_list):
        """Combine les informations sur les tournois et les joueurs"""
        self.total_tournament = tournament_dict
        self.total_tournament["players"] = players_list
        return self.total_tournament

    def save_format_json(self, tournament_dict):
        """Sauvegarde les informations sur le tournoi et les joueurs en json"""
        jtournament = TinyDB("jtournament.json",
                             ensure_ascii=False, encoding="utf8", indent=4)
        tournament_table = jtournament.table("tournaments")
        tournament_table.insert(tournament_dict)
        return tournament_table
s
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

        players = tournament_table.get(doc_id=tournament_id)["players"]
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
