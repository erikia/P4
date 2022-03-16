from Controllers import ApplicationCtrl
from Controllers import RoundsCtrl
from Controllers import PlayersCtrl
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

    def start_tournament():
        """Retourne le classe TournamentCtrl, créé des nouveaux joueurs et exporte les informations dans un fichier json"""
        tournament_number = 0
        tournament = TournamentCtrl()
        tournament.call_tournament()
        tournament.call_players()
        tournament.group_tournament_and_players()
        tournament.save_format_json()
        tournament.round_players(tournament_number)
        tournament.first_round()
        menu = ApplicationCtrl.ApplicationCtrl()

        menu.start()

    def tournament_infos():
        """Retourne un dictionnaire des informations du tournois """
        tournament_input = TournamentView.TournamentView()
        tournament = tournament_input.ask_tournament()

        return tournament

    def call_tournament(self):
        """Retourne les informations sur le tournoi rentrée par le menu"""
        self.tournament_dict = self.tournament_input
        return self.tournament_dict

    def call_players(self):
        """Retourne les informations sur les joueurs rentrée par le menu"""
        self.players_input.players_infos()
        self.players_list = self.players_input.sort_player_by_pairing_numbers()
        return self.players_list

    def group_tournament_and_players(self):
        """Retourne la liste des joueurs pour les regrouper ensemble dans un tournoi"""
        tournament_infos = Tournament.Tournament()
        self.total_tournament = tournament_infos.add_tournament_and_players(
            self.tournament_dict, self.players_list)
        return self.total_tournament

    def save_format_json(self):
        """Sauvegarde les informations du nouveau tournoi dans un fichier json"""
        save = Tournament.Tournament()
        save.save_format_json(self.total_tournament)

    def round_players(self, tournament_number):
        """Créer l'objet des rounds en récupérant les joueurs"""
        players = self.tournament.get_players(tournament_number)
        self.round_players = []
        for i in range(8):
            one_player = Player.Player(players[i])
            player_i = one_player.match_player()
            self.round_players.append(player_i)
        return self.round_players

    def first_round(self):
        """Docstring : resultat premier round , les 8 joueurs sont triés selon leur classement mondial saisi"""
        first_round = Round.Round()
        rank_players = sorted(self.round_players,
                              key=lambda x: x[1], reverse=False)
        match_list = first_round.pairing_first_round(rank_players)
        view_round = RoundView.RoundView()
        numero_round = view_round.ask_go_next_round()

        for i in range(4):
            view = RoundView.RoundView(i, numero_round, match_list[i])

        ask_rounds = RoundView.RoundView()
        ask_rounds.ask_start_round()
        start = Round.Round().start_round()
        ask_rounds.ask_end_round()
        end = Round.Round().finish_round()

        for i in range(4):
            player_score_1 = view.return_match_result(
                match_list[i][0])
            player_score_2 = view.return_match_result(
                match_list[i][1])
            match_list[i][0][3] += float(player_score_1)
            match_list[i][1][3] += float(player_score_2)

        return match_list, start, end

# rank_players = sorted(self.round_players, key=lambda x: x[1], reverse=False)
# TypeError: '<' not supported between instances of 'dict' and 'dict'

    # def first_round(self):
    #     """Docstring : resultat premier round , les 8 joueurs sont triés selon leur classement mondial saisi"""
    #     first_round = Round.Round()
    #     # round_players = TournamentCtrl.TournamentCtrl.round_players()
    #     # rank_players = sorted(round_players, key=lambda x: x[1]['Numéro associé'], reverse=False)

    #     # Solution 1 ?
    #     # rank_players = TournamentCtrl.TournamentCtrl.call_players(
    #     #     round_players)

    #     # Solution 2 ?
    #     # rank_players = sorted(self.round_players, key=itemgetter("Rang"))

    #     # Aide a tester
    #     rank_players = PlayersCtrl.PlayersCtrl.sort_players_by_ranking(
    #         self.round_players)
    #     #  srtd_players = sorted(self.players, key=lambda x: x.rank, reverse=True)
    #     # AttributeError: 'list' object has no attribute 'players'

    #     # for dictionary d
    #     # sorted(d.items(), key=lambda x: x[1]) #for inceasing order
    #     # sorted(d.items(), key=lambda x: x[1], reverse=True) # for decreasing order
    #     # #it will return list of key value pair tuples

    #     match_list = first_round.pairing_first_round(rank_players)
    #     numero_round = view.RoundView.ask_go_next_round()

    #     for i in range(4):
    #         view = view.RoundView(i, numero_round, match_list[i])
    #         player_score_1 = RoundsCtrl.RoundInput.round_infos(
    #             match_list[i][0])
    #         player_score_2 = RoundsCtrl.RoundInput.round_infos(
    #             match_list[i][1])
    #         match_list[i][0][3] += float(player_score_1)
    #         match_list[i][1][3] += float(player_score_2)

        return match_list

    def other_round(self):
        """Docsring : resultat autre rounds, les 8 joueurs sont triés en fonction de leur nombre total de points """
        other_round = Round.Round()
        round_players = TournamentCtrl.round_players()
        match_list = other_round.pairing_other_round(round_players)
        numero_round = view.RoundView.ask_go_next_round()

        for i in range(4):
            view = view.RoundView(i, numero_round, match_list[i])
            player_score_1 = RoundsCtrl.RoundInput.round_infos(
                match_list[i][0])
            player_score_2 = RoundsCtrl.RoundInput.round_infos(
                match_list[i][1])
            match_list[i][0][3] += float(player_score_1)
            match_list[i][1][3] += float(player_score_2)

        return match_list

    def resumeTournament(self):
        """Reprend un ancien tournoi en cours"""
        lenght = Tournament.Tournament()
        lenght_db = lenght.get_length_db()
