from tkinter import ttk, constants
from services.wod_service import WodService
from tkinter import messagebox
from tkinter import font


class NewWodView:
    def __init__(self, root, handle__workout_view, handle_wod_view):
        self._root = root
        self._handle_check_workout = handle__workout_view
        self._handle_wod_view = handle_wod_view
        self._frame1 = None
        self._frame2 = None
        self._frame3 = None

        self._font1 = font.Font(family='Helvetica', size=16, weight="bold")
        self._font2 = font.Font(family='Helvetica', size=12, weight="bold")

        self.entries = []
        self._ws = WodService()

        self._initialize()

    def pack(self):
        self._frame1.pack(fill=constants.X)
        self._frame2.pack(fill=constants.X)
        self._frame3.pack(fill=constants.X)

    def destroy(self):
        self._frame1.destroy()
        self._frame2.destroy()
        self._frame3.destroy()

    def create_new_row(self):
        current_row = len(self.entries) + 1
        entries = [self.wod_name_entry]

        for i in range(4):
            entry = ttk.Entry(self._frame2)
            self.default_grid2(entry, row=current_row, column=i)
            entries.append(entry)
        
        self.entries.append(
            entries)        

    def save(self):
        content = []
        for entry in self.entries:
            content.append([self.wod_name_entry.get(),
                            entry[1].get(),
                            entry[2].get(),
                            entry[3].get(),
                            entry[4].get()])

        result = self._ws.save_new_wod(content)
        if result[0]:
            messagebox.showinfo("Success", "Saving succeeded")
            self._handle_wod_view(result[1])
        else:
            messagebox.showinfo(
                "Error", "Wod name already exists, please change the name")
    
    def default_grid(self,widget, row, column, padx=3, pady=3):
        widget.grid(row=row, column=column, padx=padx, pady=pady)
    
    def default_grid2(self,widget, row, column, padx=2, pady=2, sticky="w"):
        widget.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
    
    def _initialize_header(self):
        wod_name = ttk.Label(master=self._frame1, text="Workout name", padding=3)
        self.wod_name_entry = ttk.Entry(master=self._frame1)

        self.default_grid(wod_name,0,0)
        self.default_grid(self.wod_name_entry,0,1)

    def _initialize_main_content(self):
        exercise_name_label = ttk.Label(master=self._frame2, text="Exercise")
        exercise_name_entry = ttk.Entry(master=self._frame2) 
        
        self.default_grid2(exercise_name_label,row=0, column=0)
        self.default_grid2(exercise_name_entry, row=1, column=0)

        sets_label = ttk.Label(master=self._frame2, text="Number of sets")
        sets_entry = ttk.Entry(master=self._frame2)

        self.default_grid2(sets_label,row=0, column=1)
        self.default_grid2(sets_entry,row=1, column=1)

        reps_label = ttk.Label(master=self._frame2, text="Number of reps")
        reps_entry = ttk.Entry(master=self._frame2)

        self.default_grid2(reps_label, row=0, column=2)
        self.default_grid2(reps_entry, row=1, column=2)

        weights_label = ttk.Label(master=self._frame2, text="Weights")
        weights_entry = ttk.Entry(master=self._frame2)

        self.default_grid2(weights_label, row=0, column=3)
        self.default_grid2(weights_entry, row=1, column=3)

        self.entries.append([self.wod_name_entry,
                             exercise_name_entry,
                             sets_entry,
                             reps_entry,
                             weights_entry])

    def _initialize_footer(self):
        workout_program_button = ttk.Button(
            master=self._frame3,
            text="Back to workout program",
            command=self._handle_check_workout
        )

        add_new_row_button = ttk.Button(
            master=self._frame3,
            text="Add new exercise",
            command=self.create_new_row
        )

        save_button = ttk.Button(
            master=self._frame3,
            text="Save",
            command=self.save
        )

        add_new_row_button.grid(row=0, column=0)

        save_button.grid(row=0, column=1)
        workout_program_button.grid(row=0, column=2)

    def _initialize(self):
        self._frame1 = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        self._frame3 = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_main_content()
        self._initialize_footer()
