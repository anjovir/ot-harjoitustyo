from entities.wod import Wod
from entities.workout_program import WorkoutProgram
from repositories.wod_repository import WodRepository
from repositories.wprogram_repository import WorkoutProgramRepository

class WprogramService:

    def __init__(self):
        self._wpr = WorkoutProgramRepository()
        self._wp = WorkoutProgram(1,self._wpr.find_wprogram_name())

    def initialize_wp_view(self):
        workouts = self._wpr.find_all_distinct_wods()
        if len(workouts) > 0:
            return workouts
        return [self._wp]
    
    def check_if_db_empty(self):
        if len(self._wpr.find_all_distinct_wods()) > 0:
            return False
        return True
        