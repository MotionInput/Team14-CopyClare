import time

import cv2
from PySide6.QtCore import QRect, Qt, QThread, Signal
from PySide6.QtGui import QImage

from copyclare.data import DATA_DIR


class VideoThread(QThread):
    update_frame = Signal(QImage)

    def __init__(self, container, exercise):
        QThread.__init__(self, None)
        self.container = container
        self._running = True
        self.worker = VideoWorker(exercise)

    def run(self):

        for frame in self.worker.work():

            if not self._running:
                break
            _, _, width, height = self.container.frameGeometry().getRect()

            try:
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
            except:
                pass
        self.quit()


class VideoWorker:
    def __init__(self, exercise):
        self.video_path = DATA_DIR + exercise.video_directory

    def work(self):
        # TODO: Replace with a model call
        cap = cv2.VideoCapture(self.video_path)
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
            frame = cv2.flip(frame, 1)
            yield frame
