import unittest
from repositories.wprogram_repository import WorkoutProgramRepository
from initialize_database import initialize_test_database

class TestWodRepository(unittest.TestCase):
    def setUp(self):
        initialize_test_database()
        self._wpr = WorkoutProgramRepository()
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


