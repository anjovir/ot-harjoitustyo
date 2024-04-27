from entities.workout_program import WorkoutProgram
from repositories.wprogram_repository import WorkoutProgramRepository
from services.user_service import user_service


class WprogramService:

    def __init__(self):
        self._wpr = WorkoutProgramRepository()
        self._user = user_service.get_current_user()
        self._wp_id = self._wpr.find_wprogram_id_by_user(self._user)
        self._wp = WorkoutProgram(self._wp_id, self._wpr.find_wprogram_name_by_user(self._user))

    def initialize_wp_view(self):
        workouts = self._wpr.find_all_distinct_wods_by_wp_id(self._wp_id)
        if len(workouts) > 0:
            return workouts
        return [self._wp]

    def check_if_db_empty(self):
        return not len(self._wpr.find_all_distinct_wods_by_wp_id(self._wp_id)) > 0

    def delete_wod(self, wod_id):
        self._wpr.delete_wod(wod_id)
