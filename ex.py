import sqlite3

connection = sqlite3.connect("dela.sl3", 5)
cur = connection.cursor()
#CREATE TABLE
cur.execute("CREATE TABLE IF NOT EXISTS Delas (id integer primary key autoincrement not null, delos TEXT, status TEXT);")

names = input("Add name: ")
cur.execute(f"INSERT INTO Delas (name) VALUES ('{names}')")