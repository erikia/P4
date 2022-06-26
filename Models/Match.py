from Controllers import Connection
from Views import PlayerView


class Match:
    """Class qui instancie les matchs"""

    def __init__(self, player_1, player_2):
        self.m_table = Connection.db_matchs
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_score_1 = 0
        self.player_score_2 = 0
        self.winner = ""
        self.id = ""

    def return_match_result(self):
        """Retourne le match jouée et permet de rentrez les scores"""
        print("\nLes résultats du match peuvent être soumis : \n")
        winner = PlayerView.PlayersView.verify_user_input(
            self,
            msg_display=f"{self.player_1[1]} VS " + f"{self.player_2[1]}\n"
            f"Qui est est le gagnant ?\n"
            f"0 - {self.player_1[1]}\n"
            f"1 - {self.player_2[1]}\n"
            f"2 - Égalité\n> ",
            msg_error="Veuillez entrer 0, 1 ou 2.",
            value_type="selection",
            assertions=["0", "1", "2"],
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

        self.m_table = {
            "player_1": self.player_1[1],
            "score_player1": self.player_score_1,
            "player_2": self.player_2[1],
            "score_player2": self.player_score_2,
            "winner": self.winner[1],
        }
        print("Le gagnant est : " + self.winner[1])
        return Match.save_match_db(self.m_table)

    def save_match_db(match):
        """Savegarde les matchs dans la base de donnée sqlite"""
        save_table = Connection.cursor.executemany(
            "INSERT OR IGNORE INTO matches"
            "(id, Joueur_1, score_joueur_1, Joueur_2, score_joueur_2, winner)"
            "VALUES"
            "(NULL, :player_1, :score_player1, :player_2,"
            ":score_player2, :winner)",
            [match],
        )
        m_table = save_table.connection.commit()
        return m_table
