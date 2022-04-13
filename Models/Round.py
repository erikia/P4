from datetime import datetime
from Models import Match
from tinydb import TinyDB
db = TinyDB('jtournament.json')


class Round:
    """Class qui instancie les rounds"""

    def __init__(self, matches=None, name='', start_time='',
                 date_time_end=''):
        # self.match = Match()
        # self.match_list = []
        self.r_table = db.table('Rounds')
        self.opponents = opponents
        self.matches = matches
        self.name = name
        self.start_time = start_time
        self.date_time_end = date_time_end
        self.id = ''

    def create_round(self, round_num, players):
        self.name = "Rounds".format(round_num)
        self.matches = self.generate_matches2(players)
        round_id = self.r_table.insert({
            "Matches": self.matches,
            "Nom": self.name,
            "Debut du match": self.start_time,
            "Fin du match": self.date_time_end})
        # return round_id
        return self.r_table.update({'id': round_id}, doc_ids=[round_id])[0]

    def save_rounds(self):
        if self.id == '':
            result = self.create_rounds()
        else:
            result = self.r_table.update(
                {'Matches': self.matches,
                 'Nom': self.name,
                 'Debut du match': self.start_time,
                 'Fin du match': self.date_time_end,
                 'id': self.id
                 }, doc_ids=[self.id])[0]
        return result

    def generate_matches(self, players):
        matches_ids = []

        # match = Match.Match().create_match(players)
        # a = self.pairing_first_round(players)
        # match_id = Match.Match().create_match(players)
        # matches_ids.append(match_id)
        # for i in range(4):
        # match_id = Match.Match().create_match()
        # score = Match.Match().score_players(players)

        # matches_ids.append(score)
        match_id = self.pairing_first_round(players)
        matches_ids.append(match_id)
        return matches_ids

    def generate_matches2(self, players):
        matches_ids = []

        # match = Match.Match().create_match(players)
        # a = self.pairing_first_round(players)
        # match_id = self.pairing_first_round(players)
        # matches_ids.append(match_id)
        for i in range(4):
            match_id = Match.Match.get_serialized_match(self, players)
            matches_ids.append(match_id)
        return matches_ids
    
    def get_serialized_round(self):
        opponents = []
        for pair in self.players_pairs:
            opponents.append(
                (
                    pair[0].get_serialized_player(),
                    pair[1].get_serialized_player()
                 )
            )

        return {
            "Adversaires": opponents,
            "Matches": [Match.Match.get_serialized_match() for Match in self.matchs],
            "Nom": self.name,
            "Debut du match": self.start_time,
            "Fin du match": self.date_time_end,
            }

    def pairing_first_round(self, players):
        """Associe les joueurs et continue les autres rounds"""
        first_round = []

        match_1 = Match.Match(players[0].name, players[0].name)
        match_2 = Match.Match(players[0].name, players[0].name)
        match_3 = Match.Match(players[0].name, players[0].name)
        match_4 = Match.Match(players[0].name, players[0].name)
        first_round.append(match_1.tuple_players())
        first_round.append(match_2.tuple_players())
        first_round.append(match_3.tuple_players())
        first_round.append(match_4.tuple_players())

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

    def date_time_now(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def finish_round(self):
        self.date_time_end = self.date_time_now()

    def start_round(self):
        self.date_time_start = self.date_time_now()
