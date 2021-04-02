import sqlite3


"""Работа с базой данных"""


def createbase():
    conn = sqlite3.connect("moneybase.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE money
                  (names text, short text, cost text)
               """)


def insertbase(names, shorts, costs):
    conn = sqlite3.connect("moneybase.db")
    cursor = conn.cursor()
    for i in range(len(names)):
        data = (names[i].lower(), shorts[i].lower(), costs[i].lower())
        cursor.execute('INSERT INTO money VALUES (?,?,?)', data)
    conn.commit()


def updatebase(names, shorts, costs):
    conn = sqlite3.connect("moneybase.db")
    cursor = conn.cursor()
    for i in range(len(names)):
        data = (costs[i].lower(), shorts[i].lower())
        cursor.execute('Update money set cost = ? where short = ?', data)
    conn.commit()


def chekbase(message):
    conn = sqlite3.connect("moneybase.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT cost FROM money WHERE names=? OR short =?", (message.lower(), message.lower(),))
    return cursor.fetchall()
