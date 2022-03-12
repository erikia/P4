from Views import PlayerView


class RoundView:
    """La classe qui demande des informations sur le round à l'utilisateur"""

    def return_match_result(self):
        """Retourne le match jouée et permet de rentrez les scores """
        winner = PlayerView.verify_user_input(
            msg_display=f"{self.player_1.match}) VS " +
                        f"{self.player_2.match})\n"
                        f"Gagnant ?\n"
                        f"0 - {self.player_1.match})\n"
                        f"1 - {self.player_2.match})\n"
                        f"2 - Égalité\n> ",
            msg_error="Veuillez entrer 0, 1 ou 2.",
            value_type="selection",
            assertions=["0", "1", "2"]
        )

        if winner == "0":
            self.winner = self.player_1.match
            self.player_score_1.match += 1
        elif winner == "1":
            self.winner = self.player_2.match
            self.player_score_2.match += 1
        elif winner == "2":
            self.winner = "Égalité"
            self.player_score_1.match += 0.5
            self.player_score_2.match += 0.5
        else:
            print(
                f"Merci d'entrer: 1, 2 ou 0 dans la console")
            self.winner()

    def ask_go_next_round(self):
        """Demande à l'utilisateur d'aller au round suivant"""
        print("")
        print(f"Voulez-vous passer au round suivant ?")
        print("")
        print(
            f"yes:              ",
            f"Permet de passer au round suivant",
        )
        print(
            f"menu:             ",
            f"Permet de revenir au menu principal",
            f"les actions précédentes sont enregistrées",
        )
        command = input("Action choisie: ")
        print("")

        if command == "yes":
            self.go_next_round = "yes"
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
