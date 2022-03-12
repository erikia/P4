class Player:
    """Classe de joueur qui initialiser les joueurs."""

    def __init__(self, questions_informations):
        """Retourne le joueur avec son nom, prénom, rang, numéro d'appariement et score."""
        self.name = questions_informations["Nom de famille"]
        self.first_name = questions_informations["Prénom"]
        self.date = questions_informations["Date de naissance"]
        self.gender = questions_informations["Sexe"]
        self.ranking = questions_informations["Rang"]
        self.pairing_nb = questions_informations["Numéro associé"]
        self.score = questions_informations["Score"]
        self.opponents = questions_informations["Adversaires"]

    def match_player(self):
        """Retourne les informations des joueurs"""
        match_player = [f"{self.name} {self.first_name} (Rang, Numéro associé, Score): ", (
            self.ranking), (self.pairing_nb), float(self.score)]

        return match_player

    def get_players_list():
        players_list = []
        player1 = ("Dubois", "Charles", "05-04-1995",
                   "H", 1)
        player2 = ("Alcor", "David", "17-12-1945",
                   "H", 2)
        player3 = ("Garry", "Kasparov", "1-06-1967",
                   "H", 3)
        player4 = ("Judit", "Polgar", "23-06-1989",
                   "F", 4)
        player5 = ("Fabiano", "Caruana", "15-11-1978",
                   "H", 5)
        player6 = ("Anish", "Giri", "26-03-2000",
                   "H", 6)
        player7 = ("Boris", "Spassky", "18-01-1935",
                   "H", 7)
        player8 = ("Hikaru", "Nakamura", "28-08-1985",
                   "H", 8)
        players_list.append(
            [player1, player2, player3, player4, player5, player6, player7, player8])
        return players_list
