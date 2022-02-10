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

        self.thr2 = VideoThread(None, "/sample1.mp4")
        self.thr2.finished.connect(self.close)
        self.thr2.update_frame.connect(self.setImage2)
        self.thr2.start()

        # TODO: REMOVE LATER
        self.rep = True
        self.numRep = 0

    @Slot(QImage, str)
    def setImage(self, image, angle):

        self.ui.video_2.setPixmap(QPixmap.fromImage(image))

        if float(angle) < 15 and float(angle) > 0:
            if self.rep:
                self.rep = False
                self.numRep += 1
        else:
            self.rep = True

        self.ui.rep_label.setText(f"Repetition: {self.numRep}")
        self.ui.angle_label.setText(f"Angle: {int(float(angle))}")

        pass

    @Slot(QImage)
    def setImage2(self, image):
        self.ui.video_1.setPixmap(QPixmap.fromImage(image))
