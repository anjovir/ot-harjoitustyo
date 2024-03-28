from tkinter import ttk, constants
import tkinter as tk
from tkinter import font as tkfont
from wprogram_repository import WorkoutProgramRepository
from workout_program import WorkoutProgram

class WorkoutView:

    def __init__(self, root, handle_check_wod):
        self._root = root
        self._handle_check_wod = handle_check_wod
        self._frame1 = None
        self._frame2 = None
        self._frame3 = None
        
        self.rows = [0,1,2,3]
        self.entries = []

        self.title = tkfont.Font(family='Helvetica', size=18, weight="bold")

        self._initialize()
    
    def pack(self):
        self._frame1.pack(fill=constants.X)
        self._frame2.pack(fill=constants.X)
        self._frame3.pack(fill=constants.X)
    
    def destroy(self):
        self._frame1.destroy()
        self._frame2.destroy()
        self._frame3.destroy()
    
    def save(self):
        rep = WorkoutProgramRepository()
        for entry in self.entries:
            wlabel = entry[0].get()
            weekday = entry[1].get()
            rep.write("Workout program",wlabel, weekday)

    def _initialize(self):
        self._frame1 = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        self._frame3 = ttk.Frame(master=self._root)
        wpr = WorkoutProgramRepository()
        workouts = wpr.find_all()
        
        workout_name = ttk.Label(master=self._frame1, text= workouts[0].program_name(),
                                 font=self.title, padding=5)
        workout_name.grid(row=0, column=0, columnspan=2)

        wod_button = ttk.Button(
            master=self._frame2,
            text="Check the workout",
            command=self._handle_check_wod
        )

        counter = 1
        for workout in workouts:   
            wod = ttk.Label(master=self._frame2, text= workout.wod_name())    
            wod.grid(row=counter, column=0)

            wod_button = ttk.Button(
            master=self._frame2,
            text="Check the workout",
            command=self._handle_check_wod
        )
            wod_button.grid(row=counter, column=1)
            counter += 1
        

        
        
        
