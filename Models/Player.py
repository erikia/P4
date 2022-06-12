from Controllers import Connection
db = ('db.sqlite')


class Player:
    """Classe qui instancie les joueurs."""

    def __init__(self, name, first_name, date, gender, ranking, pairing_nb, score, opponents):
        """Retourne le joueur avec son nom, prénom, rang, numéro d'appariement et score."""
        self.p_table = Connection.db_players
        self.name = name
        self.first_name = first_name
        self.date = date
        self.gender = gender
        self.ranking = ranking
        self.pairing_nb = pairing_nb
        self.score = score
        self.opponents = opponents
        self.id = ''

    def save_players(self):
        return self.p_table.insert(self.get_serialized_player())

    def match_player(self):
        """Retourne les informations des joueurs"""
        match_player = [f"{self.name} {self.first_name} (Rang, Numéro associé, Score): ", (
            self.ranking), (self.pairing_nb), float(self.score)]

        return match_player

    def read_players_db(self):
        """Retourne la liste de tous les joueurs dans la base de donnée"""
        pass
