from Controllers import Connection
from Views import PlayerView
db = ('db.sqlite')


class Match:
    """Class qui instancie les matchs"""

    def __init__(self, player_1, player_2):
        self.m_table = Connection.db_matchs
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_score_1 = 0
        self.player_score_2 = 0
        self.winner = ""
        self.id = ''

    def tuple_players(self):
        """Retourne une tuple d'un match contenant les joueurs et leurs scores """
        match_list = [self.player_1, self.player_score_1], [
            self.player_2, self.player_score_2]
        return match_list

    def score_players(self, players):
        """Retourne la vue pour affichier le score du match"""
        self.score = self.return_match_result(players)
        return self.score
    
    def return_match_result(self):
        """Retourne le match jouée et permet de rentrez les scores """
        print("\nLes résultats du match peuvent être soumis : \n")
        winner = PlayerView.PlayersView.verify_user_input(self,
                                                          msg_display=f"{self.player_1[1]} VS " +
                                                          f"{self.player_2[1]}\n"
                                                          f"Qui est est le gagnant ?\n"
                                                          f"0 - {self.player_1[1]}\n"
                                                          f"1 - {self.player_2[1]}\n"
                                                          f"2 - Égalité\n> ",
                                                          msg_error="Veuillez entrer 0, 1 ou 2.",
                                                          value_type="selection",
                                                          assertions=[
                                                              "0", "1", "2"]
                                                          )

        if winner == "0":
            self.winner = self.player_1
            print(self.winner)
            self.player_score_1 += 1
            print(self.player_score_1)
            self.create_match
        elif winner == "1":
            self.winner = self.player_2
            self.player_score_2 += 1
            self.create_match
        elif winner == "2":
            self.winner = "Égalité"
            self.player_score_1 += 0.5
            self.player_score_2 += 0.5
            self.create_match
        else:
            print(
                f"Merci d'entrer: 1, 2 ou 0 dans la console")

        # self.player_1 += self.player_score_1
        # self.player_2 += self.player_score_2


    def create_match(self):
        self.m_table = ({
            "player_1": self.player_1,
            "score_player1": self.player_score_1,
            "player_2": self.player_2,
            "score_player2": self.player_score_2,
            "winner": self.winner,
        })
        return Match.save_db(self.m_table)

    # def save_db(match):
    #     save_table = Connection.cursor.executemany(
    #         "INSERT OR IGNORE INTO macthes VALUES( NULL, ?, ?, ?, ?)", match)
    #     match_table = save_table.connection.commit()
    #     return match_table

    def save_db(match):

        save_table = Connection.cursor.executemany(
            "INSERT OR IGNORE INTO rounds (id, Joueur_1, score_joueur_1, Joueur_2, score_joueur_2, winner) VALUES( NULL, :player_1, :score_player1, :player_2, :score_player2, :winner)", match)
        print(save_table)
        m_table = save_table.connection.commit()
        return m_table
