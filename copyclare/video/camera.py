import cv2
import time

from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QThread, Signal, QRect

from copyclare.model import AccuracyModel
from copyclare import DATA_PATH


class CameraThread(QThread):
    update_frame = Signal(QImage)

    def __init__(self, container, exercise):
        QThread.__init__(self, None)
        self.container = container
        self._running = True
        self.worker = CameraWorker(exercise)

    def run(self):

        for frame in self.worker.work():
            if not self._running:
                break
            _, _, width, height = self.container.frameGeometry().getRect()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)

            scaled_img = img.scaled(width, height,
                                    Qt.KeepAspectRatioByExpanding)

            self.update_frame.emit(scaled_img)

        self.quit()


class CameraWorker:
    def __init__(self, exercise):

        self.exercise = exercise
        joints = {
            "left_shoulder",
            "left_elbow",
        }
        self.model = AccuracyModel(exercise, joints)


    def work(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error opening a video file")

        self.beginning = time.time()
        self.accuracy = 0
        self.num_of_repetitions = 0

        start = time.time()
        while (cap.isOpened):

            success, frame = cap.read()

            correct = self.model.accuracy(frame, time.time() - start)

            if correct:
                self.accuracy += 1
                self.num_of_repetitions += 1
            else:
                start = time.time()

            if not success:
                print("Can't read from Camera")

            frame = cv2.flip(frame, 1)


            yield frame
