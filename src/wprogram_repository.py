from workout_program import WorkoutProgram
from database_connection import get_database_connection
import sqlite3

class WorkoutProgramRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM workout_program")

        rows = cursor.fetchall()

        return [WorkoutProgram(row["wprogram_name"], row["wod_name"], row["weekday"]) for row in rows]

workout_program_repository = WorkoutProgramRepository(get_database_connection())
workout_programs =workout_program_repository.find_all()