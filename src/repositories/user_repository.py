from entities.user import User
from database_connection import get_database_connection
from repositories.wprogram_repository import WorkoutProgramRepository


def get_user_by_row(row):
    return User(row["username"], row["password"], row["id"]) if row else None


class UserRepository:
    """Class for the user repository"""
    def __init__(self):
        """Class constructor

        Args: 
        _connection = connection to the db
        wpr = WorkoutProgramRepository-object

        """

        self._connection = get_database_connection()
        self.wpr = WorkoutProgramRepository()

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        row = cursor.fetchone()
        return get_user_by_row(row)

    def create(self, user):
        username = user.username()
        password = user.password()

        cursor = self._connection.cursor()

        wprogram_id = self.wpr.create_new_workout_program()

        cursor.execute(
            "INSERT INTO users (username, password, wprogram_id) VALUES (?, ?, ?)",
            (username, password, wprogram_id)
        )

        self._connection.commit()

        new_user_id = cursor.lastrowid

        user.update_user_id(new_user_id)

        return user

    def delete_user_data(self, user):
        cursor = self._connection.cursor()
        user_id = user.user_id()

        cursor.execute("SELECT wprogram_id FROM users WHERE id=?", (user_id, ))
        wprogram_id = cursor.fetchone()[0]

        cursor.execute("DELETE FROM workout_program WHERE id=?", (wprogram_id, ))
        cursor.execute("DELETE FROM users WHERE id=?", (user_id, ))

        self._connection.commit()


# user_repository = UserRepository(get_database_connection())
