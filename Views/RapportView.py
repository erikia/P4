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
    
    def return_tournaments_number(self):
        """Display tournament selection menu"""

        print(
            f"\nMenu des rapports des tournois\n"
        )

        print("\nMerci d'enter le numero du tournoi a poursuivre ou 'retour'")
        print("Vous pouvez le rechercher via la fonction show du menu principal\n")

        # if self.number:
        #     try:
        #         ask_number = int(input("Numero du tournoi: "))
        #         self.number = ask_number
        #     except ValueError:
        #         print(f"Merci d'entrer un nombre entier")
        #         print("")
        #         self.ask_number()

        #     return self.number
       



    def pick_tournaments_number(self):
        try:
            tournaments_number = int(input("Numero du tournoi: "))
            self.number = tournaments_number
        except ValueError:
            print(f"Merci d'entrer un nombre entier")
            print("")
            self.pick_tournaments_number()

        return self.number
    
    def show_players(self, players):
        for player in players:
            print(""" {} - {}
        Ranking: {}
        ----------------""".format(
                        player.last_name, player.first_name, player.ranking))

    def show_rounds(self, rounds):
            for round_ in rounds:
                print("""
                    {}
                    {} - {}
                    """.format(round_.name, round_.date_time_start, round_.date_time_end))

    def show_match(self, match, players):
            p1 = players[0]
            p2 = players[0]
            print("""
            {} {} vs {} {}
            Score:      {} - {}
            -----------------------""".format(
                        p1.first_name, p1.last_name, p2.first_name, p2.last_name,
                        match.p1_score, match.p2_score))
