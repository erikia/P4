class MenuView:
    """La classe qui affiche le menu principal, et permmet de selectionner la commande des sous-menu"""

    def __init__(self):
        """Afficher les possibilités du menu principal à l'utilisateur"""

        print(f"\n\n ---- Tournoi d'échecs ----")
        print(f"\n\n---- Menu principal ----\n")
        print("\nMerci d'entrer un des mots suivant: ")
        print(
            f"commencer:            ",
            f"Commencer un nouveau tournoi",
        )
        print(
            f"rapports:             ",
            f"Afficher les rapports",
        )
        print(
            f"supprimer:            ",
            f"Effacer les informations précédentes présentes sur la console",
        )
        print(
            f"quitter:              ",
            f"Quitter le programme\n",
        )
        self.command = None

    def launch_command_menu(self):
        """Lance la commande du menu choisi par l'utilisateur"""

        input_option = input("Veuillez rentrer votre option : ")

        if input_option == "commencer":
            self.command = "commencer"
        elif input_option == "rapports":
            self.command = "rapports"
        elif input_option == "supprimer":
            self.command = "supprimer"
        elif input_option == "quitter":
            print("\nMerci d'avoir utilisé ce programme\n")
            self.command = "quitter"
        else:
            print(
                f"\nMerci de rentrer la bonne commande comme indiqué",
                f"dans les propositions ci-dessous\n"
            )
            self.launch_command_menu()

        return self.command
