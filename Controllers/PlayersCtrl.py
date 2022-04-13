import json
from operator import itemgetter
from Models import Player
from Views import PlayerView


class PlayersCtrl:
    """La classe qui appelle la vue avec les informations sur les joueurs"""

    def players_infos(self):
        """Retourne un dictionnaire des informations des joueurs avec la méthode create_players_input """

        players_input = PlayerView.PlayersView()
        self.players = players_input.create_players_input()
        return self.players

    def sort_player_by_pairing_numbers(players_input):
        """Trier les joueurs par leur numéro associé"""

        sorted_players = sorted(
            players_input, key=itemgetter("Numéro associé"))
        return sorted_players

    def sort_players_by_ranking(self):
        """Trier les joueurs par leurs rang"""

        sorted_players = sorted(
            self.players, key=lambda x: x.rank, reverse=True)
        return sorted_players
        
    def get_players_list():
        players_list: list = []

        p1 = Player.Player('Dubois', 'Charles', '05/04/1995', 'Homme', 356, 1, 0, [])
        player1 = Player.Player.get_serialized_player(p1)
        # player1 = json.dumps(p1, default=PlayersCtrl.encode_user)
        # player1 = json.dumps(p1,default=PlayersCtrl.encode_obj)
        p2 = Player.Player('Alcor', 'David', '17/12/1945', 'Homme', 287, 2, 0, [])
        player2 = Player.Player.get_serialized_player(p2)
        p3 = Player.Player('Garry', 'Kasparov', '1/06/1967', 'Homme', 593, 3, 0, [])
        player3 = Player.Player.get_serialized_player(p3)
        p4 = Player.Player('Judit', 'Polgar', '1/06/1967','Femme', 407, 4, 0, [])
        player4 = Player.Player.get_serialized_player(p4)
        p5 = Player.Player('Fabiano', 'Caruana', '15/11/1978', 'Homme', 57, 5, 0, [])
        player5 = Player.Player.get_serialized_player(p5)
        p6 = Player.Player('Anish', 'Giri', '26/03/2000','Homme',68, 6, 0, [])
        player6 = Player.Player.get_serialized_player(p6)
        p7 = Player.Player('Boris', 'Spassky', '18/01/1935', 'Homme', 708, 7, 0, [])
        player7 = Player.Player.get_serialized_player(p7)
        p8 = Player.Player('Hikaru', 'Nakamura', '28/08/1985', 'Homme', 84, 8, 0, [])
        player8 = Player.Player.get_serialized_player(p8)
        players_list.append(player1)
        players_list.append(player2)
        players_list.append(player3)
        players_list.append(player4)
        players_list.append(player5)
        players_list.append(player6)
        players_list.append(player7)
        players_list.append(player8)
        
        return players_list

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


        # player1 = {'Nom de famille': 'Dubois', 'Prénom': 'Charles', 'Date de naissance': '05/04/1995',
        #            'Sexe': 'Homme', 'Rang': 356, 'Numéro associé': 1, 'Score': 0, 'Adversaires': []}
        # player2 = {'Nom de famille': 'Alcor', 'Prénom': 'David', 'Date de naissance': '17/12/1945',
        #            'Sexe': 'Homme', 'Rang': 287, 'Numéro associé': 2, 'Score': 0, 'Adversaires': []}
        # player3 = {'Nom de famille': 'Garry', 'Prénom': 'Kasparov', 'Date de naissance': '1/06/1967',
        #            'Sexe': 'Homme', 'Rang': 593, 'Numéro associé': 3, 'Score': 0, 'Adversaires': []}
        # player4 = {'Nom de famille': 'Judit', 'Prénom': 'Polgar', 'Date de naissance': '1/06/1967',
        #            'Sexe': 'Femme', 'Rang': 407, 'Numéro associé': 4, 'Score': 0, 'Adversaires': []}
        # player5 = {'Nom de famille': 'Fabiano', 'Prénom': 'Caruana', 'Date de naissance': '15/11/1978',
        #            'Sexe': 'Homme', 'Rang': 579, 'Numéro associé': 5, 'Score': 0, 'Adversaires': []}
        # player6 = {'Nom de famille': 'Anish', 'Prénom': 'Giri', 'Date de naissance': '26/03/2000',
        #            'Sexe': 'Homme', 'Rang': 68, 'Numéro associé': 6, 'Score': 0, 'Adversaires': []}
        # player7 = {'Nom de famille': 'Boris', 'Prénom': 'Spassky', 'Date de naissance': '18/01/1935',
        #            'Sexe': 'Homme', 'Rang': 708, 'Numéro associé': 7, 'Score': 0, 'Adversaires': []}
        # player8 = {'Nom de famille': 'Hikaru', 'Prénom': 'Nakamura', 'Date de naissance': '28/08/1985',
        #            'Sexe': 'Homme', 'Rang': 84, 'Numéro associé': 8, 'Score': 0, 'Adversaires': []}