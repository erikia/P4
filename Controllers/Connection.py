from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()


db_players = cursor.execute('SELECT * FROM players')
# db_players.fetchall()
# for row in db_players.fetchall():
#         print(row)
# print(row[7])

print(db_players.fetchall())

db_tournaments = cursor.execute('SELECT * FROM tournaments')
db_tournaments.fetchall()
# print(cursor.fetchall())

db_rounds = cursor.execute('SELECT * FROM rounds')
db_rounds.fetchall()
# print(cursor.fetchall())

db_matchs = cursor.execute('SELECT * FROM matches')
db_matchs.fetchall()
# print(cursor.fetchall())


connection.commit()

# connection.close()


# class Connection:
#     connection = sqlite3.connect('db.sqlite')
#     cursor = connection.cursor()

#     db_players = cursor.execute('SELECT * FROM players')
#     db_players.fetchall()
#     # for row in db_players.fetchall():
#     #         print(row)
#     # print(row[7])

#     # print(cursor.fetchall())

#     db_tournaments = cursor.execute('SELECT * FROM tournaments')
#     db_tournaments.fetchall()
#     # print(cursor.fetchall())

#     db_rounds = cursor.execute('SELECT * FROM rounds')
#     db_rounds.fetchall()
#     # print(cursor.fetchall())

#     db_matchs = cursor.execute('SELECT * FROM matches')
#     db_matchs.fetchall()
#     # print(cursor.fetchall())


#     connection.commit()

#     connection.close()




######################

# Question: 
# - Fichier connection pour .close()  
# sqlite3.ProgrammingError: Cannot operate on a closed database.

# -     match_1 = Match.Match(players[0], players[1])
# =>   
# match_1 = Match.Match(players.fetchall()[0], players.fetchall()[1])
# IndexError: list index out of range

# - Sauvegarde save_match()
