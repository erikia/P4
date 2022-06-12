from multiprocessing import connection
import sqlite3

connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()


db_players = cursor.execute('SELECT * FROM players')
db_players.fetchall()
# for row in db_players.fetchall():
#         print(row)
# print(row[7])

# print(cursor.fetchall())

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

connection.close()
