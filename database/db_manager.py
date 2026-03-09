import sqlite3

class DBManager:

    def __init__(self):
        self.conn = sqlite3.connect("akademi.db")
        self.cursor = self.conn.cursor()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
