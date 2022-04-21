from Models import Match
from Views import RoundView


class RoundsCtrl:

    def __init__(self):
        """initier un objet sur les autres modules du code (modèle, vue et contrôleur de menu)"""
        self.round_view = RoundView.RoundView()
        self.match_model = Match.Match()

    def get_score_rounds(self):
        
        self.start_rounds = self.round_view.ask_start_round()
        self.end_rounds = self.round_view.ask_end_round()
        self.score_input = self.match_model.return_match_result()

        return self.score_input