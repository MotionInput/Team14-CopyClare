from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Slot

from common import load_ui
from views.video import VideoThread

from .page import Page


class ExercisePage(Page):
    def __init__(self, master):
        super().__init__(master, "exercise")

        self.thr = VideoThread(self)
        self.thr.finished.connect(self.close)
        self.thr.update_frame.connect(self.setImage)
        self.thr.start()

    @Slot(QImage)
    def setImage(self, image):
        self.ui.video_2.setPixmap(QPixmap.fromImage(image))
