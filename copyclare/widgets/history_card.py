from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap

from copyclare import DATA_PATH
from copyclare.model import Exporter
from copyclare.common import load_ui, AppSingleton

class HistoryCardWidget(QFrame):
    def __init__(self, master, attempt, img_path):
        super().__init__(master)
        self.app = AppSingleton.get_app()
        self.ui = load_ui("history_card")
        self.ui.setupUi(self)

        self.ui.exercise_img.setPixmap(
            QPixmap(DATA_PATH + "/assets/default-video-img.png"))

        name, desc = self.app.db.get_exercise_name_and_desc_by_ID(attempt.exercise_id)
        self.ui.title.setText(name)
        self.ui.date.setText(attempt.date)

        icon = QIcon()
        icon.addFile(DATA_PATH + "/assets/analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.analysis_button.setIcon(icon)
        self.ui.analysis_button.setIconSize(QSize(64, 64))

        icon = QIcon()
        icon.addFile(DATA_PATH + "/assets/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.export_button.setIcon(icon)
        self.ui.export_button.setIconSize(QSize(64, 64))

        self.ui.analysis_button.clicked.connect(lambda x: self._create_analysis_page(attempt))

        self.ui.export_button.clicked.connect(lambda x: self._export())

    def _create_analysis_page(self, attempt):
        self.app.load_page("analysis", attempt)

    # TODO link export button to function
    def _export(self):
        exporter = Exporter(self.app.db)
        exporter.export("saveAs(?)") # TODO idk what the args are supposed to be
        print("sree work here")
