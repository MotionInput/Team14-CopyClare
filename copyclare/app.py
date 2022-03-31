"""
Contributors: Adi Bozzhanov, Yan Lai

"""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow


from copyclare.common import load_ui
from copyclare.data import DATA_DIR, DB_DIR, Database
from copyclare.data.exporter import AccuracyGraphExporter
from copyclare.data.objects import Tag
from copyclare.pages import (AnalysisPage, ExercisePage, HomePage, LandingPage, NotFound,
                             ProfilePage, VideoAddition)
from copyclare.pyui.main_window import Ui_MainWindow as compiled_ui
from copyclare.config import DEBUG
from copyclare.widgets.video_card import VideoCardWidget
from copyclare.widgets.video_card_my_ex import VideoCardMyExWidget


class App:
    """
    The App class manages all the switching between pages of the app.

    """

    pages = {
        "landing": LandingPage,
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

        # Ui load optimisation
        if DEBUG:
            self.ui = load_ui("main_window")
        else:
            self.ui = compiled_ui()

        self.ui.setupUi(self.window)

        # landing page
        self.ui.side_nav.hide()

        self.ui.exercise_frame.hide()
        self.current_exercise_page = None

        self.window.show()

        # UI setup
        self.init_pages()
        self.load_page()

        # buttons init
        self.ui.home_button.clicked.connect(lambda x: self.load_page("home"))
        self.ui.progress_button.clicked.connect(
            lambda x: self.load_page("progress"))
        self.ui.addvideo_button.clicked.connect(
            lambda x: self.load_page("video_addition"))

        sys.exit(app.exec())

    def start_exercise(self, exercise):
        """
        Hide all the contents including navbar
        and create an exercise instance

        Upon completion of the exercise process,
        log the results of the attempt in the database.
        """

        self.ui.side_nav.hide()
        self.ui.pages_frame.hide()

        self.ui.exercise_frame.show()
        ex_page = ExercisePage(self.ui.exercise_frame, exercise)
        self.current_exercise_page = ex_page
        self.ui.exercise_layout.addWidget(ex_page)

    def end_exercise(self, attempt):
        """
        Hides and deletes exercise page,
        and reveals all previously hidden contents

        Updates Profile page with new history card and progress chart,
        and exports accuracy graph of attempt

        """
        self.ui.exercise_frame.hide()
        self.ui.side_nav.show()
        self.ui.pages_frame.show()
        self.db.add_attempt(attempt)
        self.pages["progress"].add_attempt_history_card(attempt)
        self.pages["progress"].update_progress_chart(self.db.get_attempt_in_exercise())
        accuracyGraphExporter = AccuracyGraphExporter()
        accuracyGraphExporter.export_accuracy_graph(attempt.session_json, attempt.id)

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

    def add_video_card_to_banner(self, ex):
        """
        Adds a new video card for newly-added exercise in the 'Exercise Library' banner.

        Args:
            ex (Exercise): The newly-added exercise to be added to 'Exercise Library'.

        """
        banner = self.pages["home"].banners["Exercise Library"]

        self.db.add_exercise(ex)

        banner.cards[str(ex.id)] = VideoCardWidget(banner.ui.scrollArea, ex)
        banner.ui.horizontalLayout.insertWidget(0, banner.cards[str(ex.id)])

    def move_to_my_exercises(self, ex):
        """
        Adds a new video card for selected exercise in the 'My Exercises' banner.

        Args:
            ex (Exercise): The chosen exercise to be moved to 'My Exercises'.

        """
        tag = Tag("My Exercises")
        banner = self.pages["home"].banners[tag.tag_name]

        # database stuff
        if str(ex.id) not in banner.cards:

            self.db.add_tag_to_exercise(tag, ex)

            # Video card object
            banner.cards[str(ex.id)] = VideoCardMyExWidget(banner.ui.scrollArea,
                                                       ex)
            banner.ui.horizontalLayout.insertWidget(0,
                                                    banner.cards[str(ex.id)])

    def remove_from_my_exercises(self, ex):
        """
        Removes video card for selected exercise in the 'My Exercises' banner.

        Args:
            ex (Exercise): The chosen exercise to be removed from 'My Exercises'.

        """
        tag = Tag("My Exercises")
        banner = self.pages["home"].banners[tag.tag_name]

        if str(ex.id) in banner.cards:

            self.db.remove_tag_from_exercise(tag, ex)

            for i in range(banner.ui.horizontalLayout.count() - 1): # horizontal spacer
                if banner.ui.horizontalLayout.itemAt(i).widget().id == ex.id:
                    banner.ui.horizontalLayout.itemAt(i).widget().deleteLater()
                    banner.cards.pop(str(ex.id))

    def init_pages(self):
        for page in self.pages:
            _page_obj = self.pages[page](self.ui.pages_frame)
            _page_obj.hide()
            self.pages[page] = _page_obj
            self.ui.pages_layout.addWidget(_page_obj)

    def load_page(self, page="landing", attempt=None):
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
