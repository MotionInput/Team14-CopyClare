"""
Contributors: Adi Bozzhanov, Yan Lai

"""

import json
# for testing
import random
import time

from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QImage, QPixmap

from copyclare.pyui.exercise import Ui_exercise_frame
from copyclare.video import CameraThread, ThreadManager, VideoThread
from copyclare import UiElement

# when the page is loaded start 2 threads

# user camera thread, that will manage user camera


class ExercisePage(UiElement):
    """
    Initialise and run the exercise page.

    Update the live accuracy graph and repetition counter.
    Display sample exercise video and patient's camera.

    Args:
        master (ParentWidget): The frame in which the page will be displayed in.
        exercise (Exercise):

    """

    done = Signal()

    def __init__(self, master, exercise):
        super().__init__(master, "exercise", Ui_exercise_frame)

        self.exercise = exercise
        self.tm = ThreadManager()
        self.init_video()
        self.init_camera()
        self.ui.end_button.clicked.connect(self.stop_all)
        self.ui.flip_button.clicked.connect(self.camera_thread.toggle_flipped)
        self.start = time.time()

    def stop_all(self):
        print("Trying to stop stuff")
        self.video_thread._running = False
        self.camera_thread._running = False

    def init_video(self):
        self.video_thread = VideoThread(self.ui.video_frame, self.exercise)
        self.tm.add_thread(self.video_thread)
        self.video_thread.update_frame.connect(self.update_video)
        self.video_thread.start()

    def init_camera(self):
        self.camera_thread = CameraThread(self.ui.camera_frame, self.exercise.id)
        self.tm.add_thread(self.camera_thread, True)
        self.camera_thread.update_frame.connect(self.update_camera)
        self.camera_thread.update_reps.connect(self.update_reps)
        self.camera_thread.update_graph.connect(self.update_graph)
        self.camera_thread.update_progress.connect(self.update_progress)
        self.camera_thread.start()

    @Slot(QImage)
    def update_video(self, image):
        self.ui.video_label.setPixmap(QPixmap.fromImage(image))

    @Slot(QImage)
    def update_camera(self, image):
        self.ui.camera_label.setPixmap(QPixmap.fromImage(image))

    @Slot(int)
    def update_reps(self, reps):
        self.ui.reps_label.setText(f"Reps: {reps}")

    @Slot(list)
    def update_graph(self, accuracy_vals):

        self.series.clear()

        if len(accuracy_vals) == 0:
            now = 0
        else:
            now = accuracy_vals[-1][0]

        for t, accuracy in accuracy_vals:
            self.series.append(t, accuracy)

        self.ax2.setMin(0)
        self.ax2.setMin(100)
        self.ax1.setMin(now - 5)
        self.ax1.setMax(now)

    @Slot(int)
    def update_progress(self, progress):
        self.ui.progressBar.setValue(progress)
