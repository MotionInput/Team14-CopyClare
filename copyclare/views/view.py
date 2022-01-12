import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from ui.compiled.main_window import Ui_MainWindow
from pages.home import HomePage


class View(QMainWindow):

    pages = {
        "home": HomePage,
    }

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def get_pages(self):
        """
        Spits out a set of pages.

        Returns:
            :obj:`set`
        """
        return self.pages.keys()

    def load_page(self, page="home"):
        """
        Loads a page given the page name

        Parameters:
            page-(:obj:`str`)
        """
        new_page = self.pages[page](self)
        new_page.show()

    def update(self):
        """
        Updates the existing page with new information

        """

        pass

    def _clear_page(self):
        """
        Clears the page from all widgets
        """

        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    View = View()
    View.show()

    View.load_page("home")

    sys.exit(app.exec())
