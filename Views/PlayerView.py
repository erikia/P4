class PlayersView:
    """La classe qui permet à l'utilisateur de rentrer les informations du joeurs"""

    def create_players_input(self):
        """Retourne un dictionnaire des informations entrées par l'utilisateur sur les joueurs"""

        print(
            f"Entrée des informations sur les joueurs"
        )

        list_players_informations = []
        for i in range(8):
            player = {}
            print(
                "Veuillez entrer les informations du numéro de joueur " + str(i + 1) + ":")
            player["Nom de famille"] = PlayersView().display_menu_name()
            player["Prénom"] = PlayersView().display_menu_first_name()
            player["Date de naissance"] = PlayersView().display_menu_date()
            player["Sexe"] = PlayersView().display_menu_gender()
            player["Rang"] = PlayersView().display_menu_rank()
            player["Numéro associé"] = int(i + 1)
            player["Score"] = 0
            player["Adversaires"] = []

            list_players_informations.append(player)
            print("")

        return list_players_informations

    def verify_user_input(self, msg_display, msg_error, value_type, input=None, default_value=None):
        """Vérifie les entrées des utilisateurs sur les joueurs et retourne les messages d'erreurs"""

        while True:
            value = input(msg_display)
            if value_type == "numeric":
                if value.isnumeric():
                    value = int(value)
                    return value
                else:
                    print(msg_error)
                    continue
            if value_type == "num_superior":
                if value.isnumeric():
                    value = int(value)
                    if value >= default_value:
                        return value
                    else:
                        print(msg_error)
                        continue
                else:
                    print(msg_error)
                    continue
            if value_type == "string":
                try:
                    float(value)
                    print(msg_error)
                    continue
                except ValueError:
                    return value
            elif value_type == "date":
                if self.is_date_valid(value):
                    return value
                else:
                    print(msg_error)
                    continue
            elif value_type == "selection":
                if value in input:
                    return value
                else:
                    print(msg_error)
                    continue

    @staticmethod
    def is_date_valid(value_to_test):
        if "-" not in value_to_test:
            return False
        else:
            splitted_date = value_to_test.split("-")
            for date in splitted_date:
                if not date.isnumeric():
                    return False
            return True

    def display_menu_name(self):
        """Retourne l'input du nom de famille d'un joueur"""

        name = input("""Nom du joueur:\n> """)
        return {
            "Nom de famille": name
        }

    def display_menu_first_name(self):
        """Retourne l'input du prénom d'un joueur"""

        first_name = input("""Prénom du joueur:\n> """)
        return {
            "Prénom": first_name
        }

    def display_menu_date(self):
        """Retourne l'input de la date de naissance d'un joueur"""

        date = PlayersView().verify_user_input(
            msg_display="Date de naissance (format DD-MM-YYYY):\n> ",
            msg_error="Veuillez entrer une date au format valide: DD-MM-YYYY",
            value_type="date"
        )
        return {
            "Date de naissance": date
        }

    def display_menu_gender(self):
        """Retourne l'input du sexe d'un joueur"""

        gender = PlayersView().verify_user_input(
            msg_display="Sexe (H ou F):\n> ",
            msg_error="Veuillez entrer H ou F",
            value_type="selection",
            input=["H", "h", "F", "f"]
        ).upper()

        return {
            "Sexe": gender
        }

    def display_menu_rank(self):
        """Retourne l'input du rang d'un joueur"""

        rank = PlayersView().verify_user_input(
            msg_display="Rang:\n> ",
            msg_error="Veuillez entrer une valeur numérique valide.",
            value_type="numeric"
        )

        return {
            "Rang": rank
        }
