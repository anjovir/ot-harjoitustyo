from entities.user import User
from database_connection import get_database_connection
from repositories.wprogram_repository import WorkoutProgramRepository


def get_user_by_row(row):
    """Build user

    Args:
        row (sql row-object)

    Returns:
        User: [username, password, id]
    """
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

    def find_by_username(self, username):
        """Find a user by username, build it with get_user_by_row

        Args:
            username (str)

        Returns:
            User: [username, password, id]
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        row = cursor.fetchone()
        return get_user_by_row(row)

    def create(self, user):
        """Create a new user, 
           fetch username and password from the entity
           and save them to the db.
           Create new workout program which will be referenced
           in the users table.
           Update User entity with the new user id

        Args:
            user: User-entity 

        Returns:
            user: User-entity
        """
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
        """Deletes all the data related to the user.
            First we fetch wprogram_id from users-table.
            Then we delete the workout_program which cascades
            to all other tables.

        Args:
            user (User)
        """
        cursor = self._connection.cursor()
        user_id = user.user_id()

        cursor.execute("SELECT wprogram_id FROM users WHERE id=?", (user_id, ))
        wprogram_id = cursor.fetchone()[0]

        cursor.execute("DELETE FROM workout_program WHERE id=?", (wprogram_id, ))

        self._connection.commit()


# user_repository = UserRepository(get_database_connection())
