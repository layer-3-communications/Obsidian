import sqlite3

# connect to darabase and returns conneciton
def connect(databasePath):
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()

    return c

