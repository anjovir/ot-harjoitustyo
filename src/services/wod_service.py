from entities.wod import Wod
from entities.workout_program import WorkoutProgram
from repositories.wod_repository import WodRepository
from repositories.wprogram_repository import WorkoutProgramRepository
from services.user_service import user_service

class WodService:
    def __init__(self):
        self._wr = WodRepository()
        self._wod = Wod()
    
    def initialize_wod_view(self, wod_id):
        wod = self._wr.find_current_wod_by_id(wod_id)
        content = []
        for exercise in wod:
            content.append(exercise.return_args())
        return content

    def save_new_wod(self, entries):
        wprogram_id = WorkoutProgramRepository().find_wprogram_id_by_user(user_service.get_current_user())
        
        for entry in entries:
            self._wr.write(entry[0],
                      wprogram_id,
                      entry[1],
                      entry[2],
                      entry[3],
                      entry[4])
    
    def update_wod(self, entries):
        wprogram_id = 1

        for entry in entries:
            self._wr.edit(entry[0],
                    entry[1],
                    entry[2],
                    wprogram_id,
                    entry[3],
                    entry[4],
                    entry[5],
                    entry[6])
    
    def return_last_id(self, wod_id):
        return self._wr.add_new_row_when_updating(wod_id)