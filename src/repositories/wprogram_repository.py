from entities.workout_program import WorkoutProgram
from database_connection import get_database_connection


class WorkoutProgramRepository:
    """Workout program repository
    """
    def __init__(self):
        """Class constructor

        Args:
        _connection = connection to db
        _c = cursor method
        """
        self._connection = get_database_connection()
        self._c = self._connection.cursor()

    def find_wprogram_id_by_user(self, user):
        """Finds workout program is by username

        Args:
            user (User)
        
        Returns:
            wprogram_id (int)
        """

        self._c.execute("""SELECT workout_program.id
                        FROM workout_program
                        INNER JOIN users
                        ON  workout_program.id = users.wprogram_id
                        WHERE users.username = ?""",
                       (user.username(),))

        return self._c.fetchone()[0]

    def find_wprogram_name_by_user(self, user):
        """Find wprogram_name by username

        Args:
            user (User)
        
        Returns:
            wprogram_name (str)
        """

        self._c.execute("""SELECT workout_program.wprogram_name
                        FROM workout_program
                        INNER JOIN users
                        ON  workout_program.id = users.wprogram_id
                        WHERE users.username = ?""",
                       (user.username(),))

        return self._c.fetchone()[0]

    def find_all_distinct_wods_by_wp_id(self, wp_id):
        """Find and return all distinct workout of the days

        Args:
            wp_id (int): workout_program id
        
        Returns:
            list of WorkoutProgram-entities with attributes:
                wprogram_id (int): workout_program.id
                wprogram_name (int): workout_program.wprogram_name
                wod_name (str): wod_id_table.wod_name
                wod_id (int): wod_id_table.id
        """
        self._c.execute("""SELECT DISTINCT workout_program.id,
                       workout_program.wprogram_name, 
                       wod_id_table.wod_name,
                       wod_id_table.id
                       FROM wod_id_table
                       INNER JOIN workout_program 
                       ON wod_id_table.wprogram_id = workout_program.id
                       WHERE workout_program.id = ?
                       """, (wp_id,))

        rows = self._c.fetchall()

        return [WorkoutProgram(row["id"],
                               row["wprogram_name"],
                               row["wod_name"],
                               row[3])
                for row in rows]

    def find_the_wod(self, wod_name):
        """Finds the workout of the day by wod_name

        Args:
            wod_name(str): wod_id_table.wod_name
        
        Returns:
            wod (row object): workout_program.id, wod_name
        """
        self._c.execute("""SELECT workout_program.id,
                       wod_id_table.wod_name, 
                       FROM wod_id_table
                       INNER JOIN workout_program 
                       ON wod_id_table.wprogram_id = workout_program.id
                       WHERE wod_id_table.wod_name=(?);
                       """, (wod_name))

        wod = self._c.fetchone()

        return wod

    def create_new_workout_program(self):
        """Creates a new workout program and return its id

        Returns:
            wprogram_id: the new id from the wprogram just generated
        """
        self._c.execute(
            "INSERT INTO workout_program (wprogram_name) VALUES ('My workout program')")

        self._connection.commit()

        return self._c.lastrowid

    def delete_wod(self, wod_id):
        """Deletes the workout of the day by wod_id

        Args:
            wod_id (int): wod_id_table.id
        """
        self._c.execute("DELETE FROM wod_id_table WHERE id = ?", (wod_id,))

        self._connection.commit()
