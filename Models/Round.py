from Models import Match


class Round:
    """Class qui match initialise les rounds"""

    def __init__(self) -> None:
        self.match = Match()
        self.match_list = []

    def pairing_first_round(self, players):
        """Associe les joueurs et créer le round"""
        first_round = []

        match_1 = Match.Match(players[0], players[4])
        match_2 = Match.Match(players[1], players[5])
        match_3 = Match.Match(players[2], players[6])
        match_4 = Match.Match(players[3], players[7])
        first_round.append(match_1.return_players_opponents())
        first_round.append(match_2.return_players_opponents())
        first_round.append(match_3.return_players_opponents())
        first_round.append(match_4.return_players_opponents())

        return first_round

    def pairing_other_round(self, players):
        """Associe les joueurs et continue les autres rounds"""
        other_round = []

        match_1 = Match.Match(players[0], players[1])
        match_2 = Match.Match(players[2], players[3])
        match_3 = Match.Match(players[4], players[5])
        match_4 = Match.Match(players[6], players[7])
        other_round.append(match_1.return_players_opponents())
        other_round.append(match_2.return_players_opponents())
        other_round.append(match_3.return_players_opponents())
        other_round.append(match_4.return_players_opponents())

        return other_round
