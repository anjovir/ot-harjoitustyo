from tkinter import ttk, constants
from repositories.wod_repository import WodRepository
from entities.wod import Wod
from services.wod_service import WodService

class WodView:

    def __init__(self, root, handle__workout_view, handle_edit_wod, wod_id):
        self._root = root
        self._handle_check_workout = handle__workout_view
        self.hande_edit_wod = handle_edit_wod
        self.wod_id = wod_id
        
        self._frame = None
        self._frame2 = None
        self._frame3 = None
        
        self.rows = [0,1,2,3]
        self.entries = []

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
        self._frame2.pack(fill=constants.X)
        self._frame3.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
        self._frame2.destroy()
        self._frame3.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        self._frame3 = ttk.Frame(master=self._root)

        wod = WodService().initialize_wod_view(self.wod_id)
               
        wod_name = ttk.Label(master=self._frame, text=(f"Wod name: {wod[0][0]}"))
        exercise_name_label = ttk.Label(master=self._frame, text="Exercise")
        sets_label = ttk.Label(master=self._frame, text="Number of sets")
        reps_label = ttk.Label(master=self._frame, text="Number of reps")
        weights_label = ttk.Label(master=self._frame, text="Weights")

        workout_program_button = ttk.Button(
            master=self._frame3,
            text="Back to workout program",
            command=self._handle_check_workout
        )
            
        wod_name.grid(row=0, column=0)        
        exercise_name_label.grid(row=2, column=0)
        sets_label.grid(row=2, column=1)
        reps_label.grid(row=2, column=2)
        weights_label.grid(row=2, column=3)

        workout_program_button.grid(row=0,column=1)       
        
        i = 3
        for ex in wod:
            exercise = ttk.Label(master=self._frame, text= ex[1])
            exercise.grid(row=i, column=0)
            sets = ttk.Label(master=self._frame, text=ex[2])
            sets.grid(row=i, column=1)
            reps = ttk.Label(master=self._frame, text=ex[3])
            reps.grid(row=i, column=2)
            weights = ttk.Label(master=self._frame, text=ex[4])
            weights.grid(row=i, column=3)
            i += 1
            
        wod_edit_button = ttk.Button(
            master=self._frame3,
            text="Edit WOD",
            command=lambda w_id=self.wod_id: self.hande_edit_wod(w_id)
        )

        wod_edit_button.grid(row=0, column=0)
        
        
        