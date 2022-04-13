from tinydb import TinyDB
db = TinyDB('jtournament.json')


class Player:
    """Classe qui instancie les joueurs."""

    def __init__(self, name, first_name, date, gender, ranking, pairing_nb, score, opponents):
        """Retourne le joueur avec son nom, prénom, rang, numéro d'appariement et score."""
        self.p_table = db.table('Players')
        self.name = name
        self.first_name = first_name
        self.date = date
        self.gender = gender
        self.ranking = ranking
        self.pairing_nb = pairing_nb
        self.score = score
        self.opponents = opponents
        self.id = ''
        # name, first_name, date, gender, ranking, pairing_nb, score, opponents``

    def get_serialized_player(self):
        serialized_player = {
            "Nom": self.name,
            "Prénom": self.first_name,
            "Date de naissance": self.date,
            "Sexe": self.gender,
            "Rang": self.ranking,
            "Numéro associé": self.pairing_nb,
            "Score": self.score,
            "Adversaires": self.opponents
        }
        return serialized_player
    
    # def create_player(self):
    #     player_id = self.p_table.insert(
    #         {"Nom": self.name,
    #          "Prénom": self.first_name,
    #          "Date de naissance": self.date,
    #          "Sexe": self.gender,
    #          "Rang": self.ranking,
    #          "Numéro associé": self.pairing_nb,
    #          "Score": self.score,
    #          "Adversaires": self.opponents
    #          })
    #     return player_id
    #     # return self.p_table.update({'id': player_id}, doc_ids=[player_id])[0]

    def match_player(self):
        """Retourne les informations des joueurs"""
        match_player = [f"{self.name} {self.first_name} (Rang, Numéro associé, Score): ", (
            self.ranking), (self.pairing_nb), float(self.score)]

        return match_player

    def read_players(self):
        all_players = []
        players_from_db = self.p_table.all()
        for pl in players_from_db:
            player = Player.get_player_from_id(pl.doc_id)
            all_players.append(player)
        return all_players
