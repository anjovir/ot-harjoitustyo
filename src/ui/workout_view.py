from tkinter import ttk, constants

class WorkoutView:

    def __init__(self, root, handle_check_wod):
        self._root = root
        self._handle_check_wod = handle_check_wod
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
        
        for i in range(2):
            entry = ttk.Entry(self._frame)
            entry.grid(row=current_row, column=i)
        
        wod_button = ttk.Button(
            master=self._frame,
            text="Check the workout",
            command=self._handle_check_wod
        )

        wod_button.grid(row=current_row,column=2)
        
        self.rows.append(len(self.rows))
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Workout program")

        workout_label = ttk.Label(master=self._frame, text="Workout label")
        weekday_label = ttk.Label(master=self._frame, text="Weekday")

        workout_label_entry = ttk.Entry(master=self._frame)
        weekday_label_entry = ttk.Entry(master=self._frame)

        wod_button = ttk.Button(
            master=self._frame,
            text="Check the workout",
            command=self._handle_check_wod
        )

        add_new_wod_button = ttk.Button(
            master=self._frame2,
            text="Add new workout of the day",
            command=self.create_new_row
        )

        label.grid(row=0, column=0)
        workout_label.grid(row=2, column=0)
        weekday_label.grid(row=2, column=1)
        workout_label_entry.grid(row=3, column=0)
        weekday_label_entry.grid(row=3, column=1)
        wod_button.grid(row=3, column=2)
        
        
        add_new_wod_button.grid(row=4, column=0)
        
