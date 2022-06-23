from Controllers import ApplicationCtrl
from Controllers import PlayersCtrl
from Models import Round
from Models import Tournament
from Views import RoundView, TournamentView


class TournamentCtrl:
    """La classe qui gère le tournoi"""

    def __init__(self):
        """initier un objet sur les autres modules du code (modèle, vue et contrôleur de menu)"""
        self.tournament_input = TournamentCtrl.get_tournament_infos()
        self.players_input = PlayersCtrl.PlayersCtrl()
        self.tournament = Tournament.Tournament()
        self.tournois_test = Tournament.Tournament()
        self.rounds = Round.Round()
        self.rounds_view = RoundView.RoundView()

    def start_tournament(self):
        """Retourne le classe TournamentCtrl, créé des nouveaux joueurs et exporte les informations dans un fichier json"""
        tournamentCtrl = TournamentCtrl()
        tournamentCtrl.create_tournament()
        tournamentCtrl.create_players()
        tournamentCtrl.create_rounds()
        tournamentCtrl.save_format_sqlite()
        menu = ApplicationCtrl.ApplicationCtrl()

        menu.start()

    def get_tournament_infos():
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
        # self.players_list = self.players_input
        # return self.players_list

        # Menu : saisie d'une liste des joueurs déjà crée
        self.players_list = self.tournament.players
        return self.players_list

    def create_rounds(self):
        """Retourne les rounds sur le tournoi"""
        self.round_dict = self.tournament.generate_rounds()
        return self.round_dict

    def save_format_sqlite(self):
        """Sauvegarde les informations du nouveau tournoi dans la base de donnée sqlite"""
        return self.tournament.create_tournament()
