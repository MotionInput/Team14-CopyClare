from PySide6.QtWidgets import QFrame

from copyclare.common import load_ui
from copyclare.widgets import VideoCardWidget
from copyclare.pyui.banner import Ui_Frame
from copyclare import UiElement


class BannerWidget(UiElement):
    def __init__(self, master, title, exercises):
        super().__init__(master, "banner", Ui_Frame)
        self.cards = {}
        self.ui.category_title.setText(title)

        self.init_exercises(exercises)

    def init_exercises(self, exercises):

        for exercise in exercises:
            self.cards[str(exercise.id)] = VideoCardWidget(
                self.ui.scrollArea, exercise)
            self.ui.horizontalLayout.insertWidget(0,
                                                  self.cards[str(exercise.id)])
