class Player:
    """Classe qui instancie les joueurs."""

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
