from tkinter import ttk, constants
from wod_repository import WodRepository

class EditWodView:
    def __init__(self, root, handle_workout_view, handle_wod_view, wod_name):
        self._root = root
        self._handle_check_workout = handle_workout_view
        self.handle_wod_view = handle_wod_view
        self._frame = None
        self._frame2 = None
        self._frame3 = None
        
        self.rows = [0,1,2,3]
        self.entries = []
        self.wod_name = wod_name

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
        current_row = len(self.rows)
        
        entry1 = ttk.Entry(self._frame)
        entry2 = ttk.Entry(self._frame)
        entry3 = ttk.Entry(self._frame)
        entry4 = ttk.Entry(self._frame)
        
        entry1.grid(row=current_row, column=0)
        entry2.grid(row=current_row, column=1)
        entry3.grid(row=current_row, column=2)
        entry4.grid(row=current_row, column=3)
        
        self.rows.append(len(self.rows))
        self.entries.append([self.wod_name_entry,entry1, entry2, entry3, entry4])
        
    def save(self):
        rep = WodRepository()
        wprogram_id = 1
        
        for entry in self.entries:
            exercise = entry[1].get()
            sets = entry[2].get()
            reps = entry[3].get()
            weights = entry[4].get()
            rep.write(self.wod_name_entry.get(),
                      wprogram_id,
                      exercise,
                      sets,
                      reps,
                      weights)

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
            text=f"Back to  {self.wod_name}",
            command=lambda wname=self.wod_name: self.handle_wod_view(wname)
            )
        
            
        wod_name.grid(row=0, column=0)
        self.wod_name_entry.grid(row=0, column=1)
        self.wod_name_entry.insert(0,self.wod_name)

        
        exercise_name_label.grid(row=2, column=0)
        sets_label.grid(row=2, column=1)
        reps_label.grid(row=2, column=2)
        weights_label.grid(row=2, column=3)

        wr = WodRepository()
        current_wod = wr.find_current_wod(self.wod_name)
        print(current_wod)
        
        for i in range(len(current_wod)):
            exercise_name_entry = ttk.Entry(master=self._frameb)
            exercise_name_entry.grid(row=i, column=0)
            exercise_name_entry.insert(0,current_wod[i].return_args()[1])
            
            sets_entry = ttk.Entry(master=self._frameb)
            sets_entry.grid(row=i, column=1)
            sets_entry.insert(0,current_wod[i].return_args()[2])
        
            reps_entry = ttk.Entry(master=self._frameb)
            reps_entry.grid(row=i, column=2)
            reps_entry.insert(0,current_wod[i].return_args()[3])

            weights_entry = ttk.Entry(master=self._frameb)
            weights_entry.grid(row=i, column=3)
            weights_entry.insert(0,current_wod[i].return_args()[4])

        add_new_row_button.grid(row=len(self.rows), column=0)        

        save_button.grid(row=0, column=0)
        workout_program_button.grid(row=0,column=1)
        wod_button.grid(row=5, column=5)

        self.entries.append([self.wod_name_entry,
                             exercise_name_entry,
                             sets_entry,
                             reps_entry,
                             weights_entry])
        
        