from Views import PlayerView


class PlayersCtrl:
    """La classe qui appelle la vue avec les informations sur les joueurs"""

    def players_infos(self):
        """Retourne un dictionnaire des informations des joueurs"""

        players_input = PlayerView.PlayersView()
        self.players = players_input.create_players_input()
        return self.players
