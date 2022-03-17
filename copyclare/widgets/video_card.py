from PySide6.QtWidgets import QFrame

from copyclare import DATA_PATH
from copyclare.common import load_ui


class VideoCardWidget(QFrame):
    def __init__(self, master, title, description, img_path):
        super().__init__(master)
        self.ui = load_ui("video_card")
        self.ui.setupUi(self)

        self.ui.video_image.setStyleSheet("background-image: url(" + DATA_PATH + "/assets/default-video-img.png)")
        self.ui.title.setText(title)
        self.ui.description.setText(description)
