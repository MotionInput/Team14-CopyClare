from PySide6.QtWidgets import QFrame

from copyclare.widgets import VideoCardWidget
from copyclare.common import load_ui





class BannerWidget(QFrame):
    def __init__(self, master, title, exercises):
        super().__init__(master)
        self.ui = load_ui("banner")
        self.ui.setupUi(self)
        self.ui.category_title.setText(title)
        self.init_exercises(exercises)
        self.cards = {}

    def init_exercises(self, exercises):

        for exercise in exercises:
            self.card[str(exercise.id)] = VideoCardWidget(self.ui.scrollArea, exercise)
            self.ui.horizontalLayout.insertWidget(0, _vid)
