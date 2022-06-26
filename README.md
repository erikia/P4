# P4
Projet 4 : Développez un programme logiciel en Python

Ce projet a pour but de créer un nouveau logiciel de tournoi pour une association d'echecs, qui leur permettrait de gérer leurs événements hors ligne, et de produire des rapports..

# Processus
## Modèle MVC
Ce projet est construit au modèle de conception MVC (Modèle, Vue, Controller) 
L'application se sert de classes qui serviront de modèles pour le tournoi, les joueurs, les matchs et les rondes.
Le paquet contrôleurs servira pour accepter les données de l'utilisateur, produire les résultats des matchs, lancer de nouveaux tournois.
En plus de cela, il y a le paquet de la vue pour afficher les classements, les appariements et d'autres statistiques.

## POO : Programmation orientée objet
Ce projet à était demandé d'etre travaillé en programmation orientée objet (POO) est un modèle de programmation informatique qui met en œuvre une conception basée sur les objets. 

## Flake
Ce projet dispose d'un répertoire contenant un fichier HTML généré par flake8-html.


Dans ce programme, les fonctionnalités du menu sont :
```
Commencer:      "Commencer un nouveau tournoi",
Rapports:       "Afficher les rapports",
Supprimer:      "Effacer les informations précédentes présentes sur la console",
Quitter:        "Quitter le programme"
```

# Utilisation
## Création de l'environnement virtuel
Pour la mise en palce de l'environnement virtuel :

### Sur Windows :
Dans le Windows Powershell il faudra cloner le git.

Récupération du projet
        
        $ git clone hhttps://github.com/erikia/P4.git
Activer l'environnement virtuel
        
        $ cd P4
        $ python -m venv env 
        $ ~env\scripts\activate
Installer les modules

        $ pip install -r requirements.txt
Executer le programme

        $ python main.py

----------------------------------------------
### Sur MacOS ou Linux :
Dans le terminal, il faudra cloner le git.

Récupération du projet

        $ git clone https://github.com/erikia/P4.git
Activer l'environnement virtuel

        $ cd P4
        $ python3 -m venv env 
        $ source env/bin/activate
Installer les modules

        $ pip install -r requirements.txt
Executer le programme

        $ python3 main.py