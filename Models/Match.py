from Models import Player


class Match:
    """Class qui initialise les matchs"""

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def return_players_opponents(self):
        """Associe les joueurs lors d'un match"""
        match = (self.player_1, self.player_2)
        return match

    def tuple_players(self):
        """Retourne une tuple d'un match contenant les joueurs et leurs scores """
        match_list = [self.player_1, self.player_score_1], [
            self.player_2, self.player_score_2]
        return match_list

    def players(self):
        players = []
        players.append(Player.Player(self.player_1))
        players.append(Player.Player(self.player_2))
        return players

    def score_players(self):
        pass
