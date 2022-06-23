from Controllers import ApplicationCtrl, Connection
from Views import RapportView


class RapportCtrl:

    def __init__(self) -> None:
        self.playermodel = Connection.db_players
        self.rapportview = RapportView.RapportView()

    def start_rapport():
        """Lance le menu pour afficher les rapports"""
        rapportCtrl = RapportCtrl()
        rapportCtrl.get_menu()

    def get_menu(self):
        """Retourne le menu pour afficher soit les tounois soit les joueurs"""
        self.command = self.rapportview
        self.menu = self.command.get_menu_reports()

        if self.menu == "tournois":
            RapportCtrl.show_tournaments()
        if self.menu == "joueurs":
            self.show_list_players()
        elif self.menu == "retour":
            retour = ApplicationCtrl.ApplicationCtrl()
            retour.start()
        else:
            print(
                f"\nMerci de rentrer la bonne commande comme indiqué",
                f"dans les propositions ci-dessous\n"
            )
            self.get_menu()

    def show_tournaments():
        """Retourne une liste de la base de donnée de tous les tournois"""
        tournaments_list = Connection.db_tournaments
        return print(tournaments_list)

    def show_list_players(self, players='all', mode='alpha'):
        """Retourne une liste de la base de donnée de tous les joueurs selon leurs rangs"""
        if players == 'all':
            players = self.playermodel
        if mode == 'rank':
            players = self.sort_players_by_ranking(
                self.playermodel)
        else:
            players = sorted(
                players, key=lambda x: (x[1], x[2]),
                reverse=False)

        self.rapportview.show_players(players)
    
    def sort_players_by_ranking(self, players):
        srtd_players = sorted(players, key=lambda x: x.ranking, reverse=True)
        return srtd_players
