from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QWidget, QStackedWidget, QTabWidget

from copyclare.widgets.history_card import HistoryCardWidget
from copyclare.widgets.progress_banner import ProgressBannerWidget
from copyclare.widgets.progress_chart import ProgressChartWidget
from copyclare.common import AppSingleton
from copyclare.model.attempt import Attempt

from .page import Page


class ProfilePage(Page):
    def __init__(self, master):
        super().__init__(master, "profile")

        self.app = AppSingleton.get_app()

        # TODO rename everything properly - 'profile' = name of this whole page; 'progress chart'; 'past attempts'; 'profile_banner'

        # progress chart

        # tester filtered attempts
        #ex1_attempt = [Attempt(None,"1-1-1",1,1.11,"111",11,1), Attempt(None,"2-2-2",2,2.22,"222",22,1), Attempt(None,"3-3-3",3,3.33,"333",33,1), Attempt(None,"4-4-4",4,4.44,"444",44,1), Attempt(None,"5-5-5",5,5.55,"555",55,1)]
        #ex2_attempt = [Attempt(None,"1-1-1",1,1.11,"111",44,2), Attempt(None,"2-2-2",2,2.22,"222",33,2), Attempt(None,"3-3-3",3,3.33,"333",22,2), Attempt(None,"4-4-4",4,4.44,"444",11,2)]
        #ex3_attempt = [Attempt(None,"1-1-1",1,1.11,"111",33,3), Attempt(None,"2-2-2",2,2.22,"222",22,3), Attempt(None,"3-3-3",3,3.33,"333",11,3), Attempt(None,"4-4-4",4,4.44,"444",44,3), Attempt(None,"5-5-5",5,5.55,"555",55,3)]
        #ex4_attempt = [Attempt(None,"1-1-1",1,1.11,"111",22,4), Attempt(None,"2-2-2",2,2.22,"222",22,4)]
        #all_ex_attempt = [ex1_attempt, ex2_attempt, ex3_attempt, ex4_attempt]

        self.progress_chart_banner = ProgressBannerWidget(self, "Progress chart")
        self.ui.verticalLayout_2.insertWidget(0, self.progress_chart_banner)

        all_ex_attempt = self.app.db.get_attempt_in_exercise()
        self.progress_chart = ProgressChartWidget(self, all_ex_attempt)
        self.progress_chart_banner.ui.verticalLayout_2.insertWidget(0,self.progress_chart)
        

        # past attempts

        self.past_attempts_banner = ProgressBannerWidget(self, "Past attempts")
        self.ui.verticalLayout_2.insertWidget(1, self.past_attempts_banner)

        # tester attempts
        #adis_good_attempt = Attempt(4, "30-2-2022", 10, "10:00", 1, 78, "bankai") # TODO: should be numbers for exercise_id, but might need some way to link exercise_ids to titles
        #ths_good_attempt = Attempt(3, "32-1-2022", 15, "01:70", 1, 90, "code no jutsu")
        #yans_good_attempt = Attempt(2, "20-1-2022", 15, "10:00", 1, 83, "bankai")
        #srees_failed_attempt = Attempt(1, "32-12-2021", 100, "04:20", 1, 5, "code no jutsu") # oldest attempt

        # get a list of attempts with newest attempt as 1st element
        #_all_attempts = [adis_good_attempt, ths_good_attempt, yans_good_attempt, srees_failed_attempt]
        _all_attempts = self.app.db.get_all_attempts()

        for _attempt in _all_attempts:
            _history_card = HistoryCardWidget(self.past_attempts_banner.ui.scrollArea, _attempt, None)
            self.past_attempts_banner.ui.verticalLayout_2.insertWidget(0,_history_card)

    def add_attempt(self, attempt):
        _history_card = HistoryCardWidget(self.past_attempts_banner.ui.scrollArea, attempt, None)
        self.past_attempts_banner.ui.verticalLayout_2.insertWidget(0,_history_card)
