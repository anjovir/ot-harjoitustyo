
from ui.workout_view import WorkoutView
from ui.wod_view import WodView
from ui.new_wod_view import NewWodView
from ui.edit_wod_view import EditWodView
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._handle_login()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
    
    def _handle_workout_view(self):
        self._show_workout_view()
    
    def _handle_wod_view(self, wod_id):
        self._show_wod_view(wod_id)
    
    def _handle_new_wod_view(self):
        self._show_new_wod_view()
    
    def _handle_edit_wod_view(self, wod_id):
        self._show_edit_wod_view(wod_id)
    
    def _handle_login(self):
        self._show_login_view()
    
    def _handle_create_user_view(self):
        self._show_create_user_view()
    
    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._handle_create_user_view,
            self._handle_login
        )

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_workout_view,
            self._handle_create_user_view
        )

        self._current_view.pack()

    def _show_wod_view(self, wod_id):
        self._hide_current_view()
        
        self._current_view = WodView(
            self._root,
            self._handle_workout_view,
            self._handle_edit_wod_view,
            wod_id
        )

        self._current_view.pack()

    def _show_workout_view(self):
        self._hide_current_view()

        self._current_view = WorkoutView(
            self._root,
            self._handle_wod_view,
            self._handle_new_wod_view,
            self._handle_login
        )

        self._current_view.pack()
    
    def _show_new_wod_view(self):
        self._hide_current_view()
        
        self._current_view = NewWodView(
            self._root,
            self._handle_workout_view
        )

        self._current_view.pack()

    def _show_edit_wod_view(self, wod_id):
        self._hide_current_view()
        
        self._current_view = EditWodView(
            self._root,
            self._handle_workout_view,
            self._handle_wod_view,
            wod_id
        )

        self._current_view.pack()
