from workout_program import WorkoutProgram
from database_connection import get_database_connection
import sqlite3

class WorkoutProgramRepository:
    def __init__(self):
        self._connection = get_database_connection()
    
    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("""SELECT workout_program.id, 
                       workout_program.wprogram_name, 
                       wod.wod_name 
                       FROM wod 
                       INNER JOIN workout_program 
                       ON wod.wprogram_id = workout_program.id;
                       """)

        rows = cursor.fetchall()

        return [WorkoutProgram(row["id"],row["wprogram_name"], row["wod_name"]) for row in rows]


    def save_workout_program(self, workout_program):
        """Saves the workout program to the db

        Args:
            workout_program: saved as WorkoutProgram object

        Returns:
            Saves the workout program as WorkoutProgram object
        """

        workout_programs = self.find_all()
        workout_programs.append(workout_program)

    
    def write(self, wprogram_name, wod_name, weekday):
        cursor = self._connection.cursor()

        cursor.execute("""
            INSERT INTO workout_program (wprogram_name, wod_name, weekday)
            VALUES (?, ?, ?)""", 
            (wprogram_name, wod_name, weekday))

        self._connection.commit()
    
    
    
    
    
#workout_program_repository = WorkoutProgramRepository()
#workout_programs =workout_program_repository.find_all()