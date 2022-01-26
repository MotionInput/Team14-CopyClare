import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from .ui.compiled.main_window import Ui_MainWindow
from .pages.home import HomePage


class View:

    pages = {
        "home": HomePage,
    }

    def start_ui(self):
        app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        sys.exit(app.exec())

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
        new_page = self.pages[page](self.ui.pages_frame)
        self.ui.pages_layout.addWidget(new_page)
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
