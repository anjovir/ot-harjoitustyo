import unittest
from entities.workout_program import WorkoutProgram


class TestWorkoutProgram(unittest.TestCase):
    def setUp(self):
        pass

    def test_constructor_returns_the_right_id(self):
        workout_program = WorkoutProgram(1, "Testiohjelma", "Testitreeni", 1)
        answer = str(workout_program)

        self.assertEqual(answer, f"""WorkoutProgram: (id=1, wprogram_name=Testiohjelma, wod_name=Testitreeni, wod_id=1)""")
