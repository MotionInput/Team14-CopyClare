from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Slot
from PySide6.QtCharts import QChart, QChartView, QLineSeries

from PySide6.QtMultimedia import (QMediaPlayer)

# for testing
import random

from copyclare.video import VideoThread, CameraThread

from .page import Page

# when the page is loaded start 2 threads

# user camera thread, that will manage user camera


class ExercisePage(Page):
    def __init__(self, master):
        super().__init__(master, "exercise")
        self.init_chart()
        self.init_video()
        self.init_camera()

    def init_chart(self):
        self.series = QLineSeries()

        for i in range(10):
            self.series.append(i, random.randint(0, 20))

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Accuracy")

        self.chartView = QChartView(self.chart, parent=self.ui.graph_frame)
        self.ui.graph_layout.addWidget(self.chartView)

    def init_video(self):
        self.video_thread = VideoThread()
        self.video_thread.update_frame.connect(self.update_video)
        self.video_thread.start()

    def init_camera(self):

        self.camera_thread = CameraThread(self.ui.camera_frame)
        self.camera_thread.update_frame.connect(self.update_camera)
        self.camera_thread.start()

    @Slot(QImage)
    def update_video(self, image):
        self.ui.video_label.setPixmap(QPixmap.fromImage(image))

    @Slot(QImage)
    def update_camera(self, image):
        self.ui.camera_label.setPixmap(QPixmap.fromImage(image))
