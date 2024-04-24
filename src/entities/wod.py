class Wod:
    """Class that describes single workout of the day (wod)
    Attributes:
        id
        wod_name
        exercise
        sets
        reps
        weights
    """

    def __init__(self, wod_name="Default",
                 exercise="",
                 sets="",
                 reps="",
                 weights="",
                 w_id="",
                 row_id=""):
        
        """ Class constructor, which creates a new workout program
        Args:
            wod_name (str): name of the workout of the day
            exercise (str): exercise name
            sets (str): number of sets
            reps (str): number of repetitions
            weights (str): weights
            wod_id (str): identifier for the current wod (wod_id_table)
            row_id (str): identifier for the exercise (wod_exercises table)
        """
        
        self.row_id = row_id
        self.id = w_id
        self.wod_name = wod_name
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.weights = weights

    def return_args(self):
        return [self.wod_name,
                self.exercise,
                self.sets,
                self.reps,
                self.weights,
                self.id,
                self.row_id]
