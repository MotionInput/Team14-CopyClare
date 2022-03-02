from copyclare.widgets import ExerciseListWidget
from copyclare.widgets import VideoCard

from .page import Page


class HomePage(Page):
    def __init__(self, master):
        super().__init__(master, "home")
        self.ui.latest_button.clicked.connect(
            lambda x: self.button_click(
                ["Left Hand", "Right Hand", "Shoulder", "Another Exercise"]
            )
        )
        self.ui.groups_button.clicked.connect(
            lambda x: self.button_click(["Group_1", "Group_2", "My Group", "Favourite"])
        )
        self.ex_list = None


    def button_click(self, exercises):
        if self.ex_list is not None:
            self.ex_list.hide()

        self.ex_list = ExerciseListWidget(self, exercises)
        self.ui.content_layout.addWidget(self.ex_list)
