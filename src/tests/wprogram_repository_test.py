import unittest
from repositories.wprogram_repository import WorkoutProgramRepository
from repositories.user_repository import UserRepository
from entities.user import User
from services.user_service import user_service


class TestWorkoutProgramRepository(unittest.TestCase):
    def setUp(self):
        self._wpr = WorkoutProgramRepository()
        self._ur = UserRepository()
        self._user = User("Simo", "simo1", 1)

        user_service.login("Simo", "simo1")
        self._username = user_service.get_current_user()

        cursor = self._wpr._connection.cursor()

        cursor.execute("SELECT id FROM workout_program")
        wpr_id = cursor.fetchone()
        self._wod_name = "Testitreeni"
        self._wprogram_id = wpr_id[0]
        self._exercise = "Testipenkki"
        self._sets = 3
        self._reps = 10
        self._weights = 70
        cursor = self._wpr._connection.cursor()
        self._exercise_id = 1

    def test_find_all_distinct_wods_by_wp_id(self):
        answer = self._wpr.find_all_distinct_wods_by_wp_id(self._wprogram_id)
        self.assertEqual(answer[0].id(), 1)

    def test_find_wprogram_id_by_user(self):
        answer = self._wpr.find_wprogram_id_by_user(self._username)
        self.assertEqual(answer, 1)
