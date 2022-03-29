from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QFileDialog

from copyclare.common import AppSingleton
from copyclare.data import DATA_DIR, Exporter
from copyclare.pyui.history_card import Ui_Form
from copyclare import UiElement

import res_rc

class HistoryCardWidget(UiElement):
    def __init__(self, master, attempt, img_path):
        super().__init__(master, "history_card", Ui_Form)
        self.app = AppSingleton.get_app()

        self.ui.exercise_img.setPixmap(
            QPixmap(":icons/default-video-img.png"))

        name, desc = self.app.db.get_exercise_name_and_desc_by_ID(
            attempt.exercise_id)
        self.ui.title.setText(name)
        self.ui.date.setText(attempt.date)

        self.ui.analysis_button.clicked.connect(
            lambda x: self._create_analysis_page(attempt))

        self.ui.export_button.clicked.connect(
            lambda x: self._export(attempt.id))

    def _create_analysis_page(self, attempt):
        self.app.load_page("analysis", attempt)

    def _export(self, attempt_id):
        exporter = Exporter(self.app.db)
        file_path, selectedFilter = QFileDialog.getSaveFileName(
            filter="*.docx")
        exporter.export(file_path.strip(
        )+".docx" if "." not in file_path else file_path.strip(), attempt_id)
