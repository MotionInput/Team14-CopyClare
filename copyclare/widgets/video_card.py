from PySide6.QtWidgets import QFrame
from PySide6.QtGui import QPixmap

from copyclare import DATA_PATH
from copyclare.common import load_ui, AppSingleton


class VideoCardWidget(QFrame):
    def __init__(self, master, exercise):

        super().__init__(master)
        self.ui = load_ui("video_card")
        self.ui.setupUi(self)
        self.exercise = exercise

        #self.ui.video_image.setStyleSheet("background-image: url(" + DATA_PATH + "/assets/default-video-img.png)")

        self.ui.video_image.setPixmap(
            QPixmap(DATA_PATH + "/assets/default-video-img.png"))
        self.ui.title.setText(exercise.name)
        self.ui.description.setText(exercise.description)

        self.mouseReleaseEvent = self.clicked

    def clicked(self, event):
        # spawns an exercise page

        app = AppSingleton.get_app()
        app.start_exercise(self.exercise)

        print(f"Clicked: {self.ui.title.text()}")
