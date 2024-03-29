class Wod:
    ''' Class that describes single workout of the day (wod)

    Attributes:
        wod_name
        exercise
        sets
        reps
        weights
    '''
    def __init__(self, wod_name, exercise, sets, reps, weights):
        ''' Class constructor, which creates a new workout program

        Args:
            wod_name
            exercise
            sets
            reps
            weights
            
        '''
        self.wod_name = wod_name
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.weights = weights