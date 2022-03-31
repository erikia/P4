from Models import Player
from tinydb import TinyDB

from Views import PlayerView, RoundView
db = TinyDB('jtournament.json')


class Match:
    """Class qui instancie les matchs"""

    def __init__(self, player_1, player_2, player_score_1='', player_score_2=''):
        self.m_table = db.table('Matches')
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_score_1 = player_score_1
        self.player_score_2 = player_score_2
        self.id = ''

    def return_players_opponents(self):
        """Associe les joueurs lors d'un match"""
        match = (self.player_1, self.player_2)
        return match

    def tuple_players(self):
        """Retourne une tuple d'un match contenant les joueurs et leurs scores """
        match_list = [self.player_1, self.player_score_1], [
            self.player_2, self.player_score_2]
        return match_list

    # def create_match(self):
    #     match_id = self.m_table.insert({
    #         'Joueur 1': self.player_1.name,
    #         'Score du Joueur 1': self.player_score_1,
    #         'Joueur 2': self.player_2.name,
    #         'Score du Joueur 2': self.player_score_2
    #     })
    #     return self.m_table.update({'id': match_id}, doc_ids=[match_id])[0]

    def create_match(self, ):
        match_id = self.m_table.insert({
            'Joueur 1': self.player_1.name,
            'Score du Joueur 1': self.player_score_1,
            'Joueur 2': self.player_2.name,
            'Score du Joueur 2': self.player_score_2
        })
        # self.m_table.update({'id': match_id}, doc_ids=[match_id])[0]
        return self.m_table.update({'id': match_id}, doc_ids=[match_id])[0]

    def players(self):
        players = []
        players.append(Player.get_player_from_id(self.player_1))
        players.append(Player.get_player_from_id(self.player_2))
        return players

    def score_players(self):
        """Retourne la vue pour affichier le score du match"""
        players = players()
        self.view_score = RoundView.RoundView()
        self.score = self.view_score.return_match_result(players)
        return self.score

    def save_match(self):
        if self.id == '':
            result = self.create_match()
        else:
            result = self.m_table.update(
                {'Joueur 1': self.player_1.name,
                 'Score du Joueur 1': self.player_score_1,
                 'Joueur 2': self.player_2.name,
                 'Score du Joueur 2': self.player_score_2,
                 'id': self.id
                 }, doc_ids=[self.id])[0]
        return result

    def return_match_result(self):
        """Retourne le match jouée et permet de rentrez les scores """

        winner = PlayerView.PlayersView.verify_user_input(self,
                                                          msg_display=f"{self.player_1}) VS " +
                                                          f"{self.player_2})\n"
                                                          f"Qui est Gagnant ?\n"
                                                          f"0 - {self.player_1})\n"
                                                          f"1 - {self.player_2})\n"
                                                          f"2 - Égalité\n> ",
                                                          msg_error="Veuillez entrer 0, 1 ou 2.",
                                                          value_type="selection",
                                                          assertions=[
                                                              "0", "1", "2"]
                                                          )

        if winner == "0":
            self.winner = self.player_1
            self.player_score_1 += 1
        elif winner == "1":
            self.winner = self.player_2
            self.player_score_2 += 1
        elif winner == "2":
            self.winner = "Égalité"
            self.player_score_1 += 0.5
            self.player_score_2 += 0.5
        else:
            print(
                f"Merci d'entrer: 1, 2 ou 0 dans la console")
            self.winner()
