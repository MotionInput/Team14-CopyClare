import os
import pyqtgraph as pg
from pyqtgraph import exporters
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QMargins
from PySide6.QtWidgets import QFrame, QLabel, QTabWidget

from copyclare.data import DATA_DIR
from copyclare.common import AppSingleton, load_ui
from copyclare.widgets.progress_chart_graph import ProgressChartGraphWidget
from copyclare.pyui.progress_chart import Ui_Frame
from copyclare import UiElement


class ProgressChartWidget(UiElement):
    def __init__(self, master, all_ex_attempt):
        super().__init__(master, "progress_chart", Ui_Frame)

        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet("color: #000000;")

        self._create_tab_widget(all_ex_attempt)
        self.ui.verticalLayout.insertWidget(0, self.tabWidget)

        self.export_progress_charts(all_ex_attempt)

    def _create_tab_widget(self, all_ex_attempt):
        graphWidgets = self.draw_progress_charts(all_ex_attempt)
        for graph in graphWidgets:
            temp_widget = ProgressChartGraphWidget(self)
            temp_widget.ui.verticalLayout.addWidget(graph[0])
            self.tabWidget.addTab(temp_widget, graph[1])

    def draw_progress_charts(self, all_ex_attempt):
        app = AppSingleton.get_app()
        graphWidgets = []
        for ex_type in all_ex_attempt:
            if ex_type:
                name, desc = app.db.get_exercise_name_and_desc_by_ID(
                    ex_type[0].exercise_id)

                graphWidget = pg.PlotWidget()

                x_axis = []
                y_axis = []

                for i in range(len(ex_type)):
                    x_axis.append(i + 1)
                    y_axis.append(ex_type[i].accuracy)

                graphWidget.setBackground('w')
                graphWidget.setTitle(
                    "Average Accuracy (for each attempt): " + name,
                    color="black",
                    size="15pt")
                graphWidget.getPlotItem().hideAxis('bottom')
                graphWidget.showGrid(x=True, y=True)
                graphWidget.setXRange(1, len(ex_type), padding=0)
                graphWidget.setYRange(0, 100, padding=0)

                pen = pg.mkPen(color=(0, 20, 40), width=3)
                graphWidget.plot(x_axis,
                                      y_axis,
                                      name="",
                                      pen=pen,
                                      symbol='o',
                                      symbolSize=8,
                                      symbolBrush=('#003366'))

                graph = []
                graph.append(graphWidget); graph.append(name); graph.append(ex_type[0].exercise_id)
                graphWidgets.append(graph)

        return graphWidgets

    def export_progress_charts(self, all_ex_attempt):
        progress_charts = self.draw_progress_charts(all_ex_attempt)
        for chart in progress_charts:
            path = DATA_DIR + '/progress-charts/' + str(chart[2]) + '.png'
            exists = os.path.exists(path)
            if not exists:
                exporter = exporters.ImageExporter(chart[0].plotItem)
                exporter.parameters()['width'] = 500
                exporter.parameters()['height'] = 400
                exporter.export(path)
