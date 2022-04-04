from Controllers import ApplicationCtrl, TournamentCtrl
from Models import Player, Tournament
from Views import RapportView


class RapportCtrl:

    def __init__(self) -> None:
        self.playermodel = Player.Player()
        self.tournamentsmodel = Tournament.Tournament()
        self.tournamentsCtrl = TournamentCtrl.TournamentCtrl()
        self.rapportview = RapportView.RapportView()

    def start_rapport():
        rapportCtrl = RapportCtrl()
        rapportCtrl.get_menu()

    def get_menu(self):
        self.command = self.rapportview
        self.menu = self.command.get_menu_reports()
        # self.number = self.rapportview.pick_tournaments_number()

        if self.menu == "tournois":
            self.show_tournaments()
        if self.menu == "joueurs":
            self.list_players()
        elif self.menu == "retour":
            retour = ApplicationCtrl.ApplicationCtrl()
            retour.start()
        else:
            print(
                f"\nMerci de rentrer la bonne commande comme indiqué",
                f"dans les propositions ci-dessous\n"
            )
            self.get_menu()
    

    def list_players(self, players='all', mode='alpha'):
        if players == 'all':
            players = self.playermodel.read_players()
        if mode == 'rank':
            players = self.tournamentsCtrl.sort_players_by_ranking(players)
        else:
            players = sorted(
                players, key=lambda x: (x.last_name, x.first_name),
                reverse=False)

        self.rapportview.show_players(players)

    def list_players_ranking(self):
        self.list_players(mode='ranking')

    def list_players_tournament(self, mode='alpha'):
        selected_tournament = self.tournamentsCtrl.select_tournament()
        players = selected_tournament.players
        self.list_players(players, mode=mode)

    def list_players_tournament_ranking(self):
        self.list_players_tournament(mode='ranking')

    def all_tournaments(self):
        self.t_controller.show_tournaments()