from entities.workout_program import WorkoutProgram
from repositories.wprogram_repository import WorkoutProgramRepository
from services.user_service import user_service


class WprogramService:

    def __init__(self):
        self._wpr = WorkoutProgramRepository()
        self._wp = WorkoutProgram(1, self._wpr.find_wprogram_name())

    def initialize_wp_view(self):
        wp_id = self._wpr.find_wprogram_id_by_user(
            user_service.get_current_user())
        workouts = self._wpr.find_all_distinct_wods_by_wp_id(wp_id)
        if len(workouts) > 0:
            return workouts
        return [self._wp]

    def check_if_db_empty(self):
        wp_id = self._wpr.find_wprogram_id_by_user(
            user_service.get_current_user())
        if len(self._wpr.find_all_distinct_wods_by_wp_id(wp_id)) > 0:
            return False
        return True
