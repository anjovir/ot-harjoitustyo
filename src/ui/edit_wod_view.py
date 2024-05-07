from tkinter import ttk, constants
from repositories.wod_repository import WodRepository
from services.wod_service import WodService


class EditWodView:
    def __init__(self, root, handle_workout_view, handle_wod_view, wod_id):
        self._root = root
        self._handle_check_workout = handle_workout_view
        self.handle_wod_view = handle_wod_view
        self._frame1 = None
        self._frame2 = None
        self._frame2b = None
        self._frame3 = None

        self.entries = []
        self.wod_id = wod_id
        self._ws = WodService()
        self._wod = self._ws.initialize_wod_view(self.wod_id)

        self._initialize()

    def pack(self):
        self._frame1.pack(fill=constants.X)
        self._frame2.pack(fill=constants.X)
        self._frame2b.pack(fill=constants.X)
        self._frame3.pack(fill=constants.X)

    def destroy(self):
        self._frame1.destroy()
        self._frame2.destroy()
        self._frame2b.destroy()
        self._frame3.destroy()

    def create_new_row(self):
        current_row = len(self.entries) + 1

        entry1 = ttk.Entry(self._frame2)
        entry2 = ttk.Entry(self._frame2)
        entry3 = ttk.Entry(self._frame2)
        entry4 = ttk.Entry(self._frame2)

        entry1.grid(row=current_row, column=0)
        entry2.grid(row=current_row, column=1)
        entry3.grid(row=current_row, column=2)
        entry4.grid(row=current_row, column=3)

        self.entries.append(
            [self.wod_name_entry, entry1, entry2, entry3, entry4])

    def save(self):
        id_counter = 0
        content = []

        for entry in self.entries:
            exercise = entry[1].get()
            sets = entry[2].get()
            reps = entry[3].get()
            weights = entry[4].get()
            if id_counter < len(self.ids):
                row_id = self.ids[id_counter]
            else:
                # row_id is not yet made or references to another wod_id
                row_id = 0

            content.append([row_id,
                            self.wod_id,
                            self.wod_name_entry.get(),
                            exercise,
                            sets,
                            reps,
                            weights])

            id_counter += 1

        self.ids = self._ws.update_wod(content)

    def _default_grid(self, widget, row, column, padx=2, pady=2, sticky="w"):
        widget.grid(row=row, column=column, padx=padx,
                    pady=pady, sticky=sticky)

    def _initialize_header(self):
        wod_name = ttk.Label(master=self._frame1, text="Workout name")
        self.wod_name_entry = ttk.Entry(master=self._frame1)

        wod_name.grid(row=0, column=0)
        self.wod_name_entry.grid(row=0, column=1)
        self.wod_name_entry.insert(0, self._wod[0][0])

    def _initialize_main_content(self):
        exercise_name_label = ttk.Label(master=self._frame2, text="Exercise")
        sets_label = ttk.Label(master=self._frame2, text="Number of sets")
        reps_label = ttk.Label(master=self._frame2, text="Number of reps")
        weights_label = ttk.Label(master=self._frame2, text="Weights")

        self._default_grid(exercise_name_label, 0, 0)
        self._default_grid(sets_label, 0, 1)
        self._default_grid(reps_label, row=0, column=2)
        self._default_grid(weights_label, row=0, column=3)

        self.ids = []
        self.wod_id = self._wod[0][5]

        for i in range((len(self._wod))):
            row_num = i + 1
            exercise_name_entry = ttk.Entry(master=self._frame2)
            self._default_grid(exercise_name_entry, row=row_num, column=0)
            exercise_name_entry.insert(0, self._wod[i][1])

            sets_entry = ttk.Entry(master=self._frame2)
            self._default_grid(sets_entry, row=row_num, column=1)
            sets_entry.insert(0, self._wod[i][2])

            reps_entry = ttk.Entry(master=self._frame2)
            self._default_grid(reps_entry, row=row_num, column=2)
            reps_entry.insert(0, self._wod[i][3])

            weights_entry = ttk.Entry(master=self._frame2)
            self._default_grid(weights_entry, row=row_num, column=3)
            weights_entry.insert(0, self._wod[i][4])

            self.ids.append(self._wod[i][6])

            self.entries.append([self.wod_name_entry,
                                 exercise_name_entry,
                                 sets_entry,
                                 reps_entry,
                                 weights_entry])

        add_new_row_button = ttk.Button(
            master=self._frame2b,
            text="Add new exercise",
            command=self.create_new_row
        )
        add_new_row_button.grid(row=(row_num + 1), column=0, padx=3, pady=3)

    def _initialize_footer(self):
        workout_program_button = ttk.Button(
            master=self._frame3,
            text="Back to workout program",
            command=self._handle_check_workout
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

        save_button.grid(row=0, column=0, padx=3, pady=3)
        wod_button.grid(row=0, column=1, padx=3, pady=3)
        workout_program_button.grid(row=0, column=2, padx=3, pady=3)

    def _initialize(self):
        self._frame1 = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        self._frame2b = ttk.Frame(master=self._root)
        self._frame3 = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_main_content()
        self._initialize_footer()
