from wod import Wod
from database_connection import get_database_connection
import sqlite3

class WodRepository:
    def __init__(self):
        self._connection = get_database_connection()
    
    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM wod")

        rows = cursor.fetchall()

        return [Wod(row["wod_name"], row["exercise"], row["sets"], row["reps"], row["weights"]) for row in rows]
    
    def write(self, wod_name, wprogram_id, exercise, sets, reps, weights):
        cursor = self._connection.cursor()

        cursor.execute("""
            INSERT INTO wod (wod_name, wprogram_id, exercise, sets, reps, weights)
            VALUES (?, ?, ?, ?, ?, ?)""", 
            (wod_name, wprogram_id, exercise, sets, reps, weights))

        self._connection.commit()
    