# import os
import sys
from os import system, name
from Controllers import RapportCtrl, TournamentCtrl
from Models import Tournament
from Views import MenuView
from Controllers.Connection import close_db


class ApplicationCtrl:
    """La classe qui gère le menu principale"""

    def __init__(self):
        self.controller = None
        self.tournament = Tournament.Tournament()
        self.tournamentCtrl = TournamentCtrl.TournamentCtrl()

    def start(self):
        """
        Lance l'application pour demander une action sur le menu principal
        Appeler d'autres contrôleurs suite à l'entrée de l'utilisateur
        """
        self.command = MenuView.MenuView()
        self.menu_starting = self.command.launch_command_menu()

        if self.menu_starting == "commencer":
            print("")
            self.tournamentCtrl.start_tournament()
        elif self.menu_starting == "rapports":
            print("")
            RapportCtrl.RapportCtrl.start_rapport()
        elif self.menu_starting == "quitter":
            close_db()
            sys.exit()
        elif self.menu_starting == "supprimer":
            self.clear_terminal()
            self.start()

    def clear_terminal(self):
        """Supprimer le terminal"""
        # Pour windows
        if name == 'nt':
            _ = system('cls')
    
        # Pour mac et linux
        else:
            _ = system('clear')
