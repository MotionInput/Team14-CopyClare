"""
Contributors: Adi Bozzhanov, Yan Lai, Sree Sanakkayala

"""

import os
from copyclare.data import DATA_DIR
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from copyclare.data.exporter import AccuracyGraphExporter
from copyclare.pyui.analysis import Ui_analysis_page
from copyclare.common import AppSingleton
from copyclare import UiElement


class AnalysisPage(UiElement):
    """
    Initialise the analysis page for selected attempt.

    Set the text for all information, draw and display the accuracy graph,
    and display the image of exercise.

    Args:
        master (ParentWidget): The frame in which the page will be displayed in.
        attempt (Attempt): The attempt to be displayed.

    """
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

        self.accuracyGraphExporter = AccuracyGraphExporter()
        graphWidget = self.accuracyGraphExporter.draw_accuracy_graph(
            self.attempt.session_json)
        self.ui.verticalLayout_graph.addWidget(graphWidget)

        img_path = DATA_DIR + f"/images/{self.attempt.exercise_id}.png"
        if os.path.exists(img_path):
            pixmap = QPixmap(img_path)
            pixmap = pixmap.scaled(420, 380, Qt.KeepAspectRatio)
            self.ui.ex_image.setPixmap(pixmap)
        else:
            pixmap = QPixmap(":icons/default-video-img.png")
            pixmap = pixmap.scaled(420, 380, Qt.KeepAspectRatio)
            self.ui.ex_image.setPixmap(pixmap)

        self.ui.back_button.clicked.connect(
            lambda x: self.app.load_page("progress"))
