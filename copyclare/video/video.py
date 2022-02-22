import cv2
from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QThread, Signal, Slot

from copyclare.model import AccuracyModel
import time

class VideoThread(QThread):
    update_frame = Signal(QImage, str)
    update_frame2 = Signal(QImage)

    def __init__(self, master=None, src_file=None):

        super().__init__(master)
        # TODO: change the params to something meaningfull
        self.model = AccuracyModel("1", "2")
        self.src_file = src_file

    def run(self):

        if self.src_file is None:

            for frame, accuracy in self.model.accuracy_session():

                color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                h, w, ch = color_frame.shape
                img = QImage(color_frame.data, w, h, ch * w,
                             QImage.Format_RGB888)
                scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)
                

                self.update_frame.emit(scaled_img, str(accuracy))

        else:
            for frame in self.model._raw_video():
                color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                h, w, ch = color_frame.shape
                img = QImage(color_frame.data, w, h, ch * w,
                             QImage.Format_RGB888)
                scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)
                time.sleep(0.2)

                self.update_frame2.emit(scaled_img)
