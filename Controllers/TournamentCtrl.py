from Controllers import ApplicationCtrl
from Controllers import PlayersCtrl
from Controllers.RoundsCtrl import RoundsCtrl
from Models import Player, Round
from Models import Tournament
from Views import RoundView, TournamentView


class TournamentCtrl:
    """La classe qui gère le tournoi"""

    def __init__(self):
        """initier un objet sur les autres modules du code (modèle, vue et contrôleur de menu)"""
        self.tournament_input = TournamentCtrl.tournament_infos()
        self.players_input = PlayersCtrl.PlayersCtrl()
        self.tournament = Tournament.Tournament()
        self.tournois_test = Tournament.Tournament()
        self.rounds = Round.Round()
        self.rounds_view = RoundView.RoundView()

    def start_tournament():
        """Retourne le classe TournamentCtrl, créé des nouveaux joueurs et exporte les informations dans un fichier json"""
        tournamentCtrl = TournamentCtrl()
        tournamentCtrl.create_tournament()
        tournamentCtrl.create_players()
        tournamentCtrl.create_rounds()
        tournamentCtrl.group_tournament_and_players()
        tournamentCtrl.group_tournament_and_rounds()
        # tournamentCtrl.start_match()
        tournamentCtrl.save_format_json()

        menu = ApplicationCtrl.ApplicationCtrl()

        menu.start()

    def start_match(self):
        return_score = RoundsCtrl.get_score_rounds(self)
        return return_score

    def tournament_infos():
        """Retourne un dictionnaire des informations du tournois """
        tournament_input = TournamentView.TournamentView()
        tournament = tournament_input.ask_tournament()

        return tournament

    def create_tournament(self):
        """Retourne les informations sur le tournoi rentrée par le menu"""
        self.tournament_dict = self.tournament_input
        return self.tournament_dict

    def create_players(self):
        """Retourne les informations sur les joueurs rentrée par le menu"""

        # Menu : saisie a la main des joueurs
        # self.players_input.players_infos()
        # self.players_list = self.players_input.sort_player_by_pairing_numbers()
        # return self.players_list

        # Menu : saisie d'une liste des joueurs déjà crée
        self.players_list = self.tournament.players
        return self.players_list

    def create_rounds(self):
        """Retourne les rounds sur le tournoi"""
        self.round_dict = self.tournament.generate_rounds()
        return self.round_dict

    def group_tournament_and_players(self):
        """Retourne la liste des joueurs pour les regrouper ensemble dans un tournoi"""
        tournament_infos = self.tournament
        self.total_tournament = tournament_infos.add_tournament_and_players(
            self.tournament_dict, self.players_list)
        return self.total_tournament

    def group_tournament_and_rounds(self):
        """Retourne la liste des rounds pour les regrouper ensemble dans un tournoi"""
        tournament_infos = self.tournament
        self.total_tournament = tournament_infos.add_tournament_and_rounds(
            self.tournament_dict, self.round_dict)
        return self.total_tournament

    def group_tournament_and_matchs(self):
        """Retourne la liste des matchs pour les regrouper ensemble dans un tournoi"""
        tournament_infos = self.tournament
        self.total_tournament = tournament_infos.add_tournament_and_matchs(
            self.tournament_dict, self.matches_dict)
        return self.total_tournament

    def save_format_json(self):
        """Sauvegarde les informations du nouveau tournoi dans un fichier json"""
        save = self.tournament
        save.save_format_json(self.total_tournament)

    def sort_players_by_ranking(self, players):
        srtd_players = sorted(players, key=lambda x: x.ranking, reverse=True)
        return srtd_players

    def resumeTournament(self):
        """Reprend un ancien tournoi en cours"""
        lenght = self.tournament
        lenght_db = lenght.get_length_db()
