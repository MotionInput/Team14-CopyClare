import cv2
from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QThread, Signal, QRect

from copyclare.model import AccuracyModel


class CameraThread(QThread):
    update_frame = Signal(QImage)

    def __init__(self, container):
        QThread.__init__(self, None)
        self.container = container
        self._running = True
        self.worker = CameraWorker()

    def run(self):

        for frame in self.worker.work():
            if not self._running:
                break
            _, _, width, height = self.container.frameGeometry().getRect()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)
            offset = (w - (width * h / height)) / 2
            rect = QRect(offset, 0, w, h)
            scaled_img = img.scaled(width, height,
                                    Qt.KeepAspectRatioByExpanding)

            self.update_frame.emit(scaled_img)


class CameraWorker:
    def work(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error opening a video file")

        while cap.isOpened():

            success, frame = cap.read()
            frame = cv2.flip(frame, 1)

            if not success:
                print("Can't read from Camera")

            yield frame
