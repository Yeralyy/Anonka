import sqlite3
import os.path

class AnonkaDB():
    def __init__(self, database="anonka.db"):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "anonka.db")

        self.con = sqlite3.connect(database=db_path)
        self.cur = self.con.cursor()

