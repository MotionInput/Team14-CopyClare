from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from copyclare import DATA_PATH
from copyclare.common import load_ui, AppSingleton

class HistoryCardWidget(QFrame):
    def __init__(self, master, attempt, img_path):
        super().__init__(master)
        self.app = AppSingleton.get_app()
        self.ui = load_ui("history_card")
        self.ui.setupUi(self)

        name, desc = self.app.db.get_exercise_name_and_desc_by_ID(attempt.exercise_id)
        self.ui.title.setText(name)
        self.ui.date.setText(desc)

        icon = QIcon()
        print(DATA_PATH + "/analysis.png")
        icon.addFile(DATA_PATH + "/analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.analysis_button.setIcon(icon)
        self.ui.analysis_button.setIconSize(QSize(64, 64))

        icon = QIcon()
        print(DATA_PATH + "/export.png")
        icon.addFile(DATA_PATH + "/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.export_button.setIcon(icon)
        self.ui.export_button.setIconSize(QSize(64, 64))

        self.ui.analysis_button.clicked.connect(lambda x: self._create_analysis_page(attempt))

        # TODO: SREEEEEEEEEE
        self.ui.export_button.clicked.connect(lambda x: self._export())

    def _create_analysis_page(self, attempt):
        self.app.load_page("analysis", attempt)

    def _export(self):
        print("sree work here")
