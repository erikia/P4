class TournamentView:
    """La classe qui demande des informations sur le tournoi à l'utilisateur"""

    def ask_tournament(tournament_dict):
        """Retourne un dictionnaire des informations du tournois"""
        print("Veuillez entrer les informations sur le nouveau tournoi")
        print("")
        tournament_dict = {}
        informations_rounds_sqlite = {}

        questions = [
            "Nom/ID du tournois",
            "Adresse du tournois",
            "Les dates du tournois",
            "Contrôle du temps",
            "Commentaire",
        ]

        for i in questions:
            tournament_dict[i] = input(f"{i}:  ")

        informations_rounds_sqlite["Nom/ID du tournois"] = tournament_dict[
            "Nom/ID du tournois"
        ]
        informations_rounds_sqlite["Adresse du tournois"] = tournament_dict[
            "Adresse du tournois"
        ]
        informations_rounds_sqlite["Les dates du tournois"] = tournament_dict[
            "Les dates du tournois"
        ]
        informations_rounds_sqlite["Nombre total de rounds"] = 4
        informations_rounds_sqlite["Nombre du round en cours"] = 0
        informations_rounds_sqlite["Contrôle du temps"] = tournament_dict[
            "Contrôle du temps"
        ]
        informations_rounds_sqlite["Numbre totals de joeurs"] = 8
        informations_rounds_sqlite["Commentaire"] = tournament_dict[
            "Commentaire"
            ]
        informations_rounds_sqlite["Rounds"] = []
        print("")

        return informations_rounds_sqlite
