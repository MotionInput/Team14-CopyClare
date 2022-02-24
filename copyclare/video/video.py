import cv2
from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QThread, Signal, Slot

from copyclare.model import AccuracyModel
from copyclare import DATA_PATH
import time


class CameraThread(QThread):
    update_frame = Signal(QImage)

    def __init__(self, frame):
        QThread.__init__(self, None)
        self.frame = frame
        self.worker = CameraWorker()

    def run(self):

        for frame in self.worker.work():
            _, _, width, height = self.frame.frameGeometry().getRect()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)
            scaled_img = img.scaled(width, height,
                                    Qt.KeepAspectRatioByExpanding)

            self.update_frame.emit(scaled_img)


class VideoThread(QThread):
    update_frame = Signal(QImage)

    def __init__(self):
        QThread.__init__(self, None)
        self.worker = VideoWorker()

    def run(self):

        for frame in self.worker.work():
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)
            scaled_img = img.scaled(300, 300, Qt.KeepAspectRatioByExpanding)

            self.update_frame.emit(scaled_img)


class VideoWorker:
    def work(self):

        # TODO: Replace with a model call
        video_path = DATA_PATH + "/videos/sample1.mp4"

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print("Error opening a video file")

        frame_count = 0

        while (cap.isOpened):

            success, frame = cap.read()

            if not success:
                print("Can't read from Camera")

            frame_count += 1

            if frame_count == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                frame_count = 0
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

            fps = 30

            time.sleep(1 / fps)

            yield frame


class CameraWorker:
    def work(self):

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error opening a video file")

        while cap.isOpened():

            success, frame = cap.read()

            if not success:
                print("Can't read from Camera")

            yield frame
