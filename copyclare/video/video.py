import cv2
from PySide6.QtGui import QImage
from PySide6.QtCore import Qt, QThread, Signal, QRect

from copyclare import DATA_PATH
import time


class VideoThread(QThread):
    update_frame = Signal(QImage)

    def __init__(self, container):
        QThread.__init__(self, None)
        self.container = container
        self._running = True
        self.worker = VideoWorker()

    def run(self):

        for frame in self.worker.work():

            if not self._running:
                break
            _, _, width, height = self.container.frameGeometry().getRect()
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            img = QImage(frame.data, w, h, w * ch, QImage.Format_RGB888)
            if (w / h > 1):
                offset = (w - (width * h / height)) / 2
            else:
                offset = 0
            rect = QRect(offset, 0, w, h)
            img = img.copy(rect)
            img = img.scaled(width, height, Qt.KeepAspectRatioByExpanding)
            self.update_frame.emit(img)


class VideoWorker:
    def work(self):

        # TODO: Replace with a model call
        video_path = DATA_PATH + "/videos/sample2.mp4"

        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)

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

            time.sleep(1 / fps)

            yield frame