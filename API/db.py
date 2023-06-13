import sqlite3
DATABASE_NAME = "games.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    db = get_db()
    cursor = db.cursor()
    f = open('tabla.sql')
    sql = f.read()
    cursor.executescript(sql)