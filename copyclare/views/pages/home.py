from views.widgets import ExerciseListWidget

from .page import Page


class HomePage(Page):
    def __init__(self, master):
        super().__init__(master, "home")

        self.ex_list = ExerciseListWidget(self)
        self.ui.content_layout.addWidget(self.ex_list)
