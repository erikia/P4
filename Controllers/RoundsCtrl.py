from Models import Round
from Models import Tournament
from Views import RoundView


# class RoundsCtrl:
#     """Classe qui permet de gerer les rounds et de rentrer les scores de chaque matchs"""

#     def __init__(self):
#         """initier un objet sur les autres modules du code (modèle, vue et contrôleur de menu)"""
#         self.round_input = RoundsCtrl.round_infos()
#         self.round = Round.Round()

#     def call_round(self):
#         """Retourne les rounds sur le tournoi rentrée par le menu"""
#         self.round_dict = self.round_input.round_infos()
#         return self.round_dict

#     def round_infos():
#         """Retourne un dictionnaire des informations du tournois """

#         round_input = RoundView.RoundView()
#         round_result = round_input.return_match_result()

#         return round_result

class RoundsCtrl:

    def __init__(self):
        """initier un objet sur les autres modules du code (modèle, vue et contrôleur de menu)"""
        self.tournament = Tournament.Tournament()

    def call_round(self):
        """Retourne les rounds sur le tournoi rentrée par le menu"""
        self.round_dict = self.tournament.generate_rounds()
        return self.round_dict

    def group_tournament_and_rounds(self):
        """Retourne la liste des rounds pour les regrouper ensemble dans un tournoi"""
        tournament_infos = self.tournament
        self.total_tournament = tournament_infos.add_tournament_and_rounds(
            self.tournament_dict, self.rounds_list)
        return self.total_tournament
