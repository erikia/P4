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
