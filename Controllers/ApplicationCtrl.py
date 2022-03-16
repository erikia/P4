import sys
from Controllers import TournamentCtrl
from Views import MenuView


class ApplicationCtrl:
    """La classe qui gère le menu principale"""

    def __init__(self):
        self.controller = None

    def start(self):
        """
        Lance l'application pour demander une action sur le menu principal
        Appeler d'autres contrôleurs suite à l'entrée de l'utilisateur
        """
        self.action = MenuView.MenuView()
        self.menu_starting = self.action.launch_command_menu()

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
            rapports = ""
            rapports()

        elif self.menu_starting == "quitter":
            sys.exit()

        elif self.menu_starting == "supprimer":
            self.clear_terminal()
            self.start()