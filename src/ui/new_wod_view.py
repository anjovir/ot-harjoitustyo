from tkinter import ttk, constants
from repositories.wod_repository import WodRepository
from services.wod_service import WodService
from tkinter import messagebox


class NewWodView:
    def __init__(self, root, handle__workout_view, handle_edit_wod_view):
        self._root = root
        self._handle_check_workout = handle__workout_view
        self._handle_edit_wod_view = handle_edit_wod_view
        self._frame = None
        self._frame2 = None
        self._frame3 = None

        self.entries = []
        self._ws = WodService()

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
        current_row = len(self.entries)

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
            self._handle_edit_wod_view(result[1])
        else:
            messagebox.showinfo(
                "Error", "Wod name already exists, please change the name")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        self._frame3 = ttk.Frame(master=self._root)

        wod_name = ttk.Label(master=self._frame, text="Workout name")
        self.wod_name_entry = ttk.Entry(master=self._frame)

        exercise_name_label = ttk.Label(master=self._frame, text="Exercise")
        exercise_name_entry = ttk.Entry(master=self._frame2)

        sets_label = ttk.Label(master=self._frame, text="Number of sets")
        sets_entry = ttk.Entry(master=self._frame2)

        reps_label = ttk.Label(master=self._frame, text="Number of reps")
        reps_entry = ttk.Entry(master=self._frame2)

        weights_label = ttk.Label(master=self._frame, text="Weights")
        weights_entry = ttk.Entry(master=self._frame2)

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

        wod_name.grid(row=0, column=0)
        self.wod_name_entry.grid(row=0, column=1)

        exercise_name_label.grid(row=1, column=0)
        exercise_name_entry.grid(row=0, column=0)

        sets_label.grid(row=1, column=1)
        sets_entry.grid(row=0, column=1)

        reps_label.grid(row=1, column=2)
        reps_entry.grid(row=0, column=2)

        weights_label.grid(row=1, column=3)
        weights_entry.grid(row=0, column=3)

        add_new_row_button.grid(row=0, column=0)

        save_button.grid(row=0, column=1)
        workout_program_button.grid(row=0, column=2)

        self.entries.append([self.wod_name_entry,
                             exercise_name_entry,
                             sets_entry,
                             reps_entry,
                             weights_entry])
