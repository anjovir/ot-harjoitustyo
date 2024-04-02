class Wod:
    ''' Class that describes single workout of the day (wod)

    Attributes:
        wod_name
        exercise
        sets
        reps
        weights
    '''
    def __init__(self, wod_name, exercise, sets, reps, weights, id, row_id):
        ''' Class constructor, which creates a new workout program

        Args:
            wod_name
            exercise
            sets
            reps
            weights
            
        '''
        self.row_id = row_id
        self.id = id
        self.wod_name = wod_name
        self.exercise = exercise
        self.sets = sets
        self.reps = reps
        self.weights = weights
    
    def return_args(self):
        return [self.wod_name, self.exercise, self.sets, self.reps, self.weights, self.id, self.row_id]