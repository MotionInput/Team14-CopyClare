from PySide6.QtWidgets import QFrame, QLabel, QTabWidget
from PySide6.QtCharts import QChart, QChartView, QLineSeries
from PySide6.QtCore import QMargins

from copyclare.widgets.progress_chart_graph import ProgressChartGraphWidget

from copyclare.common import load_ui, AppSingleton


class ProgressChartWidget(QFrame):
    def __init__(self, master, all_ex_attempt):
        super().__init__(master)
        self.ui = load_ui("progress_chart")
        self.ui.setupUi(self)

        self.app = AppSingleton.get_app()
        self.tabWidget = QTabWidget()
        self.tabWidget.setStyleSheet("color: #000000;")

        for ex_type in all_ex_attempt:
            if ex_type:
                name, desc = self.app.db.get_exercise_name_and_desc_by_ID(
                    ex_type[0].exercise_id)

                temp_widget = ProgressChartGraphWidget(self)
                self.series = QLineSeries()

                for i in range(len(ex_type)):
                    self.series.append(i + 1, ex_type[i].accuracy)

                self.chart = QChart()
                self.chart.addSeries(self.series)
                self.chart.createDefaultAxes()
                self.chart.setAnimationOptions(QChart.AllAnimations)
                self.chart.setTitle("Average Accuracy (for each attempt)")
                self.chart.legend().hide()
                self.chart.setMargins(QMargins(0, 0, 0, 0))
                self.ax1 = self.chart.axisX(self.series)
                self.ax2 = self.chart.axisY(self.series)
                self.ax2.setMin(0)
                self.ax2.setMax(100)

                self.chartView = QChartView(self.chart, parent=temp_widget)
                temp_widget.ui.verticalLayout.addWidget(self.chartView)

                self.tabWidget.addTab(temp_widget, name)

                self.ui.verticalLayout.insertWidget(0, self.tabWidget)
