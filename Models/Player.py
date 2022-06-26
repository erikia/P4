from Controllers import Connection


class Player:
    """Classe qui instancie les joueurs."""

    def __init__(
        self,
        name="",
        first_name="",
        date="",
        gender="",
        ranking="",
        pairing_nb="",
        score="",
    ):
        """Retourne le nom, prénom, rang, numéro d'appariement et score."""
        self.p_table = Connection.db_players
        self.name = name
        self.first_name = first_name
        self.date = date
        self.gender = gender
        self.ranking = ranking
        self.pairing_nb = pairing_nb
        self.score = score
        self.id = ""

    def create_players(self, players_dict):
        """Retourne un dictionnaire du tournois"""
        self.p_table = {
            "nom": players_dict["Nom de famille"],
            "first_name": players_dict["Prénom"],
            "date": players_dict["Date de naissance"],
            "gender": players_dict["Sexe"],
            "ranking": players_dict["Rang"],
            "pairing_nb": players_dict["Numéro associé"],
            "score": players_dict["Score"],
        }
        return Player.save_players(self.p_table)

    def save_players(players):
        """Sauvegarde les joueurs dans la base de donnée sqlite"""
        save_table = Connection.cursor.executemany(
            "INSERT OR IGNORE INTO players"
            "(id, Nom_de_famille, Prénom, Date_de_naissance,"
            "Sexe, Rang, Numéro_associé, Score, Adversaires)"
            "VALUES"
            "(NULL, :nom, :first_name, :date, :gender,"
            ":ranking, :pairing_nb, :score)",
            [players],
        )
        player_table = save_table.connection.commit()
        return player_table
