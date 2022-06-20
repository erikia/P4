import sys
from Controllers import RapportCtrl, TournamentCtrl
from Models import Tournament
from Views import MenuView, RapportView


class ApplicationCtrl:
    """La classe qui gère le menu principale"""

    def __init__(self):
        self.controller = None
        self.tournament = Tournament.Tournament()

    def start(self):
        """
        Lance l'application pour demander une action sur le menu principal
        Appeler d'autres contrôleurs suite à l'entrée de l'utilisateur
        """
        self.command = MenuView.MenuView()
        self.menu_starting = self.command.launch_command_menu()

        if self.menu_starting == "commencer":
            print("")
            create_new_tournament = TournamentCtrl.TournamentCtrl.start_tournament()
            create_new_tournament()
        elif self.menu_starting == "reprendre":
            print("")
            resume = TournamentCtrl.TournamentCtrl.resumeTournament()
            resume()
        elif self.menu_starting == "rapports":
            print("")
            rapports = RapportCtrl.RapportCtrl.start_rapport()
            rapports()
        elif self.menu_starting == "quitter":
            sys.exit()
        elif self.menu_starting == "supprimer":
            self.clear_terminal()
            self.start()
