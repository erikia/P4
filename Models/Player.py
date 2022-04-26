from json import JSONEncoder
import jsonpickle
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

    def create_player(self):
        player = {
            "Nom": self.name,
            "Prénom": self.first_name,
            "Date de naissance": self.date,
            "Sexe": self.gender,
            "Rang": self.ranking,
            "Numéro associé": self.pairing_nb,
            "Score": self.score,
            "Adversaires": self.opponents
        }
        return player

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

    def save_players(self):
        return self.p_table.insert(self.get_serialized_player())

    def get_players_list():
        players_list: list = []

        p1 = Player('Dubois', 'Charles', '05/04/1995', 'Homme', 356, 1, 0, [])
        player1 = Player.get_serialized_player(p1)
        p2 = Player('Alcor', 'David', '17/12/1945', 'Homme', 287, 2, 0, [])
        player2 = Player.get_serialized_player(p2)
        p3 = Player('Garry', 'Kasparov', '1/06/1967', 'Homme', 593, 3, 0, [])
        player3 = Player.get_serialized_player(p3)
        p4 = Player('Judit', 'Polgar', '1/06/1967', 'Femme', 407, 4, 0, [])
        player4 = Player.get_serialized_player(p4)
        p5 = Player('Fabiano', 'Caruana', '15/11/1978', 'Homme', 57, 5, 0, [])
        player5 = Player.get_serialized_player(p5)
        p6 = Player('Anish', 'Giri', '26/03/2000', 'Homme', 68, 6, 0, [])
        player6 = Player.get_serialized_player(p6)
        p7 = Player('Boris', 'Spassky', '18/01/1935', 'Homme', 708, 7, 0, [])
        player7 = Player.get_serialized_player(p7)
        p8 = Player('Hikaru', 'Nakamura', '28/08/1985', 'Homme', 84, 8, 0, [])
        player8 = Player.get_serialized_player(p8)

        players_list.append(player1)
        players_list.append(player2)
        players_list.append(player3)
        players_list.append(player4)
        players_list.append(player5)
        players_list.append(player6)
        players_list.append(player7)
        players_list.append(player8)
        return players_list

    # def get_players_list():
        players_list: list = []

        player1 = Player('Dubois', 'Charles', '05/04/1995',
                         'Homme', 356, 1, 0, [])
        player2 = Player('Alcor', 'David', '17/12/1945',
                         'Homme', 287, 2, 0, [])
        player3 = Player('Garry', 'Kasparov', '1/06/1967',
                         'Homme', 593, 3, 0, [])
        player4 = Player('Judit', 'Polgar', '1/06/1967',
                         'Femme', 407, 4, 0, [])
        player5 = Player('Fabiano', 'Caruana', '15/11/1978',
                         'Homme', 57, 5, 0, [])
        player6 = Player('Anish', 'Giri', '26/03/2000', 'Homme', 68, 6, 0, [])
        player7 = Player('Boris', 'Spassky', '18/01/1935',
                         'Homme', 708, 7, 0, [])
        player8 = Player('Hikaru', 'Nakamura', '28/08/1985',
                         'Homme', 84, 8, 0, [])
        players_list.append(player1)
        players_list.append(player2)
        players_list.append(player3)
        players_list.append(player4)
        players_list.append(player5)
        players_list.append(player6)
        players_list.append(player7)
        players_list.append(player8)
        return players_list


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
