from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Slot


from copyclare.video import VideoThread

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
        self.thr2.update_frame2.connect(self.setImagee)
        self.thr2.start()

        # TODO: REMOVE LATER
        self.rep = True
        self.numRep = 0

    @Slot(QImage, str)
    def setImage(self, image, angle):

        self.ui.video_2.setPixmap(QPixmap.fromImage(image))

        self.ui.rep_label.setText(f"Repetition: {self.numRep}")
        self.ui.angle_label.setText(f"Accuracy: {int(float(angle))}")

        pass

    @Slot(QImage)
    def setImagee(self, image):
        print("2")
        self.ui.video_1.setPixmap(QPixmap.fromImage(image))
