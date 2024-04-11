from entities.user import User
from database_connection import get_database_connection
from repositories.wprogram_repository import WorkoutProgramRepository


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    def __init__(self):
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
        username = user.username
        password = user.password

        cursor = self._connection.cursor()

        wprogram_id = self.wpr.create_new_workout_program()

        cursor.execute(
            "INSERT INTO users (username, password, wprogram_id) VALUES (?, ?, ?)",
            (username, password, wprogram_id)
        )

        self._connection.commit()

        return user

    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM users")

        self._connection.commit()


# user_repository = UserRepository(get_database_connection())
