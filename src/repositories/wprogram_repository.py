from entities.workout_program import WorkoutProgram
from database_connection import get_database_connection
import sqlite3

class WorkoutProgramRepository:
    def __init__(self):
        self._connection = get_database_connection()
        self._c = self._connection.cursor()
    
    def find_wprogram_id_by_user(self, user):
        cursor = self._connection.cursor()

        cursor.execute("""SELECT workout_program.id 
                        FROM workout_program
                        INNER JOIN users
                        ON  workout_program.id = users.wprogram_id
                        WHERE users.username = ?""",
                        (user.username,))
        
        return cursor.fetchone()[0]
    
    def find_wprogram_name(self):
        self._c.execute("SELECT wprogram_name FROM workout_program WHERE id=1")
        return self._c.fetchone()[0]
    
    def find_all_distinct_wods_by_wp_id(self, wp_id):
        cursor = self._connection.cursor() 

        cursor.execute("""SELECT DISTINCT workout_program.id, 
                       workout_program.wprogram_name, 
                       wod_id_table.wod_name,
                       wod_id_table.id
                       FROM wod_id_table
                       INNER JOIN workout_program 
                       ON wod_id_table.wprogram_id = workout_program.id
                       WHERE workout_program.id = ?
                       """, (wp_id,))

        rows = cursor.fetchall()

        return [WorkoutProgram(row["id"],row["wprogram_name"], row["wod_name"], row[3]) for row in rows]
    
    def find_the_wod(self, wod_name):
        cursor = self._connection.cursor()

        cursor.execute("""SELECT workout_program.id,  
                       wod_id_table.wod_name, 
                       FROM wod_id_table
                       INNER JOIN workout_program 
                       ON wod_id_table.wprogram_id = workout_program.id
                       WHERE wod_id_table.wod_name=(?);
                       """,(wod_name))

        wod = cursor.fetchone()

        return wod
    
    def create_new_workout_program(self):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO workout_program (wprogram_name) VALUES ('My workout program')")

        self._connection.commit()

        id = cursor.lastrowid

        return id
    