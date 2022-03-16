from copyclare.model.attempt import Attempt
from PySide6.QtCore import Qt
from copyclare.widgets.history_card import HistoryCardWidget

from copyclare.widgets.progress_banner import ProgressBannerWidget

from .page import Page


class ProfilePage(Page):
    def __init__(self, master):
        super().__init__(master, "profile")
        
        _banner = ProgressBannerWidget(self)
        self.ui.verticalLayout.insertWidget(0, _banner)


        # tester attempts
        adis_good_attempt = Attempt(4, "30-2-2022", 10, "10:00", 1, 78, "bankai") # TODO: should be numbers for exercise_id, but might need some way to link exercise_ids to titles
        ths_good_attempt = Attempt(3, "32-1-2022", 15, "01:70", 1, 90, "code no jutsu")
        yans_good_attempt = Attempt(2, "20-1-2022", 15, "10:00", 1, 83, "bankai")
        srees_failed_attempt = Attempt(1, "32-12-2021", 100, "04:20", 1, 5, "code no jutsu") # oldest attempt
        
        # TODO: get a list of attempts with newest attempt as 1st element
        _all_attempts = [adis_good_attempt, ths_good_attempt, yans_good_attempt, srees_failed_attempt]

        for _attempt in _all_attempts:
            _history_card = HistoryCardWidget(_banner.ui.scrollArea, _attempt, None)
            _banner.ui.verticalLayout_2.addWidget(_history_card)
