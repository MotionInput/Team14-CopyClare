from copyclare.widgets import ExerciseListWidget


from .page import Page


class HomePage(Page):
    def __init__(self, master):
        super().__init__(master, "home")
