from Models import Round
from Views import PlayerView
from tinydb import TinyDB
from Models import Match
db = TinyDB('jtournament.json')


class RoundView:
    """La classe qui demande des informations sur le round à l'utilisateur"""

    def ask_go_next_round(self):
        """Demande à l'utilisateur d'aller au round suivant"""
        print("")
        print(f"Voulez-vous passer au round suivant ?")
        print("")
        print(
            f"oui:              ",
            f"Permet de passer au round suivant",
        )
        print(
            f"menu:             ",
            f"Permet de revenir au menu principal",
            f"les actions précédentes sont enregistrées",
        )
        command = input("Action choisie: ")
        print("")

        if command == "oui":
            self.go_next_round = "oui"
        elif command == "menu":
            self.go_next_round = "menu"
        else:
            print("")
            print(
                f"Merci de rentrer la bonne commande comme indiqué",
                f"dans les propositions ci-dessous"
            )
            self.ask_go_next_round()

        return self.go_next_round

    def ask_start_round(self):
        """Demande à l'utilisateur de commencer le round"""
        input("\nAppuyez sur ENTREE pour commencer le round\n")

    def ask_end_round(self):
        """Demande à l'utilisateur d'arreter le round"""
        input("\nAppuyez sur ENTREE pour ternimner le round\n")
