class WorkoutProgram:
    ''' Class that describes single workout program

    Attributes:
        wprogram_name: string, which describes workout programs name
        wod_name: string for the label of workout of the day
        weekday: string for the weekday of the wod
    '''
    def __init__(self, wprogram_name, wod_name, weekday):
        ''' Class constructor, which creates a new workout program

        Args:
            wprogram_name: string, which describes workout programs name
            wod_name: string for the label of workout of the day
            weekday: string for the weekday of the wod

        '''
        self._wprogram_name = wprogram_name
        self._wod_name = wod_name
        self._weekday = weekday