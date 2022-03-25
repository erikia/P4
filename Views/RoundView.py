from Models import Round
from Views import PlayerView
from tinydb import TinyDB
from Models import Match
db = TinyDB('jtournament.json')


class RoundView:
    """La classe qui demande des informations sur le round à l'utilisateur"""

    def __init__(self):
        # self.player_1 = Match.Match().player_1
        # self.player_2 = Match.Match().player_2
        # self.player_score_1 = Match.Match().player_score_1
        # self.player_score_2 = Match.Match().player_score_2
        # self.player_1 = Match.Match.tuple_players()
        # tuple_p = Match.Match.tuple_players()
        # tuple_p.keys(1)
        # print(tuple.keys(1))
        # self.player_2 = Match.Match.tuple_players().player_2
        # self.player_score_1 = Match.Match.tuple_players().player_score_1
        # self.player_score_2 = Match.Match.tuple_players().player_score_2
        # rounds = Round.Round().matches
        # tuples = Match.Match.tuple_players()

        # self.player_1 = match.players()
        # self.player_2 = Match.Match().player_2
        # self.player_score_1 = Match.Match().player_score_1
        # self.player_score_2 = Match.Match().player_score_2
        pass

    def players_view(rounds):
        for match in rounds.matches:
            players = match.players()
            player_1 = players[0]
            player_2 = players[1]

    def return_match_result(self, rounds):
        """Retourne le match jouée et permet de rentrez les scores """

        for match in rounds.matches:
            players = match.players()
            player_1 = players[0]
            player_2 = players[1]

        winner = PlayerView.PlayersView.verify_user_input(self,
                                                          msg_display=f"{self.player_1}) VS " +
                                                          f"{self.player_2})\n"
                                                          f"Qui est Gagnant ?\n"
                                                          f"0 - {self.player_1})\n"
                                                          f"1 - {self.player_2})\n"
                                                          f"2 - Égalité\n> ",
                                                          msg_error="Veuillez entrer 0, 1 ou 2.",
                                                          value_type="selection",
                                                          assertions=[
                                                              "0", "1", "2"]
                                                          )

        if winner == "0":
            self.winner = self.player_1
            self.player_score_1 += 1
        elif winner == "1":
            self.winner = self.player_2
            self.player_score_2 += 1
        elif winner == "2":
            self.winner = "Égalité"
            self.player_score_1 += 0.5
            self.player_score_2 += 0.5
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
