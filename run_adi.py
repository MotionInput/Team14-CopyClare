import sys

from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QHBoxLayout,
    QWidget,
    QFrame,
)

from PySide6.QtCore import (
    QSize, )

from copyclare.pages import ExercisePage
from copyclare.common import load_ui

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = load_ui("main_window")
    ui.setupUi(window)

    page = ExercisePage(ui.pages_frame)
    ui.pages_layout.addWidget(page)

    window.showMaximized()

    sys.exit(app.exec())
