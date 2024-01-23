import sqlite3

connection = sqlite3.connect("IMBA.sl3", 5)
cur = connection.cursor()

#CREATE TABLE
cur.execute("CREATE TABLE IF NOT EXISTS Users (id integer primary key autoincrement not null, logit TEXT, password TEXT);")
connection.commit()
connection.close()

def login():
    print("Меню входа в аккаунт.")
    log = input("Введите логин БЫСТРО: ")
    passw = input("Введите пароль БЫСТРО: ")
    connection = sqlite3.connect("IMBA.sl3", 5)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM Users WHERE logit='{log}';")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        print("Такого чувака не существует!!!")
        exit(0)
    else:
        res = list(res[0])
        if res[2] == passw:
            print("Вы вошли в аккаунт.")

def register():
    print("Меню регистрации.")
    log = input("Введите логин БЫСТРО: ")
    connection = sqlite3.connect("IMBA.sl3", 5)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM Users WHERE logit='{log}';")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        passw = input("ВВЕДИТЕ ПАРОЛЬ БЫСТРО: ")
        cur.execute(f"INSERT INTO Users (logit, password) VALUES ('{log}', '{passw}');")
        connection.commit()
        print("ВЫ ДОБАВЛЕНЫ.")
    else:
        print("ТАКИЕ УЖЕ ЕСТЬ!!!")
        exit(0)

choise = int(input("1. Войти.\n2. Зарегистрироваться.\n"))
if choise == 1:
    login()
elif choise == 2:
    register()
else:
    print("НЕПРАВИЛЬНО!!!!!!!!")
    exit(0)