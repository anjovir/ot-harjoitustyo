from tkinter import ttk, constants

class WorkoutView:

    def __init__(self, root, handle_check_wod):
        self._root = root
        self._handle_check_wod = handle_check_wod
        self._frame = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Workout program")

        button = ttk.Button(
            master=self._frame,
            text="Check the workout of the day",
            command=self._handle_check_wod
        )

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)