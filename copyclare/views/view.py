import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from ui.compiled.main_window import Ui_MainWindow
from pages.home import HomePage


class MainWindow(QMainWindow):

    pages = {
        "home": HomePage,
    }

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def load_page(self, page="home"):
        # add the page to the main frame
        new_page = self.pages[page](self)
        new_page.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()

    MainWindow.load_page("home")

    sys.exit(app.exec())
