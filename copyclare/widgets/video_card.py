import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame

from copyclare.common import AppSingleton, load_ui
from copyclare.data import DATA_DIR


class VideoCardWidget(QFrame):
    def __init__(self, master, exercise):

        super().__init__(master)
        self.ui = load_ui("video_card")
        self.ui.setupUi(self)
        self.exercise = exercise

        #self.ui.video_image.setStyleSheet("background-image: url(" + DATA_PATH + "/assets/default-video-img.png)")

        img_path = DATA_DIR + f"/test/{exercise.id}.png"
        print(img_path)
        if os.path.exists(img_path):
            self.ui.video_image.setPixmap(QPixmap(img_path))
        else:
            self.ui.video_image.setPixmap(
                QPixmap(DATA_DIR + "/assets/default-video-img.png"))
        self.ui.title.setText(exercise.name)
        self.ui.description.setText(exercise.description)

        # TODO - if already in my_exercises, then need to be on 'remove' function state
        self.ui.add_btn.clicked.connect(self.add_click)

        self.mouseReleaseEvent = self.clicked

    def add_click(self, event):
        app = AppSingleton.get_app()
        app.move_to_my_exercises(self.exercise)
        self.ui.add_btn.setText("remove")
        self.ui.add_btn.clicked.connect(self.remove_click)

    # TODO - if clicked, moves back to library
    def remove_click(self):
        app = AppSingleton.get_app()
        app.remove_from_my_exercises(self.exercise)
        self.ui.add_btn.setText("add")
        self.ui.add_btn.clicked.connect(self.add_click)

    def clicked(self, event):
        # spawns an exercise page

        app = AppSingleton.get_app()
        app.start_exercise(self.exercise)

        print(f"Clicked: {self.ui.title.text()}")
