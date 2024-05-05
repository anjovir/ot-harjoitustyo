from tkinter import ttk, constants
# import tkinter as tk
from tkinter import font as tkfont
# from repositories.wprogram_repository import WorkoutProgramRepository
# from entities.workout_program import WorkoutProgram
from services.wprogram_service import WprogramService
from tkinter import messagebox
from services.user_service import user_service


class WorkoutView:

    def __init__(self, root,
                 handle_wod,
                 handle_new_wod,
                 handle_logout):

        self._root = root
        self._handle_check_wod = handle_wod
        self.handle_new_wod = handle_new_wod
        self._handle_logout = handle_logout
        self._frame1 = None
        self._frame2 = None
        self._frame3 = None

        self._workouts = WprogramService().initialize_wp_view()

        self.rows = [0, 1, 2, 3]
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

    def delete_wod(self, wod_id, wl, db, wb):
        WprogramService().delete_wod(wod_id)

        wl.destroy()
        db.destroy()
        wb.destroy()

        messagebox.showinfo("Succes", "Workout deleted successfully")

    def _delete_user_data(self):
        user_service.delete_user_data()
        messagebox.showinfo("Succes", "User data deleted successfully")
        self._handle_logout()

    def _initialize(self):
        self._frame1 = ttk.Frame(master=self._root)
        self._frame2 = ttk.Frame(master=self._root)
        self._frame3 = ttk.Frame(master=self._root)

        check = WprogramService().check_if_db_empty()

        workout_name = ttk.Label(master=self._frame1, text=self._workouts[0].program_name(),
                                 font=self.title, padding=5)

        workout_name.grid(row=0, column=0, columnspan=2)

        counter = 1
        for workout in self._workouts:

            wod = ttk.Label(master=self._frame2, text=workout.wod_name())

            wod.grid(row=counter, column=0)

            wod_button = ttk.Button(
                master=self._frame2,
                text="Check the workout",
                command=lambda wod_id=workout.wod_id(), : self._handle_check_wod(wod_id))

            delete_button = ttk.Button(
                master=self._frame2,
                text="Delete workout"
            )

            if check == False:
                wod_button.grid(row=counter, column=1)
                delete_button.grid(row=counter, column=2)

                delete_button.config(
                    command=lambda wod_id=workout.wod_id(),
                    wl=wod,
                    db=delete_button,
                    wb=wod_button: self.delete_wod(wod_id, wl, db, wb)
                )

            counter += 1

        new_wod_button = ttk.Button(
            master=self._frame3,
            text="New WOD",
            command=self.handle_new_wod
        )
        new_wod_button.grid(row=0, column=0)

        logout = ttk.Button(
            master=self._frame3,
            text="Logout",
            command=self._handle_logout
        )
        logout.grid(row=0, column=1)

        delete_user_data = ttk.Button(
            master=self._frame3,
            text="Delete user data",
            command=self._delete_user_data
        )
        delete_user_data.grid(row=0, column=2)
