from PySide6.QtWidgets import QFrame

from copyclare.common import load_ui


class VideoCardWidget(QFrame):
    def __init__(self, master, title, description, duration, img_path):
        super().__init__(master)
        self.ui = load_ui("video_card")
        self.ui.setupUi(self)

        self.ui.title.setText(title)
        self.ui.description.setText(description)
        self.ui.duration.setText(duration)
