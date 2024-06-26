from entities.workout_program import WorkoutProgram
from repositories.wprogram_repository import WorkoutProgramRepository
from services.user_service import user_service


class WprogramService:
    """Workout program service
    """

    def __init__(self):
        """Constructor
        """
        self._wpr = WorkoutProgramRepository()
        self._user = user_service.get_current_user()
        self._wp_id = self._wpr.find_wprogram_id_by_user(self._user)
        self._wp = WorkoutProgram(
            self._wp_id, self._wpr.find_wprogram_name_by_user(self._user))

    def initialize_wp_view(self):
        """Initializes workout program view
            If there are some wods already created for the user
            then the method returns those
            Otherwise returns default workout view for the user

        Returns:
            list: wod list
            WorkoutProgram: WorkoutProgram object
        """
        workouts = self._wpr.find_all_distinct_wods_by_wp_id(self._wp_id)
        if len(workouts) > 0:
            return workouts
        return [self._wp]

    def check_if_db_empty(self):
        """Checks if the database is empty

        Returns:
            bool: false if db is empty
        """
        return not len(self._wpr.find_all_distinct_wods_by_wp_id(self._wp_id)) > 0

    def delete_wod(self, wod_id):
        """Deletes workout of the day"""

        self._wpr.delete_wod(wod_id)
