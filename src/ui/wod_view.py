from tkinter import ttk, constants

class WodView:

    def __init__(self, root, handle__workout_view):
        self._root = root
        self._handle_check_workout = handle__workout_view
        self._frame = None
        self._frame2 = None
        
        self.rows = [0,1,2,3]

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
        self._frame2.pack(fill=constants.X)


    def destroy(self):
        self._frame.destroy()
        self._frame2.destroy()
    
    def create_new_row(self):
        current_row = len(self.rows)
        
        for i in range(4):
            entry = ttk.Entry(self._frame)
            entry.grid(row=current_row, column=i)
        
        self.rows.append(len(self.rows))
        
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Workout of the day")
        
        exercise_name_label = ttk.Label(master=self._frame, text="Exercise")
        exercise_name_entry = ttk.Entry(master=self._frame)

        sets_label = ttk.Label(master=self._frame, text="Number of sets")
        sets_entry = ttk.Entry(master=self._frame)

        reps_label = ttk.Label(master=self._frame, text="Number of reps")
        reps_entry = ttk.Entry(master=self._frame)

        weights_label = ttk.Label(master=self._frame, text="Weights")
        weights_entry = ttk.Entry(master=self._frame)


        workout_program_button = ttk.Button(
            master=self._frame,
            text="Back to workout program",
            command=self._handle_check_workout
        )

        add_new_row_button = ttk.Button(
            master=self._frame2,
            text="Add new exercise",
            command=self.create_new_row
            )
            
        
        label.grid(row=0, column=0, pady=5)
        workout_program_button.grid(row=0, column=1, pady=5)
        exercise_name_label.grid(row=2, column=0)
        sets_label.grid(row=2, column=1)
        reps_label.grid(row=2, column=2)
        weights_label.grid(row=2, column=3)

        exercise_name_entry.grid(row=3, column=0)
        sets_entry.grid(row=3, column=1)
        reps_entry.grid(row=3, column=2)
        weights_entry.grid(row=3, column=3)
        add_new_row_button.grid(row=len(self.rows), column=0)
        
        
        