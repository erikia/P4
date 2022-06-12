from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('tournament.db')
cursor = connection.cursor()

cursor.execute(
    "create table players (nom text, prenom text, date text, sexe text, rang integer,numéro integer,score integer)")


players_list = [
    ('Dubois', 'Charles', '05/04/1995', 'Homme', 356, 1, 0),
    ('Alcor', 'David', '17/12/1945', 'Homme', 287, 2, 0),
    ('Garry', 'Kasparov', '1/06/1967', 'Homme', 593, 3, 0),
    ('Judit', 'Polgar', '1/06/1967', 'Femme', 407, 4, 0),
    ('Fabiano', 'Caruana', '15/11/1978', 'Homme', 57, 5, 0),
    ('Anish', 'Giri', '26/03/2000', 'Homme', 68, 6, 0),
    ('Boris', 'Spassky', '18/01/1935', 'Homme', 708, 7, 0),
    ('Hikaru', 'Nakamura', '28/08/1985', 'Homme', 84, 8, 0)
]
# Print database 
for row in cursor.executemany("insert into players values (?,?,?,?,?,?,?)", players_list)
        print(row)

# print specific row
cursor.execute("select * from players where nom=n",{"n": "dubois"} )

connection.close()
