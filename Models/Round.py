from Models import Match
from tinydb import TinyDB
db = TinyDB('jtournament.json')

class Round:
    """Class qui match initialise les rounds"""

    def __init__(self, matches=None, name='', start_time='',
            date_time_end=''):
        # self.match = Match()
        # self.match_list = []
        self.r_table = db.table('Rounds')
        self.matches = matches
        self.name = name
        self.start_time = start_time
        self.date_time_end = date_time_end
        self.id = ''
    
    def create_round(self, round_num):
        self.name = "Rounds{}".format(round_num)
        self.matches = self.generate_matches()
        round_id = self.r_table.insert({
            "matches": self.matches,
            "name": self.name,
            "start_time": self.start_time,
            "date_time_end": self.date_time_end})
        return self.r_table.update({'id': round_id}, doc_ids=[round_id])[0]

    def generate_matches(self):
        matches_ids = []
        for i in range(4):
            match_id = Match().create_match()
            matches_ids.append(match_id)
        return matches_ids

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
