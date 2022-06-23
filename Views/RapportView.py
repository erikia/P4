class RapportView:
    """La classe qui affiche le menu des rapports, et permmet de selectionner la commande des sous-menu"""

    def __init__(self):
        self.command = None
        self.number = None

    def get_menu_reports(self):
        """Afficher les possibilités du menu des rapports à l'utilisateur"""

        print(f"\n\n---- Menu des rapports ----\n")
        print("\nMerci d'entrer un des mots suivant: ")
        print(
            f"tournois:            ",
            f"Affichier les tournois",
        )
        print(
            f"joueurs:            ",
            f"Affichier les joueurs",
        )
        print(
            f"retour:              ",
            f"Retour au menu principal\n",
        )
        input_option = input("Veuillez rentrer votre option : ")

        if input_option == "tournois":
            self.command = "tournois"
        elif input_option == "joueurs":
            self.command = "joueurs"
        elif input_option == "retour":
            self.command = "retour"
        else:
            print(
                f"\nMerci de rentrer la bonne commande comme indiqué",
                f"dans les propositions ci-dessous\n"
            )
            self.launch_command_menu_reports()

        return self.command

    def launch_command_menu_reports(self):
        """Lance la commande du menu choisi par l'utilisateur"""

        input_option = input("Veuillez rentrer votre option : ")

        if input_option == "tournois":
            self.command = "tournois"
        elif input_option == "joueurs":
            self.command = "joueurs"
        elif input_option == "retour":
            self.command = "retour"
        else:
            print(
                f"\nMerci de rentrer la bonne commande comme indiqué",
                f"dans les propositions ci-dessous\n"
            )
            self.launch_command_menu_reports()

        return self.command


    def show_players(self, players):
        """Retourne les joueurs avec leurs noms de familles,prénoms et rang"""
        for player in players:
            print(""" {} - {}
        Ranking: {}
        ----------------""".format(
                player[1], player[2], player[5]))
