from tkinter import ttk, constants

class WodView:

    def __init__(self, root, handle_check_workout):
        self._root = root
        self._handle_check_workout = handle_check_workout
        self._frame = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Workout of the day")

        button = ttk.Button(
            master=self._frame,
            text="Check the full workout program",
            command=self._handle_check_workout
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)