"""
Contributors: Adi Bozzhanov, Yan Lai, Sree Sanakkayala

"""

import os

from PySide6.QtGui import QPixmap

from copyclare.common import AppSingleton
from copyclare.data import DATA_DIR
from copyclare.pyui.video_card_my_ex import Ui_Form
from copyclare import UiElement


class VideoCardMyExWidget(UiElement):
    def __init__(self, master, exercise):

        super().__init__(master, "video_card_my_ex", Ui_Form)
        self.exercise = exercise
        self.id = self.exercise.id
        self.app = AppSingleton.get_app()

        img_path = DATA_DIR + f"/images/{self.exercise.id}.png"
        if os.path.exists(img_path):
            self.ui.video_image.setPixmap(QPixmap(img_path))
        else:
            self.ui.video_image.setPixmap(
                QPixmap(":icons/default-video-img.png"))

        self.ui.title.setText(exercise.name)
        self.ui.description.setText(exercise.description)

        self.ui.remove_btn.clicked.connect(self.remove_click)

        self.mouseReleaseEvent = self.clicked

    def remove_click(self, event):
        """
        Triggered when 'remove' button is clicked. Removes 'My Exercises' tag from chosen exercise 

        """
        self.app.remove_from_my_exercises(self.exercise)

    def clicked(self, event):
        # spawns an exercise page

        app = AppSingleton.get_app()
        app.start_exercise(self.exercise)

        print(f"Clicked: {self.ui.title.text()}")
