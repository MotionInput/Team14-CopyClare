import cv2
from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QThread, Signal, Slot


class VideoThread(QThread):
    update_frame = Signal(QImage)

    def __init__(self, master=None):
        super().__init__(master)
        self.cap = True
        self.status = True

    def run(self):
        self.cap = cv2.VideoCapture(0)

        while self.status:

            ret, frame = self.cap.read()

            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, ch = color_frame.shape
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)

            self.update_frame.emit(scaled_img)
