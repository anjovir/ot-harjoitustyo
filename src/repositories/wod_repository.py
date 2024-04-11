from entities.wod import Wod
from database_connection import get_database_connection
import sqlite3


class WodRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def find_current_wod_by_id(self, wod_id):

        cursor = self._connection.cursor()
        cursor.execute("""SELECT wod_id_table.wod_name,
                       wod_id_table.id,
                       wod_exercises.id,
                       wod_exercises.exercise,
                       wod_exercises.sets,
                       wod_exercises.reps,
                       wod_exercises.weights
                       FROM wod_id_table
                       INNER JOIN wod_exercises 
                       ON wod_id_table.id = wod_exercises.wod_id
                       WHERE wod_id_table.id = ?;""",
                       (wod_id,))

        rows = cursor.fetchall()

        return [Wod(row["wod_name"], row["exercise"], row["sets"], row["reps"], row["weights"], row[1], row[2]) for row in rows]

    def write(self, wod_name, wprogram_id, exercise, sets, reps, weights):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT wod_name FROM wod_id_table WHERE wod_name=?", (wod_name,))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("""
                INSERT INTO wod_id_table (wprogram_id, wod_name)
                VALUES (?, ?)""",
                           (wprogram_id, wod_name))

        cursor.execute(
            "SELECT id FROM wod_id_table WHERE wod_name = ?", (wod_name,))

        wod_id = cursor.fetchone()["id"]

        cursor.execute("""
            INSERT INTO wod_exercises (wod_id,exercise, sets, reps, weights)
            VALUES (?, ?, ?, ?, ?)""",
                       (wod_id, exercise, sets, reps, weights))

        self._connection.commit()

    def return_last_exercise_id(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id FROM wod_exercises")
        return cursor.fetchall()[-1]

    def add_new_row_when_updating(self, wod_id):
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO wod_exercises 
                       (wod_id, exercise, sets, reps, weights) 
                       VALUES (?, "", "", "", "")""",
                       (wod_id,))
        self._connection.commit()

        cursor.execute("SELECT id FROM wod_exercises")

        last_id = cursor.fetchall()[-1]
        return last_id["id"]

    def edit(self, row_id, wod_id, wod_name, wprogram_id, exercise, sets, reps, weights):
        cursor = self._connection.cursor()

        cursor.execute("""UPDATE wod_id_table 
                       SET wod_name = ?,
                       wprogram_id = ?
                       WHERE id = ?""",
                       (wod_name, wprogram_id, wod_id))

        self._connection.commit()

        cursor.execute("""
                    UPDATE wod_exercises 
                    SET exercise = ?,
                       sets = ?, 
                       reps = ?,
                       weights = ?
                       WHERE id = ?
            """,
                       (exercise, sets, reps, weights, row_id))

        self._connection.commit()
