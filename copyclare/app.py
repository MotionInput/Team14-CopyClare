import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from copyclare.common import load_ui
from copyclare.data import DATA_DIR, DB_DIR, Database
from copyclare.data.objects import Attempt, Tag
from copyclare.pages import (AnalysisPage, ExercisePage, HomePage, NotFound,
                             ProfilePage, VideoAddition)
from copyclare.widgets import TutorialPopupWidget, VideoCardWidget


class App:

    pages = {
        "home": HomePage,
        "not_found": NotFound,
        "progress": ProfilePage,
        "video_addition": VideoAddition,
    }

    def start_ui(self):
        self.current_page = None
        self.db = Database(DB_DIR)

        # App necessary setup
        app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.showMaximized()
        self.ui = load_ui("main_window")
        self.ui.setupUi(self.window)

        self.ui.exercise_frame.hide()
        self.current_exercise_page = None

        # edit for the ui button
        icon = QIcon()
        icon.addFile(DATA_DIR + "/assets/home.png", QSize(), QIcon.Normal,
                     QIcon.Off)

        self.ui.home_button.setIcon(icon)
        self.ui.home_button.setIconSize(QSize(64, 64))

        icon1 = QIcon()
        icon1.addFile(DATA_DIR + "/assets/progress.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.ui.progress_button.setIcon(icon1)
        self.ui.progress_button.setIconSize(QSize(64, 64))

        icon2 = QIcon()
        icon2.addFile(DATA_DIR + "/assets/settings.png", QSize(), QIcon.Normal,
                      QIcon.Off)
        self.ui.settings_button.setIcon(icon2)
        self.ui.settings_button.setIconSize(QSize(64, 64))

        icon3 = QIcon()
        icon3.addFile(DATA_DIR + "/assets/icon-addvideo.png", QSize(),
                      QIcon.Normal, QIcon.Off)
        self.ui.addvideo_button.setIcon(icon3)
        self.ui.addvideo_button.setIconSize(QSize(64, 64))

        self.window.show()

        # UI setup
        self.init_pages()
        self.load_page()

        # buttons init
        self.ui.home_button.clicked.connect(lambda x: self.load_page("home"))
        self.ui.settings_button.clicked.connect(
            lambda x: self.load_page("settings"))
        self.ui.progress_button.clicked.connect(
            lambda x: self.load_page("progress"))
        self.ui.addvideo_button.clicked.connect(lambda x: self.load_page("video_addition"))


        tutorial_popup = TutorialPopupWidget()
        tutorial_popup.show()

        sys.exit(app.exec())

    def start_exercise(self, exercise):
        """
        Hide all the contents including navbar
        and create and exercise instacne

        Upon completion of the exercise process,
        log the results of the attempt in the database.
        """

        self.ui.side_nav.hide()
        self.ui.pages_frame.hide()

        self.ui.exercise_frame.show()
        print("HELLO ADI WAS HERE")
        ex_page = ExercisePage(self.ui.exercise_frame, exercise)
        self.current_exercise_page = ex_page
        self.ui.exercise_layout.addWidget(ex_page)

    def end_exercise(self, attempt):
        self.ui.exercise_frame.hide()
        self.ui.side_nav.show()
        self.ui.pages_frame.show()
        self.db.add_attempt(attempt)
        self.pages["progress"].add_attempt(attempt)

        if self.current_exercise_page is not None:
            self.current_exercise_page.deleteLater()
            self.current_exercise_page = None

    def get_pages(self):
        """
        Spits out a set of pages.

        Returns:
            :obj:`set`
        """

        return self.pages.keys()

    def move_to_my_exercises(self, ex):
        tag = Tag("My Exercises")
        banner = self.pages["home"].banners[tag.tag_name]

        # database stuff
        if str(ex.id) not in banner.cards:

            self.db.add_tag_to_exercise(tag, ex)

            # Video card object
            banner.cards[str(ex.id)] = VideoCardWidget(banner.ui.scrollArea,
                                                       ex)
            banner.ui.horizontalLayout.insertWidget(0,
                                                    banner.cards[str(ex.id)])

    def remove_from_my_exercises(self, ex):
        pass

    def init_pages(self):
        for page in self.pages:
            _page_obj = self.pages[page](self.ui.pages_frame)
            _page_obj.hide()
            self.pages[page] = _page_obj
            self.ui.pages_layout.addWidget(_page_obj)

    def load_page(self, page="home", attempt=None):
        """
        Loads a page given the page name
        """
        if self.current_page is not None:
            self.current_page.hide()

        if page == "analysis":
            _analysis_page_obj = AnalysisPage(self.ui.pages_frame, attempt)
            self.ui.pages_layout.addWidget(_analysis_page_obj)
            self.current_page = _analysis_page_obj
        elif page in self.pages:  # these pages are the same each time you load
            self.current_page = self.pages[page]
        else:
            print(f"Could not find page: {page}")
            self.current_page = self.pages["not_found"]

        self.current_page.show()

    def nav_click(self):

        print("nav clicked!")
