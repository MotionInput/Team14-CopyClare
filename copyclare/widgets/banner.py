"""
Contributors: Adi Bozzhanov, Yan Lai

"""

from copyclare.widgets import VideoCardWidget
from copyclare.pyui.banner import Ui_Frame
from copyclare import UiElement
from copyclare.widgets.video_card_my_ex import VideoCardMyExWidget


class BannerWidget(UiElement):
    def __init__(self, master, title, exercises):
        super().__init__(master, "banner", Ui_Frame)
        self.cards = {}
        self.ui.category_title.setText(title)

        if title == "My Exercises":
            self.init_my_exercises(exercises)
        else:
            self.init_exercises(exercises)

    def init_exercises(self, exercises):
        """
        Initialise video cards in banner for all tags except for 'My Exercises'.

        Args:
            exercises ([Exercise]): List of Exercise objects holding the same tag.

        """
        for exercise in exercises:
            self.cards[str(exercise.id)] = VideoCardWidget(
                self.ui.scrollArea, exercise)
            self.ui.horizontalLayout.insertWidget(0,
                                                  self.cards[str(exercise.id)])

    def init_my_exercises(self, exercises):
        """
        Initialise video cards in banner for 'My Exercises' tag.

        Args:
            exercises ([Exercise]): List of Exercise objects holding the 'My Exercises' tag.

        """
        for exercise in exercises:
            self.cards[str(exercise.id)] = VideoCardMyExWidget(
                self.ui.scrollArea, exercise)
            self.ui.horizontalLayout.insertWidget(0,
                                                  self.cards[str(exercise.id)])
