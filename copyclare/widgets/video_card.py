"""
Contributors: Adi Bozzhanov, Yan Lai, Sree Sanakkayala

"""

import os

from PySide6.QtGui import QPixmap

from copyclare.common import AppSingleton
from copyclare.data import DATA_DIR
from copyclare.pyui.video_card import Ui_Form
from copyclare import UiElement


class VideoCardWidget(UiElement):
    def __init__(self, master, exercise):

        super().__init__(master, "video_card", Ui_Form)
        self.exercise = exercise
        self.app = AppSingleton.get_app()

        img_path = DATA_DIR + f"/images/{self.exercise.id}.png"
        if os.path.exists(img_path):
            self.ui.video_image.setPixmap(QPixmap(img_path))
        else:
            self.ui.video_image.setPixmap(
                QPixmap(":icons/default-video-img.png"))
        self.ui.title.setText(exercise.name)
        self.ui.description.setText(exercise.description)

        self.ui.add_btn.clicked.connect(self.add_click)

        self.mouseReleaseEvent = self.clicked

    def add_click(self, event):
        self.app.move_to_my_exercises(self.exercise)

    def clicked(self, event):
        # spawns an exercise page

        app = AppSingleton.get_app()
        app.start_exercise(self.exercise)

        print(f"Clicked: {self.ui.title.text()}")
