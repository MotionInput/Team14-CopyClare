from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QFrame

from copyclare.common import AppSingleton, load_ui
from copyclare.data import DATA_DIR, Exporter
from copyclare.pyui.history_card import Ui_Form
from copyclare import UiElement


class HistoryCardWidget(UiElement):
    def __init__(self, master, attempt, img_path):
        super().__init__(master, "history_card", Ui_Form)
        self.app = AppSingleton.get_app()

        self.ui.exercise_img.setPixmap(
            QPixmap(DATA_DIR + "/assets/default-video-img.png"))

        name, desc = self.app.db.get_exercise_name_and_desc_by_ID(
            attempt.exercise_id)
        self.ui.title.setText(name)
        self.ui.date.setText(attempt.date)

        icon = QIcon()
        icon.addFile(DATA_DIR + "/assets/analysis.png", QSize(), QIcon.Normal,
                     QIcon.Off)
        self.ui.analysis_button.setIcon(icon)
        self.ui.analysis_button.setIconSize(QSize(64, 64))

        icon = QIcon()
        icon.addFile(DATA_DIR + "/assets/export.png", QSize(), QIcon.Normal,
                     QIcon.Off)
        self.ui.export_button.setIcon(icon)
        self.ui.export_button.setIconSize(QSize(64, 64))

        self.ui.analysis_button.clicked.connect(
            lambda x: self._create_analysis_page(attempt))

        self.ui.export_button.clicked.connect(
            lambda x: self._export(attempt.id))

    def _create_analysis_page(self, attempt):
        self.app.load_page("analysis", attempt)

    # TODO link export button to function
    def _export(self, attempt_id):
        exporter = Exporter(self.app.db)
        exporter.export(DATA_DIR + "/results/" + "Results.docx", attempt_id)
