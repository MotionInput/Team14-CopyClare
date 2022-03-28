import pyqtgraph as pg

from PySide6.QtWidgets import QFrame, QLabel, QTabWidget

from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QMargins
from PySide6.QtWidgets import QFrame, QLabel, QTabWidget

from copyclare.common import AppSingleton, load_ui
from copyclare.widgets.progress_chart_graph import ProgressChartGraphWidget


class ProgressChartWidget(QFrame):
    def __init__(self, master, all_ex_attempt):
        super().__init__(master)
        self.ui = load_ui("progress_chart")
        self.ui.setupUi(self)

        self.app = AppSingleton.get_app()
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet("color: #000000;")

        self._draw_charts(all_ex_attempt)
        self.ui.verticalLayout.insertWidget(0, self.tabWidget)

    def update_progress_chart(self, all_ex_attempt):
        self._draw_charts(all_ex_attempt)

    def _draw_charts(self, all_ex_attempt):
        for ex_type in all_ex_attempt:
            if ex_type:
                name, desc = self.app.db.get_exercise_name_and_desc_by_ID(
                    ex_type[0].exercise_id)

                temp_widget = ProgressChartGraphWidget(self)

                self.graphWidget = pg.PlotWidget()

                x_axis = []
                y_axis = []

                for i in range(len(ex_type)):
                    x_axis.append(i + 1)
                    y_axis.append(ex_type[i].accuracy)

                self.graphWidget.setBackground('w')
                self.graphWidget.setTitle("Average Accuracy (for each attempt)", color="black", size="15pt")
                self.graphWidget.getPlotItem().hideAxis('bottom')
                self.graphWidget.showGrid(x=True, y=True)
                self.graphWidget.setXRange(1, len(ex_type), padding=0)
                self.graphWidget.setYRange(0, 100, padding=0)

                pen = pg.mkPen(color=(0, 20, 40), width=3)
                self.graphWidget.plot(x_axis, y_axis, name="",  pen=pen, symbol='o', symbolSize=8, symbolBrush=('#003366'))

                temp_widget.ui.verticalLayout.addWidget(self.graphWidget)

                self.tabWidget.addTab(temp_widget, name)
