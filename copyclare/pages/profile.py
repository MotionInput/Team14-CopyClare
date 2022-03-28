from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QStackedWidget, QTabWidget
from copyclare.widgets.export_all_banner import ExportAllBannerWidget

from copyclare.widgets.history_card import HistoryCardWidget
from copyclare.widgets.past_attempts_banner import PastAttemptsBannerWidget
from copyclare.widgets.progress_banner import ProgressBannerWidget
from copyclare.widgets.progress_chart import ProgressChartWidget
from copyclare.common import AppSingleton
from copyclare.model.attempt import Attempt

from .page import Page


class ProfilePage(Page):
    def __init__(self, master):
        super().__init__(master, "profile")

        self.app = AppSingleton.get_app()

        # progress chart

        self.progress_chart_banner = ProgressBannerWidget(
            self, "Progress chart")
        self.ui.verticalLayout_2.insertWidget(0, self.progress_chart_banner)

        all_ex_attempt = self.app.db.get_attempt_in_exercise()
        print(all_ex_attempt)
        self.progress_chart = ProgressChartWidget(self, all_ex_attempt)
        self.progress_chart_banner.ui.verticalLayout_2.insertWidget(
            0, self.progress_chart)

        # past attempts

        self.past_attempts_banner = PastAttemptsBannerWidget(self)
        self.ui.verticalLayout_2.insertWidget(1, self.past_attempts_banner)

        _all_attempts = self.app.db.get_all_attempts()

        for _attempt in _all_attempts:
            _history_card = HistoryCardWidget(
                self.past_attempts_banner.ui.scrollArea, _attempt, None)
            self.past_attempts_banner.ui.verticalLayout_2.insertWidget(
                0, _history_card)

    def add_attempt(self, attempt):
        _history_card = HistoryCardWidget(
            self.past_attempts_banner.ui.scrollArea, attempt, None)
        self.past_attempts_banner.ui.verticalLayout_2.insertWidget(
            0, _history_card)
