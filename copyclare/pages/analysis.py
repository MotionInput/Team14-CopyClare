"""
AnalysisPage`


"""

import os
import json
import pyqtgraph as pg
from pyqtgraph import exporters
from PySide6.QtGui import QPixmap

from copyclare.data import DATA_DIR
from copyclare.pyui.analysis import Ui_analysis_page
from copyclare.common import AppSingleton
from copyclare import UiElement


class AnalysisPage(UiElement):
    def __init__(self, master, attempt):
        super().__init__(master, "analysis", Ui_analysis_page)
        self.attempt = attempt

        self.app = AppSingleton.get_app()
        name, desc = self.app.db.get_exercise_name_and_desc_by_ID(
            self.attempt.exercise_id)

        self.ui.name.setText(name)
        self.ui.description.setText(desc)
        self.ui.date.setText(self.attempt.date)
        self.ui.repetitions.setText(str(self.attempt.num_of_repetitons))
        self.ui.accuracy.setText(str(self.attempt.accuracy))

        graphWidget = self.draw_accuracy_graph(self.attempt.session_json)
        self.ui.verticalLayout_graph.addWidget(graphWidget)

        self.export_accuracy_graph(self.attempt.session_json, self.attempt.id)

        # TODO put exercise image here
        """img_path = DATA_DIR + f"/test/{exercise.id}.png"
        if os.path.exists(img_path):
            self.ui.ex_image.setPixmap(QPixmap(img_path))
        else:
            self.ui.ex_image.setPixmap(
                QPixmap(DATA_DIR + "/assets/default-video-img.png"))"""

        self.ui.back_button.clicked.connect(
            lambda x: self.app.load_page("progress"))

    def draw_accuracy_graph(self, session_json):
        graphWidget = pg.PlotWidget()

        x_axis = []
        y_axis = []

        accuracy = json.loads(session_json)

        for pair in accuracy:
            x_axis.append(pair[0]) # timestamp
            y_axis.append(pair[1]) # accuracy

        graphWidget.setBackground('w')
        graphWidget.setTitle("Accuracy throughout exercise (recorded by second)", color="black", size="15pt")
        graphWidget.showGrid(x=True, y=True)
        graphWidget.setXRange(x_axis[0], x_axis[-1], padding=0)
        graphWidget.setYRange(0, 100, padding=0)

        pen = pg.mkPen(color=(0, 20, 40), width=3)
        graphWidget.plot(x_axis, y_axis, name="",  pen=pen, symbol='o', symbolSize=2, symbolBrush=('#003366'))

        return graphWidget

    def export_accuracy_graph(self, session_json, attempt_id):
        path = DATA_DIR + '/accuracy-graphs/' + str(attempt_id) + '.png'
        exists = os.path.exists(path)
        if not exists:
            accuracy_graph = self.draw_accuracy_graph(session_json)
            exporter = exporters.ImageExporter(accuracy_graph.plotItem)
            exporter.parameters()['width'] = 500
            exporter.parameters()['height'] = 400
            exporter.export(path)
