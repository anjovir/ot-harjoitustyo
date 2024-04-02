class WorkoutProgram:
    ''' Class that describes single workout program

    Attributes:
        id: unique indentifier for the workout program
        wprogram_name: string, which describes workout programs name
        wod_name: string for the label of workout of the day
        
    '''
    def __init__(self, id, wprogram_name, wod_name, wod_id):
        ''' Class constructor, which creates a new workout program

        Args:
            id: unique indentifier for the workout program
            wprogram_name: string, which describes workout programs name
            wod_name: string for the label of workout of the day
            
        '''
        self._id = id
        self._wprogram_name = wprogram_name
        self._wod_name = wod_name
        self.w_id = wod_id
    
    def id(self):
        return self._id
    
    def program_name(self):
        return self._wprogram_name
    
    def wod_name(self):
        return self._wod_name
    
    def wod_id(self):
        return self.w_id

    def __str__(self):
        return f"WorkoutProgram(id={self._id}, wprogram_name={self._wprogram_name}, wod_name={self._wod_name})"