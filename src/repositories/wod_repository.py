from entities.wod import Wod
from database_connection import get_database_connection


class WodRepository:
    """Workout of the day repository
    """
    def __init__(self):
        """Class constructor, connection to db
        """
        self._connection = get_database_connection()

    def find_current_wod_by_id(self, wod_id):
        """Finds the current workout of the day by its id-number
            and then returns it

        Args:
            wod_id (int)

        Returns:
            Wod-entity
        """

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

        return [Wod(row["wod_name"],
                    row["exercise"],
                    row["sets"],
                    row["reps"],
                    row["weights"],
                    row[1], row[2])
                for row in rows]

    def write(self, wod_name, wprogram_id, exercise, sets, reps, weights):
        """Writes a workout of the day to the db

        Args:
            wod_name (str)
            wprogram_id (int)
            exercise (str)
            sets (str)
            reps (str)
            weights (str)
        
        """

        cursor = self._connection.cursor()
        cursor.execute("""
                INSERT INTO wod_id_table (wprogram_id, wod_name)
                VALUES (?, ?)""",
                           (wprogram_id, wod_name))

        wod_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO wod_exercises (wod_id,exercise, sets, reps, weights)
            VALUES (?, ?, ?, ?, ?)""",
                       (wod_id, exercise, sets, reps, weights))

        self._connection.commit()

    def return_last_exercise_id(self):
        """Returns the last id from wod_exercises table

        Returns:
            id(int)
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT id FROM wod_exercises")
        return cursor.fetchall()[-1]

    def add_new_row_when_updating(self, wod_id):
        """Adds a new blank row to the wod_exercises table
            when a user adds a new row in the ui

        Args:
            wod_id(int)
        
        Returns:
            id (int): id from the added row in wod_exercises
        """
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO wod_exercises
                       (wod_id, exercise, sets, reps, weights) 
                       VALUES (?, "", "", "", "")""",
                       (wod_id,))
        self._connection.commit()
        return cursor.lastrowid

    def edit(self,
             row_id,
             wod_id,
             wod_name,
             wprogram_id,
             exercise,
             sets,
             reps,
             weights):

        """Updates the db when editing an existing wod.
            First update wod_id_table
            then wod_exercises table

        Args:
            row_id (int): wod exercise id
            wod_id  (int): wod_id_table id
            wod_name (str): wod_id_table wod_name
            wprogram_id (int): wod_id_table wprogram_id
            exercise (str): wod_exercises exercise
            sets (str): wod_exercises sets
            reps (str): wod_exercises reps
            weights (str): wod_exercises weights
        """
        cursor = self._connection.cursor()

        cursor.execute("""SELECT wod_id FROM wod_exercises
                       WHERE id = ?""", (row_id,))
        
        w_id = cursor.fetchone()
        
        
        if not w_id or (isinstance(w_id[0], int) and w_id[0] != wod_id):
            row_id = self.add_new_row_when_updating(wod_id)

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
