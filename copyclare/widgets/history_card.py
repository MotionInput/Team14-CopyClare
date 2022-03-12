from PySide6.QtWidgets import QFrame
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from copyclare import DATA_PATH
from copyclare.common import load_ui

class HistoryCardWidget(QFrame):
    def __init__(self, master, attempt, img_path):
        super().__init__(master)
        self.ui = load_ui("history_card")
        self.ui.setupUi(self)

        self.ui.title.setText(attempt.exercise_id)
        self.ui.date.setText(attempt.date)

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
