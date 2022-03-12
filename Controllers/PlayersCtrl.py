from operator import itemgetter
from Models import Player
from Views import PlayerView


class PlayersCtrl:
    """La classe qui appelle la vue avec les informations sur les joueurs"""

    def __init__(self) -> None:

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
        self.players = players_list

    # def __init__(self) -> None:
    #     player_list = PlayersModel.Player.get_players_list()
    #     self.players = PlayersModel.Player()

    def players_infos(self):
        """Retourne un dictionnaire des informations des joueurs avec la méthode create_players_input """

        players_input = PlayerView.PlayersView()
        self.players = players_input.create_players_input()
        return self.players

    def sort_player_by_pairing_numbers(self):
        """Trier les joueurs par leur numéro associé"""

        sorted_players = sorted(self.players, key=itemgetter("Numéro associé"))
        return sorted_players

    def sort_players_by_ranking(self):
        """Trier les joueurs par leurs rang"""

        sorted_players = sorted(
            self.players, key=lambda x: x.rank, reverse=True)
        return sorted_players
