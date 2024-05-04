from entities.wod import Wod
from repositories.wod_repository import WodRepository
from repositories.wprogram_repository import WorkoutProgramRepository
from services.user_service import user_service


class WodService:
    """Workout of the day service layer
    """
    def __init__(self):
        """Constructor
        """
        self._wr = WodRepository()
        self._wod = Wod()
        self._wprogram_id = WorkoutProgramRepository().find_wprogram_id_by_user(
            user_service.get_current_user())

    def initialize_wod_view(self, wod_id):
        """Initializes wod_view

        Args:
            wod_id (int): to specify the wod

        Returns:
            content (list): all wod exercises as a list
        """
        wod = self._wr.find_current_wod_by_id(wod_id)
        content = []
        for exercise in wod:
            content.append(exercise.return_args())
        return content

    def save_new_wod(self, entries):
        """Save new workout of the day to the db

        Args:
            entries (list): contains wod attributes
        """

        for entry in entries:
            self._wr.write(entry[0],
                           self._wprogram_id,
                           entry[1],
                           entry[2],
                           entry[3],
                           entry[4])

    def update_wod(self, entries):
        """Updates an existing workout of the day

        Args:
            entries (list): contains wod attributes
        """
        row_ids = []
        for entry in entries:
            row_ids.append(self._wr.edit(entry[0],
                          entry[1],
                          entry[2],
                          self._wprogram_id,
                          entry[3],
                          entry[4],
                          entry[5],
                          entry[6]))
        
        return row_ids
        

    def return_last_id(self, wod_id):
        """Return wod_exercises new id when adding new row in the ui

        Args:
            wod_id (int): id of wod

        Returns:
            int: wod_exercises.id
        """
        return self._wr.add_new_row_when_updating(wod_id)
