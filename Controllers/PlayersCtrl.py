from operator import itemgetter
from Models import Player
from Views import PlayerView


class PlayersCtrl:
    """La classe qui appelle la vue avec les informations sur les joueurs"""

    # def __init__(self) -> None:
    # self.players = PlayersCtrl.get_players_list()

    def players_list():
        players_list: list = []
        # player["Nom de famille", "Prénom",
        #         "Date de naissance", "Sexe", "Rang"]
        # player = Player(database.get('Nom de famille'), database.get('Prénom'), database.get(
        #     'gender'), database.get('Date de naissance'), database.get('ranking'))

        player1 = {'Nom de famille': 'Dubois', 'Prénom': 'Charles', 'Date de naissance': '05/04/1995',
                   'Sexe': 'Homme', 'Rang': 356, 'Numéro associé': 1, 'Score': 0, 'Adversaires': []}
        player2 = {'Nom de famille': 'Alcor', 'Prénom': 'David', 'Date de naissance': '17/12/1945',
                   'Sexe': 'Homme', 'Rang': 287, 'Numéro associé': 2, 'Score': 0, 'Adversaires': []}
        player3 = {'Nom de famille': 'Garry', 'Prénom': 'Kasparov', 'Date de naissance': '1/06/1967',
                   'Sexe': 'Homme', 'Rang': 593, 'Numéro associé': 3, 'Score': 0, 'Adversaires': []}
        player4 = {'Nom de famille': 'Judit', 'Prénom': 'Polgar', 'Date de naissance': '1/06/1967',
                   'Sexe': 'Femme', 'Rang': 407, 'Numéro associé': 4, 'Score': 0, 'Adversaires': []}
        player5 = {'Nom de famille': 'Fabiano', 'Prénom': 'Caruana', 'Date de naissance': '15/11/1978',
                   'Sexe': 'Homme', 'Rang': 579, 'Numéro associé': 5, 'Score': 0, 'Adversaires': []}
        player6 = {'Nom de famille': 'Anish', 'Prénom': 'Giri', 'Date de naissance': '26/03/2000',
                   'Sexe': 'Homme', 'Rang': 68, 'Numéro associé': 6, 'Score': 0, 'Adversaires': []}
        player7 = {'Nom de famille': 'Boris', 'Prénom': 'Spassky', 'Date de naissance': '18/01/1935',
                   'Sexe': 'Homme', 'Rang': 708, 'Numéro associé': 7, 'Score': 0, 'Adversaires': []}
        player8 = {'Nom de famille': 'Hikaru', 'Prénom': 'Nakamura', 'Date de naissance': '28/08/1985',
                   'Sexe': 'Homme', 'Rang': 84, 'Numéro associé': 8, 'Score': 0, 'Adversaires': []}
        players_list.append(
            [player1, player2, player3, player4, player5, player6, player7, player8])
        return players_list

    def get_players_list():
        players_list = []
        player1 = ("Dubois", "Charles", "05-04-1995",
                   "H", 1)
        player2 = ("Alcor", "David", "17-12-1945",
                   "H", 2)
        player3 = ("Garry", "Kasparov", "1-06-1967",
                   "H", 3)
        player4 = ("Judit", "Polgar", "23-06-1989",
                   "F", 4)
        player5 = ("Fabiano", "Caruana", "15-11-1978",
                   "H", 5)
        player6 = ("Anish", "Giri", "26-03-2000",
                   "H", 6)
        player7 = ("Boris", "Spassky", "18-01-1935",
                   "H", 7)
        player8 = ("Hikaru", "Nakamura", "28-08-1985",
                   "H", 8)
        players_list.append(
            [player1, player2, player3, player4, player5, player6, player7, player8])
        return players_list
        # self.players = players_list
        # return self.players

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
