from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Slot, Signal
from PySide6.QtCharts import QChart, QChartView, QLineSeries

from PySide6.QtMultimedia import (QMediaPlayer)

# for testing
import random
import json

from copyclare.video import VideoThread, CameraThread, ThreadManager
from copyclare.common import AppSingleton


from .page import Page

# when the page is loaded start 2 threads

# user camera thread, that will manage user camera


class ExercisePage(Page):
    done = Signal()

    def __init__(self, master, exercise):
        super().__init__(master, "exercise")

        self.exercise = exercise
        self.tm = ThreadManager()
        self.init_chart()
        self.init_video()
        self.init_camera()
        self.ui.end_button.clicked.connect(self.stop_all)

    def stop_all(self):
        print("Trying to stop stuff")
        self.video_thread._running = False
        self.camera_thread._running = False



    def init_chart(self):
        self.series = QLineSeries()

        a = json.loads(self.exercise.angles_json)

        for t in a["left_elbow"]:
            self.series.append(float(t), a["left_elbow"][t])



        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Accuracy")

        self.chartView = QChartView(self.chart, parent=self.ui.graph_frame)
        self.ui.graph_layout.addWidget(self.chartView)

    def init_video(self):
        self.video_thread = VideoThread(self.ui.video_frame, self.exercise)
        self.tm.add_thread(self.video_thread)
        self.video_thread.update_frame.connect(self.update_video)
        self.video_thread.start()

    def init_camera(self):
        self.camera_thread = CameraThread(self.ui.camera_frame, self.exercise)
        self.tm.add_thread(self.camera_thread, True)
        self.camera_thread.update_frame.connect(self.update_camera)
        self.camera_thread.start()

    @Slot(QImage)
    def update_video(self, image):
        self.ui.video_label.setPixmap(QPixmap.fromImage(image))

    @Slot(QImage)
    def update_camera(self, image):
        self.ui.camera_label.setPixmap(QPixmap.fromImage(image))
