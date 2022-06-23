from Controllers import Connection

class Player:
    """Classe qui instancie les joueurs."""

    def __init__(self, name, first_name, date, gender, ranking, pairing_nb, score):
        """Retourne le joueur avec son nom, prénom, rang, numéro d'appariement et score."""
        self.p_table = Connection.db_players
        self.name = name
        self.first_name = first_name
        self.date = date
        self.gender = gender
        self.ranking = ranking
        self.pairing_nb = pairing_nb
        self.score = score
        self.id = ''
    
    def save_players(rounds):
        """Sauvegarde les joueurs dans la base de donnée sqlite"""
        save_table = Connection.cursor.executemany(
            "INSERT OR IGNORE INTO players (id, Nom_de_famille, Prénom, Date_de_naissance, Sexe, Rang, Numéro_associé, Score, Adversaires) VALUES( NULL, :Matches, :Nom, :Debut, :Fin)", [rounds])
        match_table = save_table.connection.commit()
        return match_table

