from tkinter import ttk, constants
from repositories.wod_repository import WodRepository
from services.wod_service import WodService

class EditWodView:
    def __init__(self, root, handle_workout_view, handle_wod_view, wod_id):
        self._root = root
        self._handle_check_workout = handle_workout_view
        self.handle_wod_view = handle_wod_view
        self._frame = None
        self._frame2 = None
        self._frame3 = None
        
        self.entries = []
        self.wod_id = wod_id
        self._ws = WodService()

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
        self._frameb.pack(fill=constants.X)
        self._frame2.pack(fill=constants.X)
        self._frame3.pack(fill=constants.X)


    def destroy(self):
        self._frame.destroy()
        self._frameb.destroy()
        self._frame2.destroy()
        self._frame3.destroy()
    
    def create_new_row(self):
        current_row = len(self.entries)
        
        entry1 = ttk.Entry(self._frameb)
        entry2 = ttk.Entry(self._frameb)
        entry3 = ttk.Entry(self._frameb)
        entry4 = ttk.Entry(self._frameb)
        
        entry1.grid(row=current_row, column=0)
        entry2.grid(row=current_row, column=1)
        entry3.grid(row=current_row, column=2)
        entry4.grid(row=current_row, column=3)
        
        self.entries.append([self.wod_name_entry,entry1, entry2, entry3, entry4])
        self.ids.append(self._ws.return_last_id(self.wod_id))
        
    def save(self):
        id_counter = 0
        content = []
        
        for entry in self.entries:
            exercise = entry[1].get()
            sets = entry[2].get()
            reps = entry[3].get()
            weights = entry[4].get()
            row_id = self.ids[id_counter]
        
            content.append([row_id,
                    self.wod_id,
                    self.wod_name_entry.get(),
                    exercise,
                    sets,
                    reps,
                    weights])

            id_counter += 1
        
        self._ws.update_wod(content)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frameb = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        self._frame3 = ttk.Frame(master=self._root)
        
        wod_name = ttk.Label(master=self._frame, text="Workout name")
        self.wod_name_entry = ttk.Entry(master=self._frame)
        
        exercise_name_label = ttk.Label(master=self._frame, text="Exercise")
        sets_label = ttk.Label(master=self._frame, text="Number of sets")
        reps_label = ttk.Label(master=self._frame, text="Number of reps")
        weights_label = ttk.Label(master=self._frame, text="Weights")

        wod = self._ws.initialize_wod_view(self.wod_id)
        
        workout_program_button = ttk.Button(
            master=self._frame3,
            text="Back to workout program",
            command=self._handle_check_workout
        )

        add_new_row_button = ttk.Button(
            master=self._frame2,
            text="Add new exercise",
            command=self.create_new_row
            )
        
        save_button = ttk.Button(
            master=self._frame3,
            text="Save",
            command=self.save
        )

        wod_button = ttk.Button(
            master=self._frame3,
            text=f"Back to workout",
            command=lambda w_id=self.wod_id: self.handle_wod_view(w_id)
            )
        
        wod_name.grid(row=0, column=0)
        self.wod_name_entry.grid(row=0, column=1)
        self.wod_name_entry.insert(0,wod[0][0])

        exercise_name_label.grid(row=2, column=0)
        sets_label.grid(row=2, column=1)
        reps_label.grid(row=2, column=2)
        weights_label.grid(row=2, column=3)

        self.ids = []
        self.wod_id = wod[0][5]

        for i in range(len(wod)):
            exercise_name_entry = ttk.Entry(master=self._frameb)
            exercise_name_entry.grid(row=i, column=0)
            exercise_name_entry.insert(0,wod[i][1])
            
            sets_entry = ttk.Entry(master=self._frameb)
            sets_entry.grid(row=i, column=1)
            sets_entry.insert(0,wod[i][2])
        
            reps_entry = ttk.Entry(master=self._frameb)
            reps_entry.grid(row=i, column=2)
            reps_entry.insert(0,wod[i][3])

            weights_entry = ttk.Entry(master=self._frameb)
            weights_entry.grid(row=i, column=3)
            weights_entry.insert(0,wod[i][4])

            self.ids.append(wod[i][6])

            self.entries.append([self.wod_name_entry,
                             exercise_name_entry,
                             sets_entry,
                             reps_entry,
                             weights_entry])

        add_new_row_button.grid(row=0, column=0)        

        save_button.grid(row=0, column=0)
        wod_button.grid(row=0, column=1)
        workout_program_button.grid(row=0,column=2)

        
        
        