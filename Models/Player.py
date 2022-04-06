from tinydb import TinyDB
db = TinyDB('jtournament.json')

class Player:
    """Classe qui instancie les joueurs."""

    def __init__(self):
        """Retourne le joueur avec son nom, prénom, rang, numéro d'appariement et score."""
        # self.name = questions_informations["Nom de famille"]
        # self.first_name = questions_informations["Prénom"]
        # self.date = questions_informations["Date de naissance"]
        # self.gender = questions_informations["Sexe"]
        # self.ranking = questions_informations["Rang"]
        # self.pairing_nb = questions_informations["Numéro associé"]
        # self.score = questions_informations["Score"]
        # self.opponents = questions_informations["Adversaires"]
        self.p_table = db.table('players')
        self.name = ["Nom de famille"]
        self.first_name = ["Prénom"]
        self.date = ["Date de naissance"]
        self.gender = ["Sexe"]
        self.ranking = ["Rang"]
        self.pairing_nb = ["Numéro associé"]
        self.score = ["Score"]
        self.opponents = ["Adversaires"]
        self.id = ''

    def match_player(self):
        """Retourne les informations des joueurs"""
        match_player = [f"{self.name} {self.first_name} (Rang, Numéro associé, Score): ", (
            self.ranking), (self.pairing_nb), float(self.score)]

        return match_player

    def get_player_from_id(self, id_num):
        player = Player()
        questions_informations = player.p_table.get(doc_id=int(id_num))
        for i in player:
            self.name = questions_informations["Nom de famille"]
            self.first_name = questions_informations["Prénom"]
            self.date = questions_informations["Date de naissance"]
            self.gender = questions_informations["Sexe"]
            self.ranking = questions_informations["Rang"]
            self.pairing_nb = questions_informations["Numéro associé"]
            self.score = questions_informations["Score"]
            self.opponents = questions_informations["Adversaires"]
            self.id = id_num
        # player.last_name = player_data["last_name"]
        # player.first_name = player_data["first_name"]
        # player.birth_date = player_data["birth_date"]
        # player.sex = player_data["sex"]
        # player.ranking = player_data["ranking"]
        # player.id = id_num

        return player

    def get_players_list():
        players_list: list = []

        player1 = {'Nom de famille': 'Dubois', 'Prénom': 'Charles', 'Date de naissance': '05/04/1995',
                'Sexe': 'Homme', 'Rang': 356, 'Numéro associé': 1, 'Score': 0, 'Adversaires': []}
        player2 = {'Nom de famille': 'Alcor', 'Prénom': 'David', 'Date de naissance': '17/12/1945',
                'Sexe': 'Homme', 'Rang': 287, 'Numéro associé': 2, 'Score': 0, 'Adversaires': []}
        player3 = {'Nom de famille': 'Garry', 'Prénom': 'Kasparov', 'Date de naissance': '1/06/1967',
                'Sexe': 'Homme', 'Rang': 593, 'Numéro associé': 3, 'Score': 0, 'Adversaires': []}
        player4 = {'Nom de famille': 'Judit', 'Prénom': 'Polgar', 'Date de naissance': '1/06/1967',
                'Sexe': 'Femme', 'Rang': 407, 'Numéro associé': 4, 'Score': 0, 'Adversaires': []}
        player5 = {'Nom de famille': 'Fabiano', 'Prénom': 'Caruana', 'Date de naissance': '15/11/1978',
                'Sexe': 'Homme', 'Rang': 579, 'Numéro associé': 5, 'Score': 0, 'Adversaires': []}
        player6 = {'Nom de famille': 'Anish', 'Prénom': 'Giri', 'Date de naissance': '26/03/2000',
                'Sexe': 'Homme', 'Rang': 68, 'Numéro associé': 6, 'Score': 0, 'Adversaires': []}
        player7 = {'Nom de famille': 'Boris', 'Prénom': 'Spassky', 'Date de naissance': '18/01/1935',
                'Sexe': 'Homme', 'Rang': 708, 'Numéro associé': 7, 'Score': 0, 'Adversaires': []}
        player8 = {'Nom de famille': 'Hikaru', 'Prénom': 'Nakamura', 'Date de naissance': '28/08/1985',
                'Sexe': 'Homme', 'Rang': 84, 'Numéro associé': 8, 'Score': 0, 'Adversaires': []}
        players_list.append(player1)
        players_list.append(player2)
        players_list.append(player3)
        players_list.append(player4)
        players_list.append(player5)
        players_list.append(player6)
        players_list.append(player7)
        players_list.append(player8)
        return players_list

    def current_score(self, tournament):
        score = 0
        for round_ in tournament.rounds:
            for match in round_.matches:
                if match.player_score_1 != '':
                    if match.player_1 == self.id:
                        score += match.player_score_1
                    elif match.player_2 == self.id:
                        score += match.player_score_1
        return score
    
    def read_players(self):
        all_players = []
        players_from_db = self.p_table.all()
        for pl in players_from_db:
            player = Player.get_player_from_id(pl.doc_id)
            all_players.append(player)
        return all_players
