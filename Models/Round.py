from datetime import datetime
from Models import Match
from tinydb import TinyDB
db = TinyDB('jtournament.json')


class Round:
    """Class qui instancie les rounds"""

    def __init__(self, matches=None, name='', start_time='',
                 date_time_end=''):
        self.r_table = db.table('Rounds')
        self.matches = matches
        self.name = name
        self.start_time = start_time
        self.date_time_end = date_time_end
        self.id = ''

    def create_round(self, round_num, players):
        self.name = "Rounds".format(round_num)
        self.matches = self.generate_matches(players)
        round_id = self.r_table.insert({
            "Matches": self.matches,
            "Nom": self.name,
            "Debut du match": self.start_time,
            "Fin du match": self.date_time_end})
        # return round_id
        return self.r_table.update({'id': round_id}, doc_ids=[round_id])[0]

    def generate_matches_real(self, players):
        matches_ids = []

        for i in range(4):
            match_id = Match.Match.get_serialized_match(self, players)
            matches_ids.append(match_id)
        return matches_ids

    def generate_matches(self, players):
        matches_ids = []

        for i in range(4):
            match_id = self.pairing_round(players)
            matches_ids.append(match_id)
        return matches_ids


    def pairing_round(self, players):
        """Associe les joueurs et continue les autres rounds"""
        rounds = []

        match_1 = Match.Match(players[0], players[1])
        match_2 = Match.Match(players[2], players[3])
        match_3 = Match.Match(players[4], players[5])
        match_4 = Match.Match(players[6], players[7])
        rounds.append(match_1.tuple_players())
        rounds.append(match_2.tuple_players())
        rounds.append(match_3.tuple_players())
        rounds.append(match_4.tuple_players())

        return rounds


    def date_time_now(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def finish_round(self):
        self.date_time_end = self.date_time_now()

    def start_round(self):
        self.date_time_start = self.date_time_now()
