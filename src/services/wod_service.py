from entities.wod import Wod
from entities.workout_program import WorkoutProgram
from repositories.wod_repository import WodRepository
from repositories.wprogram_repository import WorkoutProgramRepository

class WodService:
    def __init__(self):
        self._wod_repo = WodRepository()
        self._wod = Wod()
    
    def initialize_wod_view(self, wod_id):
        wod = self._wod_repo.find_current_wod_by_id(wod_id)
        content = []
        for exercise in wod:
            content.append(exercise.return_args())
        return content

        
    def save_new_wod(self, entries):

        wprogram_id = 1
        
        for entry in entries:
            exercise = entry[1].get()
            sets = entry[2].get()
            reps = entry[3].get()
            weights = entry[4].get()
            self._wod_repo.write(self.wod_name_entry.get(),
                      wprogram_id,
                      exercise,
                      sets,
                      reps,
                      weights)
    