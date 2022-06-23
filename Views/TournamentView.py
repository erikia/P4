from Models import Tournament


class TournamentView:
    """La classe qui demande des informations sur le tournoi à l'utilisateur"""

    def ask_tournament(self):
        """Retourne un dictionnaire des informations entrées par l'utilisateur sur un tournois"""
        print(
            f"Veuillez entrer les informations sur le nouveau tournoi"
        )
        print("")
        informations_questions = {}
        informations_rounds_sqlite = {}

        questions = [
            "Nom/ID du tournois",
            "Adresse du tournois",
            "Les dates du tournois",
            "Contrôle du temps",
            "Commentaire",
        ]

        for i in questions:
            informations_questions[i] = input(f"{i}:  ")

        informations_rounds_sqlite["Nom/ID du tournois"] = informations_questions["Nom/ID du tournois"]
        informations_rounds_sqlite["Adresse du tournois"] = informations_questions["Adresse du tournois"]
        informations_rounds_sqlite["Les dates du tournois"] = informations_questions["Les dates du tournois"]
        informations_rounds_sqlite["Nombre total de rounds"] = 4
        informations_rounds_sqlite["Nombre du round en cours"] = 0
        informations_rounds_sqlite["Contrôle du temps"] = informations_questions["Contrôle du temps"]
        informations_rounds_sqlite["Numbre totals de joeurs"] = 8
        informations_rounds_sqlite["Commentaire"] = informations_questions["Commentaire"]
        informations_rounds_sqlite["Rounds"] = []
        print("")

        return informations_rounds_sqlite
    