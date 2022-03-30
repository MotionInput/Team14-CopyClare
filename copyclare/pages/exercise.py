import json
# for testing
import random
import time

from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtMultimedia import QMediaPlayer

from copyclare.pyui.exercise import Ui_exercise_frame
from copyclare.common import AppSingleton
from copyclare.video import CameraThread, ThreadManager, VideoThread
from copyclare import UiElement

# when the page is loaded start 2 threads

# user camera thread, that will manage user camera


class ExercisePage(UiElement):
    done = Signal()

    def __init__(self, master, exercise):
        super().__init__(master, "exercise", Ui_exercise_frame)

        self.exercise = exercise
        self.tm = ThreadManager()
        self.init_chart()
        self.init_video()
        self.init_camera()
        self.ui.end_button.clicked.connect(self.stop_all)
        self.start = time.time()

    def stop_all(self):
        print("Trying to stop stuff")
        self.video_thread._running = False
        self.camera_thread._running = False

    def init_chart(self):

        self.chart = QChart()
        self.series = QLineSeries(self.chart)
        self.chart.legend().hide()
        self.chart.addSeries(self.series)

        self.chart.createDefaultAxes()
        self.chartView = QChartView(self.chart, parent=self.ui.graph_frame)
        self.ui.graph_layout.addWidget(self.chartView)
        self.ax1 = self.chart.axisX(self.series)
        self.ax2 = self.chart.axisY(self.series)

    def init_video(self):
        self.video_thread = VideoThread(self.ui.video_frame, self.exercise)
        self.tm.add_thread(self.video_thread)
        self.video_thread.update_frame.connect(self.update_video)
        self.video_thread.start()

    def init_camera(self):
        self.camera_thread = CameraThread(self.ui.camera_frame, self.exercise)
        self.tm.add_thread(self.camera_thread, True)
        self.camera_thread.update_frame.connect(self.update_camera)
        self.camera_thread.update_reps.connect(self.update_reps)
        self.camera_thread.update_graph.connect(self.update_graph)
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
