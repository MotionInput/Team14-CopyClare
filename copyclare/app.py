import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from copyclare import DATA_PATH
from .common import load_ui
from .pages import HomePage, NotFound, ProfilePage


class App:


    pages = {
        "home": HomePage,
        "not_found": NotFound,
        "progress": ProfilePage,
    }



    def start_ui(self):
        self.current_page = None

        # App necessary setup
        app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.showMaximized()
        self.ui = load_ui("main_window")
        self.ui.setupUi(self.window)

        # edit for the ui button
        icon = QIcon()
        print(DATA_PATH + "/home.png")
        icon.addFile(DATA_PATH + "/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.home_button.setIcon(icon)
        self.ui.home_button.setIconSize(QSize(64, 64))

        icon1 = QIcon()
        icon1.addFile(DATA_PATH + "/progress.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.ui.progress_button.setIcon(icon1)
        self.ui.progress_button.setIconSize(QSize(64, 64))

        icon2 = QIcon()
        icon2.addFile(DATA_PATH + "/settings.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.ui.settings_button.setIcon(icon2)
        self.ui.settings_button.setIconSize(QSize(64, 64))

        icon3 = QIcon()
        icon3.addFile(DATA_PATH + "/navlines.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.ui.nav_button.setIcon(icon3)
        self.ui.settings_button.setIconSize(QSize(64, 64))

        self.window.show()

        # UI setup
        self.init_pages()
        self.load_page("home")

        # buttons init
        self.ui.home_button.clicked.connect(lambda x: self.load_page("home"))
        self.ui.settings_button.clicked.connect(
            lambda x: self.load_page("settings"))
        self.ui.progress_button.clicked.connect(
            lambda x: self.load_page("progress"))

        self.ui.nav_button.clicked.connect(self.nav_click)

        sys.exit(app.exec())

    def get_pages(self):
        """
        Spits out a set of pages.

        Returns:
            :obj:`set`
        """
        return self.pages.keys()

    def init_pages(self):
        for page in self.pages:
            _page_obj = self.pages[page](self.ui.pages_frame)
            _page_obj.hide()
            self.pages[page] = _page_obj
            self.ui.pages_layout.addWidget(_page_obj)

    def load_page(self, page="home"):
        """
        Loads a page given the page name
        """
        if self.current_page is not None:
            self.current_page.hide()

        if page in self.pages:
            self.current_page = self.pages[page]
        else:
            print(f"Could not find page: {page}")
            self.current_page = self.pages["not_found"]

        self.current_page.show()

    def nav_click(self):

        print("nav clicked!")
