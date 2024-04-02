
from ui.workout_view import WorkoutView
from ui.wod_view import WodView
from ui.new_wod_view import NewWodView
from ui.edit_wod_view import EditWodView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_workout_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
    
    def _handle_workout(self):
        self._show_workout_view()
    
    def _handle_wod(self, wod_id):
        self._show_wod_view(wod_id)
    
    def _handle_new_wod_view(self):
        self._show_new_wod_view()
    
    def _handle_edit_wod_view(self, wod_id):
        self._show_edit_wod_view(wod_id)

    def _show_wod_view(self, wod_id):
        self._hide_current_view()
        
        self._current_view = WodView(
            self._root,
            self._handle_workout,
            self._handle_edit_wod_view,
            wod_id
        )

        self._current_view.pack()

    def _show_workout_view(self):
        self._hide_current_view()

        self._current_view = WorkoutView(
            self._root,
            self._handle_wod,
            self._handle_new_wod_view
        )

        self._current_view.pack()
    
    def _show_new_wod_view(self):
        self._hide_current_view()
        
        self._current_view = NewWodView(
            self._root,
            self._handle_workout
        )

        self._current_view.pack()

    def _show_edit_wod_view(self, wod_id):
        self._hide_current_view()
        
        self._current_view = EditWodView(
            self._root,
            self._handle_workout,
            self._handle_wod,
            wod_id
        )

        self._current_view.pack()
