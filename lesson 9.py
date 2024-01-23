import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()
#CREATE TABLE
#cur.execute("CREATE TABLE Users (name TEXT);")

#INSERT
#names = input("Add name: ")
#cur.execute(f"INSERT INTO Users (name) VALUES ('{names}')")

#SELECT
cur.execute("SELECT rowid, name FROM Users;")
connection.commit()

res = cur.fetchall()
print(res)

connection.close()