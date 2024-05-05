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

        self._frame1 = None
        self._frame2 = None
        self._frame3 = None

        self.rows = [0, 1, 2, 3]
        self.entries = []
        self._wod = WodService().initialize_wod_view(self.wod_id)

        self._initialize()

    def pack(self):
        self._frame1.pack(fill=constants.X)
        self._frame2.pack(fill=constants.X)
        self._frame3.pack(fill=constants.X)

    def destroy(self):
        self._frame1.destroy()
        self._frame2.destroy()
        self._frame3.destroy()
    
    def _initialize_header(self):
        wod_name = ttk.Label(master=self._frame1,
                             text=(f"Wod name: {self._wod[0][0]}"))
        wod_name.grid(row=0, column=0)

    def _initialize_main_content(self):
        exercise_name_label = ttk.Label(master=self._frame2, text="Exercise")
        sets_label = ttk.Label(master=self._frame2, text="Number of sets")
        reps_label = ttk.Label(master=self._frame2, text="Number of reps")
        weights_label = ttk.Label(master=self._frame2, text="Weights")

        
        exercise_name_label.grid(row=0, column=0)
        sets_label.grid(row=0, column=1)
        reps_label.grid(row=0, column=2)
        weights_label.grid(row=0, column=3)

        i = 1
        for ex in self._wod:
            exercise = ttk.Label(master=self._frame2, text=ex[1])
            exercise.grid(row=i, column=0)
            sets = ttk.Label(master=self._frame2, text=ex[2])
            sets.grid(row=i, column=1)
            reps = ttk.Label(master=self._frame2, text=ex[3])
            reps.grid(row=i, column=2)
            weights = ttk.Label(master=self._frame2, text=ex[4])
            weights.grid(row=i, column=3)
            i += 1
        
        

    def _initialize_footer(self):
        workout_program_button = ttk.Button(
            master=self._frame3,
            text="Back to workout program",
            command=self._handle_check_workout
        )
        workout_program_button.grid(row=0, column=1)

        wod_edit_button = ttk.Button(
            master=self._frame3,
            text="Edit WOD",
            command=lambda w_id=self.wod_id: self.hande_edit_wod(w_id)
        )

        wod_edit_button.grid(row=0, column=0)

    def _initialize(self):
        self._frame1 = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        self._frame3 = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_main_content()
        self._initialize_footer()
