import cv2
import time

from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QThread, Signal, QRect

from copyclare.model import AccuracyModel
from copyclare import DATA_PATH


class CameraThread(QThread):
    update_frame = Signal(QImage)
    update_reps = Signal(int)
    update_graph = Signal(list)

    def __init__(self, container, exercise):
        QThread.__init__(self, None)
        self.container = container
        self._running = True
        self.worker = CameraWorker(exercise)
        self.reps = 0

    def run(self):
        count = 0

        for frame in self.worker.work():
            count += 1
            if not self._running:
                break

            _, _, width, height = self.container.frameGeometry().getRect()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            self.update_reps.emit(self.worker.num_of_repetitions)

            img = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)

            scaled_img = img.scaled(width, height,
                                    Qt.KeepAspectRatioByExpanding)

            self.update_frame.emit(scaled_img)
            if count % 2 == 0:
                self.update_graph.emit(self.worker.accuracy_vals)

        self.quit()


class CameraWorker:
    def __init__(self, exercise):

        self.exercise = exercise
        joints = {
            "left_shoulder",
            "left_elbow",
            "right_elbow",
            "right_shoulder",
        }
        self.model = AccuracyModel(exercise, joints)

    def work(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error opening a video file")

        self.beginning = time.time()
        self.accuracy = 0
        self.num_of_repetitions = 0
        self.updated = False
        self.accuracy_vals = []

        start = time.time()
        while (cap.isOpened):

            success, frame = cap.read()

            self.accuracy, rep = self.model.accuracy(frame,
                                                     time.time() - start)

            if self.accuracy > 0:
                self.accuracy_vals.append(
                    (time.time() - self.beginning, self.accuracy))

            if rep:
                start = time.time()

            if not self.accuracy > 80:
                start = time.time()
                self.updated = False
            elif not self.updated:
                self.num_of_repetitions += 1
                self.updated = True

            if not success:
                print("Can't read from Camera")

            frame = cv2.flip(frame, 1)

            yield frame
