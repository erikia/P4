from datetime import datetime
from Models import Match
from tinydb import JSONStorage, TinyDB, Query
from tinydb_serialization import SerializationMiddleware
from tinydb_serialization.serializers import DateTimeSerializer
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
        self.start_time = self.date_time_now()
        self.date_time_end = self.date_time_now()
        rounds = {
            "Matches": self.matches,
            "Nom": self.name,
            "Debut du match": self.start_time,
            "Fin du match": self.date_time_end}
        return rounds

    def generate_matches_OlD(self, players):
        matches = []

        for i in range(4):
            match = Match.Match.get_serialized_match(self, players)
            matches.append(match)
        return matches

    def generate_matches(self, players):
        matches = []

        for i in range(4):
            match = self.pairing_round(players)
            matches.append(match)
        return matches

    def score(self, players):
        match = self.generate_matches(players)
        score = Match.Match.return_match_result(match)

        return score

    def pairing_round(self, players):
        """Associe les joueurs et continue les autres rounds"""
        rounds = []

        # print(players)
        match_1 = Match.Match(players[0], players[1])
        match_2 = Match.Match(players[2], players[3])
        match_3 = Match.Match(players[4], players[5])
        match_4 = Match.Match(players[6], players[7])

        # Créations des matchs et des scores pour ensuite les sauvegarder dans la liste des rounds
        m1 = match_1.return_match_result()
        m2 = match_2.return_match_result()
        m3 = match_3.return_match_result()
        m4 = match_4.return_match_result()

        rounds.append(m1)
        rounds.append(m2)
        rounds.append(m3)
        rounds.append(m4)

        # Créations des matchs  pour ensuite les sauvegarder dans la liste des rounds
        # rounds.append(match_1.tuple_players())
        # rounds.append(match_2.tuple_players())
        # rounds.append(match_3.tuple_players())
        # rounds.append(match_4.tuple_players())

        return rounds

    def date_time_now(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def finish_round(self):
        self.date_time_end = self.date_time_now()

    def start_round(self):
        self.date_time_start = self.date_time_now()
