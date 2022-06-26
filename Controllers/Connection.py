import sqlite3

try:
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()

    db_players = cursor.execute("SELECT * FROM players").fetchall()

    db_tournaments = cursor.execute("SELECT * FROM tournaments").fetchall()

    db_rounds = cursor.execute("SELECT * FROM rounds").fetchall()

    db_matchs = cursor.execute("SELECT * FROM matches").fetchall()

    connection.commit()
    print("Connexion SQLite ouverte")

except sqlite3.Error as error:
    print("Erreur lors de la connexion à la base de donnée", error)


def close_db():
    try:
        connection.close()
        print("Connexion SQLite est fermée")

    except sqlite3.Error as error:
        print("Erreur lors de la fermeture à la base de donnée", error)
