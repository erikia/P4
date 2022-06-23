# P4
Projet 4 : Développez un programme logiciel en Python

Ce projet a pour but de créer un nouveau logiciel de tournoi pour une association d'echecs, qui leur permettrait de gérer leurs événements hors ligne, et de produire des rapports..

# Processus
## Modèle MVC
Le script fait une requête sur le site books.toscrape.com. Si la requête est accessible, le script récupérer toutes les 50 catégories puis crée ensuite une liste pour les répertorier. Par la suite, le script va pouvoir créer un fichier CSV par catégorie où nous allons récupérer chacun des livres dans leurs dossiers respectifs. De plus, le script va récupérer pour chaque catégorie toutes les pages selon la quantité de livres.

## POO : Programmation orientée objet
Nous allons ensuite placer les liens des livres dans un dictionnaire qui procède ensuite au scrapping de toutes les données que nous placerons voir dans un fichier csv pour chaque page de livres.

Dans ce programme, les fonctionnalités du menu sont :

-Commencer un nouveau tournois
-Reprendre un ancien tournois
-Affichier les rapports


# Utilisation
## Création de l'environnement virtuel
Pour la mise en palce de l'environnement virtuel :

### Sur Windows :
Dans le Windows Powershell il faudra cloner le git.

Récupération du projet
    $ git clone hhttps://github.com/erikia/P4.git
Activer l'environnement virtuel
    $ cd P2_OC 
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
    $ cd P2_OC 
    $ python3 -m venv env 
    $ source env/bin/activate
Installer les modules
    $ pip install -r requirements.txt
Executer le programme
    $ python3 main.py