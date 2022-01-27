import os
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QFrame
from common import load_ui

from .pages import *


class View:

    pages = {
        "home": HomePage,
        "not_found": NotFound,
        "exercise": ExercisePage,
        "profile": ProfilePage,
    }

    def start_ui(self):
        self.current_page = None

        # App necessary setup
        app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.showMaximized()
        self.ui = load_ui("main_window")
        self.ui.setupUi(self.window)
        self.window.show()

        # UI setup
        self.init_pages()
        self.init_buttons()
        self.load_page("home")

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

    def init_buttons(self):
        self.ui.exercise_button.clicked.connect(lambda x: self.load_page("exercise"))
        self.ui.home_button.clicked.connect(lambda x: self.load_page("home"))
        self.ui.profile_button.clicked.connect(lambda x: self.load_page("profile"))
        self.ui.analysis_button.clicked.connect(lambda x: self.load_page("analysis"))
