from json import JSONEncoder
import json
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
    
    # def get_players_list():
        players_list: list = []
        p1 = Player('Dubois', 'Charles', '05/04/1995', 'Homme', 356, 1, 0, [])
        p_json1 = json.dumps(p1, cls=PlayerEncoder, indent=4)
        p2 = Player('Alcor', 'David', '17/12/1945', 'Homme', 287, 2, 0, [])
        p_json2 = json.dumps(p2, cls=PlayerEncoder, indent=4)
        p3 = Player('Garry', 'Kasparov', '1/06/1967', 'Homme', 593, 3, 0, [])
        p_json3 = json.dumps(p3, cls=PlayerEncoder, indent=4)
        p4 = Player('Judit', 'Polgar', '1/06/1967','Femme', 407, 4, 0, [])
        p_json4 = json.dumps(p4, cls=PlayerEncoder, indent=4)
        p5 = Player('Fabiano', 'Caruana', '15/11/1978', 'Homme', 57, 5, 0, [])
        p_json5 = json.dumps(p5, cls=PlayerEncoder, indent=4)
        p6 = Player('Anish', 'Giri', '26/03/2000','Homme',68, 6, 0, [])
        p_json6 = json.dumps(p6, cls=PlayerEncoder, indent=4)
        p7 = Player('Boris', 'Spassky', '18/01/1935', 'Homme', 708, 7, 0, [])
        p_json7 = json.dumps(p7, cls=PlayerEncoder, indent=4)
        p8 = Player('Hikaru', 'Nakamura', '28/08/1985', 'Homme', 84, 8, 0, [])
        p_json8 = json.dumps(p8, cls=PlayerEncoder, indent=4)                
        players_list.append(p_json1)
        players_list.append(p_json2)
        players_list.append(p_json3)
        players_list.append(p_json4)
        players_list.append(p_json5)
        players_list.append(p_json6)
        players_list.append(p_json7)
        players_list.append(p_json8)
        jsons = json.dumps(players_list)
        
        return jsons

    def get_players_list():
        players_list: list = []

        p1 = Player('Dubois', 'Charles', '05/04/1995', 'Homme', 356, 1, 0, [])
        player1 = Player.get_serialized_player(p1)
        # player1 = json.dumps(p1, default=PlayersCtrl.encode_user)
        # player1 = json.dumps(p1,default=PlayersCtrl.encode_obj)
        p2 = Player('Alcor', 'David', '17/12/1945', 'Homme', 287, 2, 0, [])
        player2 = Player.get_serialized_player(p2)
        p3 = Player('Garry', 'Kasparov', '1/06/1967', 'Homme', 593, 3, 0, [])
        player3 = Player.get_serialized_player(p3)
        p4 = Player('Judit', 'Polgar', '1/06/1967','Femme', 407, 4, 0, [])
        player4 = Player.get_serialized_player(p4)
        p5 = Player('Fabiano', 'Caruana', '15/11/1978', 'Homme', 57, 5, 0, [])
        player5 = Player.get_serialized_player(p5)
        p6 = Player('Anish', 'Giri', '26/03/2000','Homme',68, 6, 0, [])
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
    
    # def encode_user(o):
    #     if isinstance(o, Player.Player):
    #         return {"Nom": o.name,
    #         "Prénom": o.first_name,
    #         "Date de naissance": o.date,
    #         "Sexe": o.gender,
    #         "Rang": o.ranking,
    #         "Numéro associé": o.pairing_nb,
    #         "Score": o.score,
    #         "Adversaires": o.opponents, o.__class__.__name__: True}
    #     else:
    #         raise TypeError(f"Object of type '{o.__class__.__name__}' is not JSON serializable")

    # def encode_obj(obj):
    
    #     obj_dict = {
    #     "__class__": obj.__class__.__name__,
    #     }
    
    #     obj_dict.update(obj.__dict__)
    
    #     return obj_dict


class PlayerEncoder(JSONEncoder):

    def default(self, o):

        if isinstance(o, Player):

            return {"Nom": o.name,
            "Prénom": o.first_name,
            "Date de naissance": o.date,
            "Sexe": o.gender,
            "Rang": o.ranking,
            "Numéro associé": o.pairing_nb,
            "Score": o.score,
            "Adversaires": o.opponents}

        else:
            # raise TypeError(f'Object of type {object.__class__.__name__} '
            #             f'is not JSON serializable')

            return super().default(o)

