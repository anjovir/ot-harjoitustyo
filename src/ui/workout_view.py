from tkinter import ttk, constants
from wprogram_repository import WorkoutProgramRepository

class WorkoutView:

    def __init__(self, root, handle_check_wod):
        self._root = root
        self._handle_check_wod = handle_check_wod
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
    
    def create_new_row(self):
        current_row = len(self.rows)
        
        self.entry1 = ttk.Entry(self._frame)
        self.entry1.grid(row=current_row, column=0)
        self.entry2 = ttk.Entry(self._frame)
        self.entry2.grid(row=current_row, column=1)
        self.entries.append([self.entry1, self.entry2])
        
        wod_button = ttk.Button(
            master=self._frame,
            text="Check the workout",
            command=self._handle_check_wod
        )

        wod_button.grid(row=current_row,column=2)
        
        self.rows.append(len(self.rows))
        print(self.entries)
    
    def save(self):
        rep = WorkoutProgramRepository()
        for entry in self.entries:
            wlabel = entry[0].get()
            weekday = entry[1].get()
            print("Tulostus:", wlabel, weekday)
            rep.write("Workout program",wlabel, weekday)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        self._frame3 = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Workout program")

        self.workout_label = ttk.Label(master=self._frame, text="Workout label")
        weekday_label = ttk.Label(master=self._frame, text="Weekday")

        self.workout_label_entry = ttk.Entry(master=self._frame)
        self.weekday_label_entry = ttk.Entry(master=self._frame)

        self.entries.append([self.workout_label_entry, self.weekday_label_entry])

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

        save_button = ttk.Button(
            master=self._frame3,
            text="Save",
            command=self.save
        )

        label.grid(row=0, column=0)
        self.workout_label.grid(row=2, column=0)
        weekday_label.grid(row=2, column=1)
        self.workout_label_entry.grid(row=3, column=0)
        self.weekday_label_entry.grid(row=3, column=1)
        wod_button.grid(row=3, column=2)
        
        add_new_wod_button.grid(row=4, column=0)

        save_button.grid(row=5, column=0)
        
