from tinydb import TinyDB
from Models import Match
from Views import RoundView
db = TinyDB('jtournament.json')


class RoundsCtrl:

    def __init__(self):
        """initier un objet sur les autres modules du code (modèle, vue et contrôleur de menu)"""
        self.rounds_view = RoundView.RoundView()
        self.m_table = db.table('Matches')

    def get_score_rounds(self, player_1, player_2):
        match = db.contains('Matches')

        self.start_rounds = self.rounds_view.ask_start_round()
        # match = Match.Match().pairing_round()
        self.score_input = match.return_match_result(player_1, player_2)
        self.end_rounds = self.rounds_view.ask_end_round()
        return self.score_input